import os
import re
import glob

GENERIC_HEADINGS = {"paper summary", "summary"}


def title_from_filename(file_path):
    """Infer a readable paper title from filename when markdown title is generic."""
    base = os.path.splitext(os.path.basename(file_path))[0]

    # Remove leading year (e.g., 2026-...)
    m = re.match(r'^(?:19|20)\d{2}[-_ ]+(.*)$', base)
    if m:
        base = m.group(1)

    # Drop a likely leading author/journal token (e.g., "Nguyen-", "Nature Communications-")
    if '-' in base:
        base = base.split('-', 1)[1]
    elif '_' in base:
        base = base.split('_', 1)[1]

    title = re.sub(r'[_-]+', ' ', base).strip()
    if title and title[0].islower():
        title = title[0].upper() + title[1:]
    return title or os.path.basename(file_path)


def extract_title(content, file_path):
    # Prefer first H1 heading if it is not generic.
    title_match = re.search(r'^#\s+(.*)', content, re.MULTILINE)
    if title_match:
        heading = title_match.group(1).strip()
        heading_lower = heading.lower().strip(': ')

        if heading_lower not in GENERIC_HEADINGS and not heading_lower.startswith('paper summary'):
            return heading

        # Handle "Paper Summary: <real title>" style.
        suffix_match = re.match(r'(?i)^paper summary\s*:\s*(.+)$', heading)
        if suffix_match:
            return suffix_match.group(1).strip()

    # Then try explicit title metadata variants.
    title_patterns = [
        r'^\*\*Title:\*\*\s*(.+)$',
        r'^\*\*Paper Title:\*\*\s*(.+)$',
        r'^Title:\s*(.+)$',
        r'^###\s+Title\s*$\n^\s*-\s+(.+)$',
    ]
    for pattern in title_patterns:
        match = re.search(pattern, content, re.IGNORECASE | re.MULTILINE)
        if match:
            return match.group(1).strip()

    return title_from_filename(file_path)


def parse_markdown(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    title = extract_title(content, file_path)

    # Year: extract from common metadata lines.
    year = None
    year_patterns = [
        r'\*\*Year:\*\*\s*(?:.*?)(\b(?:19|20)\d{2}\b)',
        r'\*\*Published:\*\*\s*(?:.*?)(\b(?:19|20)\d{2}\b)',
        r'\*\*Publication:\*\*\s*(?:.*?)(\b(?:19|20)\d{2}\b)',
        r'^\s*-\s*(?:.*?)(\b(?:19|20)\d{2}\b)\s*$',
        r'^###\s+Publication Date\s*$\n^\s*-\s*(?:.*?)(\b(?:19|20)\d{2}\b)',
        r'Year:\s*(\b(?:19|20)\d{2}\b)'
    ]
    for pattern in year_patterns:
        # Search from the end of matching line if possible
        match = re.search(pattern, content, re.MULTILINE)
        if match:
            # If there are multiple matches on the line, take the last one that looks like a year
            line_end = content.find('\n', match.start())
            line = content[match.start():line_end]
            all_years = re.findall(r'\b(19\d{2}|20\d{2})\b', line)
            if all_years:
                year = all_years[-1]
            else:
                year = match.group(1)
            break
    
    # If not found, extract from filename prefix.
    if not year:
        filename_match = re.match(r'^((?:19|20)\d{2})[-_ ]', os.path.basename(file_path))
        if filename_match:
            year = filename_match.group(1)

    # Last fallback: search whole file for first plausible year.
    if not year:
        match = re.search(r'(20\d{2}|19\d{2})', content)
        if match:
            year = match.group(1)
        else:
            year = "Unknown"

    # Keywords: Look for Keywords: or *Keywords:*
    keywords = []
    keyword_patterns = [
        r'\*Keywords:\*\s*(.*)',
        r'Keywords:\s*(.*)'
    ]
    for pattern in keyword_patterns:
        match = re.search(pattern, content, re.IGNORECASE)
        if match:
            line = match.group(1).strip()
            # Remove trailing * if exists
            line = line.rstrip('*').strip()
            # Split by comma or semicolon
            split_keywords = re.split(r',|;', line)
            keywords = [k.strip() for k in split_keywords if k.strip()]
            break
            
    return {
        'title': title,
        'year': year,
        'keywords': keywords,
        'file': os.path.basename(file_path)
    }

def generate_readme():
    files = glob.glob('*.md')
    # Filter out README.md and other non-article files if necessary
    articles = []
    for f in files:
        if f.lower() in ['readme.md']:
            continue
        articles.append(parse_markdown(f))

    # Sort by numeric year (desc), keeping Unknown at the end, then title.
    def sort_key(article):
        year_str = str(article['year'])
        year_num = int(year_str) if re.fullmatch(r'(19|20)\d{2}', year_str) else -1
        return (year_num, article['title'].lower())

    articles.sort(key=sort_key, reverse=True)

    with open('README.md', 'w', encoding='utf-8') as f:
        f.write("# Literature Summaries\n\n")
        f.write("Automatically generated list of literature summaries.\n\n")

        # (1) List of articles ordered by year
        f.write("## Articles by Year\n\n")
        current_year = None
        for art in articles:
            if art['year'] != current_year:
                current_year = art['year']
                f.write(f"### {current_year}\n\n")
            f.write(f"- [{art['title']}]({art['file']})\n")
        f.write("\n")

        # (2) List of keywords and under each keyword a list of articles
        f.write("## Articles by Keyword\n\n")
        keyword_map = {}
        for art in articles:
            for kw in art['keywords']:
                kw_lower = kw.lower()
                if kw_lower not in keyword_map:
                    keyword_map[kw_lower] = {'display': kw, 'articles': []}
                keyword_map[kw_lower]['articles'].append(art)
        
        # Sort keywords alphabetically
        sorted_keywords = sorted(keyword_map.keys())
        for kw_key in sorted_keywords:
            kw_data = keyword_map[kw_key]
            f.write(f"### {kw_data['display']}\n\n")
            for art in kw_data['articles']:
                f.write(f"- [{art['title']}]({art['file']}) ({art['year']})\n")
            f.write("\n")

if __name__ == "__main__":
    generate_readme()
