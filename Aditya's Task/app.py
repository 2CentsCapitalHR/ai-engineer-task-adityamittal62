import os
import gradio as gr
from analyzer import Analyzer

OPENAI_KEY = os.getenv('OPENAI_API_KEY')

analyzer = Analyzer()

def analyze_files(files):
    uploads = [f.name for f in files]
    results = analyzer.run(uploads)
    return results['reviewed_zip'], results['report']

iface = gr.Interface(
    fn=analyze_files,
    inputs=gr.File(file_count="multiple", file_types=[".docx"]),
    outputs=[
        gr.File(label="Reviewed .docx (ZIP)"),
        gr.JSON(label="Report")
    ],
    flagging_mode="never",
    title="ADGM Corporate Agent"
)

if __name__ == "__main__":
    iface.launch(server_name="0.0.0.0", share=False)
