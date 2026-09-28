from pathlib import Path

from pypdf import PdfReader
from docx import Document


def document_reader(state):

    ext = Path(
        state.file_path
    ).suffix.lower()

    text = ""

    if ext == ".pdf":

        reader = PdfReader(
            state.file_path
        )

        for page in reader.pages:

            page_text = page.extract_text()

            if page_text:
                text += page_text

    elif ext == ".docx":

        doc = Document(
            state.file_path
        )

        text = "\n".join(
            paragraph.text
            for paragraph in doc.paragraphs
        )

    else:

        raise ValueError(
            "Only PDF and DOCX supported"
        )

    return {
        "resume_text": text
    }