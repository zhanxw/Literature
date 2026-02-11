import os
import re
import glob

def parse_markdown(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Title: First # heading
    title_match = re.search(r'^#\s+(.*)', content, re.MULTILINE)
    title = title_match.group(1).strip() if title_match else os.path.basename(file_path)

    # Year: Extract from **Year:**, **Published:**, or **Publication:**
    # Look for 4 digits in those lines, preferring 19xx or 20xx
    year = None
    year_patterns = [
        r'\*\*Year:\*\*\s*(?:.*?)(\b(?:19|20)\d{2}\b)',
        r'\*\*Published:\*\*\s*(?:.*?)(\b(?:19|20)\d{2}\b)',
        r'\*\*Publication:\*\*\s*(?:.*?)(\b(?:19|20)\d{2}\b)',
        r'Year:\s*(\b(?:19|20)\d{2}\b)'
    ]
    for pattern in year_patterns:
        # Search from the end of matching line if possible
        match = re.search(pattern, content)
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
    
    # If not found, try to extract from filename or just look for 20xx in the whole file
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

    # Sort by year (desc) and then title
    articles.sort(key=lambda x: (x['year'], x['title']), reverse=True)

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
