import zipfile
import uuid
from lxml import etree

NS = {
    'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main',
    'r': 'http://schemas.openxmlformats.org/officeDocument/2006/relationships'
}

class Commenter:
    def add_comment_to_docx(self, input_docx, output_docx, comments):
        with zipfile.ZipFile(input_docx, 'r') as zin:
            items = {name: zin.read(name) for name in zin.namelist()}

        if 'word/comments.xml' in items:
            root = etree.fromstring(items['word/comments.xml'])
        else:
            root = etree.Element('{%s}comments' % NS['w'], nsmap={'w': NS['w']})

        for c in comments:
            comment_id = str(uuid.uuid4().int % 1000000)
            comment_node = etree.SubElement(root, '{%s}comment' % NS['w'], id=comment_id, author=c.get('author', 'Agent'))
            p = etree.SubElement(comment_node, '{%s}p' % NS['w'])
            r = etree.SubElement(p, '{%s}r' % NS['w'])
            t = etree.SubElement(r, '{%s}t' % NS['w'])
            t.text = c.get('text')

        items['word/comments.xml'] = etree.tostring(root, xml_declaration=True, encoding='UTF-8', standalone='yes')

        with zipfile.ZipFile(output_docx, 'w') as zout:
            for name, data in items.items():
                zout.writestr(name, data)

        return output_docx
