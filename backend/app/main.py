# source .venv/bin/activate
# uvicorn app.main:app --reload

from fastapi import FastAPI

app = FastAPI(title="API Controle Financeiro")