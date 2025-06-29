
# Full-Stack Debug & Feature Test

Welcome! This is a full-stack take-home test. The app is partially functional and contains a few bugs. Your task:

1. Debug and fix the application so it runs correctly.
2. Implement filtering and sorting of feedback by rating and date.
3. Refactor any part of the code you find necessary.
4. Add appropriate test coverage.

## How to Run

### Backend
```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install flask
pip install flask-cors
python app.py
```

### Frontend
```bash

npm create vite@latest frontend –template react
Ignore existing files
Select React and Javascript in the next steps
Above steps create a default App.jsx, replace this file from the project App.jsx file

npm install

Add "start": "vite", in package-json in “scripts” section


cd frontend
npm start
```

## Submission
Push your changes to GitHub and send us the link. Include notes in a PR or README on:
- Bugs you fixed
- Design decisions you made
- Any improvements/refactors
