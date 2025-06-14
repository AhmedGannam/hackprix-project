---

## ⚙ Prerequisites

- Node.js (LTS) & npm
- Ionic CLI (npm install -g @ionic/cli)
- Conda or Python 3.11
- Git
- MySQL (optional for later stages)

---

## 🚀 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-org/medical-care-hub.git
cd medical-care-hub

cd backend
conda create -p ./venv python=3.11 -y
conda activate ./venv
pip install -r requirements.txt

DATABASE_URL=mysql+aiomysql://username:password@localhost:3306/db_name
OPENAI_API_KEY=your_openai_key

cd ../frontend
npm install

cd medical‑care‑hub/backend
conda activate ./venv
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

# Medical AI Doctor Chatbot Backend

This backend powers an AI doctor chatbot using The Gale Encyclopedia of Medicine PDF as its knowledge base.

## Setup Instructions

1. **Place the PDF**
   - Put your `encyclopedia.pdf` file in `backend/app/encyclopedia.pdf`.

2. **Install Dependencies**
   - Create and activate your conda environment if not already done.
   - Install requirements:
     ```bash
     pip install -r requirements.txt
     ```

3. **Set OpenAI API Key**
   - Create a `.env` file in `backend/app/` with:
     ```env
     OPENAI_API_KEY=your_openai_key_here
     ```
   - Or set the environment variable in your shell.

4. **Run the Backend**
   ```bash
   uvicorn app.main:app --reload
   ```

5. **API Endpoint**
   - POST `/ask` with JSON `{ "question": "your medical question" }`
   - Returns: `{ "answer": "AI-generated answer" }`

## Notes
- On first run, the PDF will be processed and indexed (may take a few minutes).
- Make sure your PDF is not scanned images (text must be extractable).

