import pdfplumber
from app.utils.text_cleaner import TextCleaner


class PDFService:

    def extract_text(self, file_path):

        text = ""

        with pdfplumber.open(file_path) as pdf:

            for page in pdf.pages:

                page_text = page.extract_text()

                if page_text:
                    text += page_text + "\n"

        return TextCleaner.clean(text)
