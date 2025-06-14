import os
from openai import OpenAI
from sentence_transformers import SentenceTransformer
import numpy as np
from .pdf_ingest import prepare_pdf_index, MODEL_NAME


client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

index, chunks = prepare_pdf_index()
model = SentenceTransformer(MODEL_NAME)


def answer_question(question, k=5):
    # Embed the question
    q_emb = model.encode([question])
    # Search FAISS
    D, I = index.search(np.array(q_emb).astype('float32'), k)
    context = "\n".join([chunks[i] for i in I[0]])
    # Compose prompt
    prompt = f"You are a helpful medical assistant. Use the following context from a medical encyclopedia to answer the question.\nContext:\n{context}\n\nQuestion: {question}\nAnswer:"
    # Call OpenAI
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": "You are a helpful medical assistant."},
                  {"role": "user", "content": prompt}],
        max_tokens=512,
        temperature=0.2
    )
    return response.choices[0].message.content.strip()