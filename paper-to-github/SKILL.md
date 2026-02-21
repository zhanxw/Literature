---
name: paper-to-github
description: Read a research paper and create a structured markdown summary in the repository root with required sections (keywords, main idea, novelty, datasets, experimental procedure, and supporting evidence), using filename format year-author-last-name-title.md, then commit and push to GitHub. Use when users ask to summarize papers and publish results to a repo.
---

# Paper to GitHub

Follow this workflow each time.

## 1. Gather inputs

- Identify the paper source (PDF path, URL, or text).
- Extract or confirm: publication year, first author last name, and short title.
- If paper input is missing, request a concrete path or URL before proceeding.

## 2. Read and extract evidence

- Read the full paper or all available sections.
- Capture only claims supported by methods/results in the paper.
- Track evidence that directly supports the central claim (metrics, ablations, statistical tests, comparisons, or qualitative results).

## 3. Create the summary markdown

- Create one markdown file at repo root with this exact filename pattern:
`<year>-<first-author-last-name>-<title>.md`
- Normalize title for filenames:
  - Keep ASCII when possible.
  - Replace spaces with hyphens.
  - Remove filename-unsafe characters.

Use this section structure:

```markdown
# <Paper Title>

## Bibliographic info
- Year:
- Authors:
- Venue:
- DOI/URL:

## Keywords
- ...

## Main idea
...

## Main novelty
...

## Datasets used for evaluation
- Dataset:
  - Type:
  - Size/splits:
  - Role in evaluation:

## Experimental procedure
1. ...
2. ...
3. ...

## Evidence supporting the main idea
- Evidence:
  - Experiment/setup:
  - Result (with numbers when available):
  - Why it supports the claim:

## Limitations and caveats
...
```

## 4. Quality checks

- Verify all required sections exist.
- Verify evidence statements are traceable to paper content.
- Verify filename follows the required naming format.

## 5. Commit and push

- Stage only intended files.
- Commit with a descriptive message.
- Push to the configured remote branch.
- If using a token, pass it through environment variables or credential helper; do not write it into files.
