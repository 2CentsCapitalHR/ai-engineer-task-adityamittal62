PROMPT_CLAUSE_ANALYSIS = """
You are an ADGM compliance expert.
Given a document section, classify:
1. Whether it's compliant with ADGM rules.
2. If not compliant, suggest a correction.
3. Cite the relevant ADGM regulation text.

Section:
{section}

Relevant ADGM References:
{references}

Respond in JSON:
{{
  "compliant": true/false,
  "issue": "...",
  "suggestion": "...",
  "reference_snippet": "..."
}}
"""

PROMPT_SUMMARY = """
Summarize the compliance findings across all documents.
Highlight:
- Total docs reviewed
- Missing documents
- Number of high/medium/low severity issues
- ADGM citations used
"""
