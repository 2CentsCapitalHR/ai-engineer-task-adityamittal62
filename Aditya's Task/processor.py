import re
from docx import Document

class DocProcessor:
    def __init__(self):
        self.type_map = {
            'articles of association': ['articles of association', 'aoa'],
            'memorandum of association': ['memorandum of association', 'moa'],
            'board resolution': ['board resolution', 'resolution']
        }

    def load(self, path):
        doc = Document(path)
        text = "\n".join(p.text for p in doc.paragraphs)
        return doc, text

    def detect_type(self, text):
        t = text.lower()
        for typ, keys in self.type_map.items():
            for k in keys:
                if k in t:
                    return typ
        return 'unknown'

    def find_jurisdiction_issues(self, text):
        issues = []
        if re.search(r"UAE Federal Courts", text, re.I):
            issues.append({
                'section': 'jurisdiction',
                'issue': 'Mentions UAE Federal Courts instead of ADGM Courts',
                'severity': 'High',
                'suggestion': 'Change jurisdiction clause to ADGM Courts'
            })
        return issues

    def find_signature_issues(self, text):
        issues = []
        if not re.search(r"Signed by", text, re.I):
            issues.append({
                'section': 'signatures',
                'issue': 'Missing signature block',
                'severity': 'Medium',
                'suggestion': 'Add authorized signatory section'
            })
        return issues

    def run_checks(self, path):
        doc, text = self.load(path)
        doc_type = self.detect_type(text)
        issues = []
        issues.extend(self.find_jurisdiction_issues(text))
        issues.extend(self.find_signature_issues(text))
        return {'path': path, 'type': doc_type, 'issues': issues}
