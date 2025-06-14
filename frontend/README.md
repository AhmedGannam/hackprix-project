# Medical AI Doctor Chatbot Frontend

This is the Ionic Angular frontend for the Medical AI Doctor Chatbot.

## Features
- Chat interface to interact with an AI-powered doctor
- Connects to a Python FastAPI backend for medical Q&A

## Setup
1. Install dependencies:
   ```bash
   npm install
   ```
2. Start the development server:
   ```bash
   ionic serve
   ```
   The app will be available at `http://localhost:8100` by default.

## Usage
- Navigate to the "Doctor Chatbot" page using the footer button.
- Type your medical question and receive answers from the AI doctor.

## Project Structure
- `src/app/doctor-chatbot/` — Doctor chatbot page and logic
- `src/app/home/` — Home page

## Notes
- Ensure the backend is running at `http://localhost:8000` for API calls.
- Update the API URL in `doctor-chatbot.page.ts` if your backend runs elsewhere. 