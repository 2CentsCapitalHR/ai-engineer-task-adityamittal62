# Analyzer placeholder
import zipfile
from processor import DocProcessor
from commenter import Commenter
from rag import RAG

class Analyzer:
    def __init__(self):
        self.processor = DocProcessor()
        self.commenter = Commenter()
        self.rag = RAG()

    def run(self, paths):
        reports = []
        comments_all = []

        for p in paths:
            res = self.processor.run_checks(p)
            reports.append(res)
            for issue in res['issues']:
                comments_all.append({
                    'para_index': 0,
                    'author': 'ADGM-Agent',
                    'text': f"{issue['issue']} - {issue['suggestion']}"
                })

        reviewed_paths = []
        for p in paths:
            out = p.replace('.docx', '_reviewed.docx')
            self.commenter.add_comment_to_docx(p, out, comments_all)
            reviewed_paths.append(out)

        zipname = 'reviewed_output.zip'
        with zipfile.ZipFile(zipname, 'w') as zf:
            for rp in reviewed_paths:
                zf.write(rp)

        final_report = {
            'process': 'Company Incorporation',
            'documents_uploaded': len(paths),
            'required_documents': 5,
            'missing_document': 'Register of Members and Directors' if len(paths) < 5 else None,
            'issues_found': reports
        }
        return {'reviewed_zip': zipname, 'report': final_report}
