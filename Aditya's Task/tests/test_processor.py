from processor import DocProcessor

def test_detect_type():
    p = DocProcessor()
    text = "This is the Articles of Association."
    assert p.detect_type(text) == "articles of association"

def test_signature_issue():
    p = DocProcessor()
    doc_text = "Board Resolution\nSome content without signature"
    issues = p.find_signature_issues(doc_text)
    assert any("signature" in i['issue'].lower() for i in issues)