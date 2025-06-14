import os
import PyPDF2
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

PDF_PATH = os.path.join(os.path.dirname(__file__), 'encyclopedia.pdf')
EMBEDDINGS_PATH = os.path.join(os.path.dirname(__file__), 'faiss_index.bin')
CHUNKS_PATH = os.path.join(os.path.dirname(__file__), 'chunks.npy')

MODEL_NAME = 'all-MiniLM-L6-v2'


def load_pdf_chunks(pdf_path=PDF_PATH, chunk_size=500):
    reader = PyPDF2.PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n\n" 
    # Split into chunks
    chunks = [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]
    return chunks


def embed_chunks(chunks, model_name=MODEL_NAME):
    model = SentenceTransformer(model_name)
    embeddings = model.encode(chunks, show_progress_bar=True)
    return embeddings


def build_faiss_index(embeddings):
    dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(embeddings)
    return index


def save_index(index, path=EMBEDDINGS_PATH):
    faiss.write_index(index, path)

def load_index(path=EMBEDDINGS_PATH):
    return faiss.read_index(path)

def save_chunks(chunks, path=CHUNKS_PATH):
    np.save(path, np.array(chunks))

def load_chunks(path=CHUNKS_PATH):
    return np.load(path, allow_pickle=True).tolist()


def prepare_pdf_index():
    if not os.path.exists(EMBEDDINGS_PATH) or not os.path.exists(CHUNKS_PATH):
        chunks = load_pdf_chunks()
        embeddings = embed_chunks(chunks)
        index = build_faiss_index(np.array(embeddings))
        save_index(index)
        save_chunks(chunks)
    else:
        index = load_index()
        chunks = load_chunks()
    return index, chunks 