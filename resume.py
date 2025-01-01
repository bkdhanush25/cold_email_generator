import pdfplumber
import chromadb
__import__('pysqlite3')
import sys
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')
import uuid
from chains import Chain

class Resume:
    def __init__(self):
        self.file_path = ""
        self.chain = Chain()
        self.client = chromadb.PersistentClient("vectorstore")
        self.collection = self.client.get_or_create_collection(name="resume_collection")

    def extract_text_from_pdf(self):
        with pdfplumber.open(self.file_path) as pdf:
            text = ''
            for page in pdf.pages:
                text += page.extract_text(x_tolerance=2, y_tolerance=2) + "\n"
        return text.strip()

    def load_resume(self,pdf_path):
        self.file_path=pdf_path
        chunks = self.extract_text_from_pdf()
        if not self.collection.count():
            for chunk in chunks:
                self.collection.add(
                    documents=[chunk],
                    metadatas={"source": "resume"},
                    ids=[str(uuid.uuid4())]
                )

        return chunks