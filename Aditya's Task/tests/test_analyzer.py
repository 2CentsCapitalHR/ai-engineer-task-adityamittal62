from analyzer import Analyzer
import os

def test_analyzer_runs(tmp_path):
    # Create dummy docx file
    from docx import Document
    doc_path = tmp_path / "dummy.docx"
    Document().save(doc_path)

    analyzer = Analyzer()
    res = analyzer.run([str(doc_path)])
    assert 'report' in res
    assert os.path.exists(res['reviewed_zip'])
