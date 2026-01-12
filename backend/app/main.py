from fastapi import FastAPI
from app.database import engine
import app.models  # 👈 obrigatório para Alembic/metadata

from app.routers import (
    user,
    permission,
    company,
    group,
    category,
    transaction,
)

app = FastAPI(title="API Controle Financeiro")

# ❌ NÃO usar mais create_all quando usa Alembic
# @app.on_event("startup")
# def on_startup():
#     Base.metadata.create_all(bind=engine)

app.include_router(user.router)
app.include_router(permission.router)
app.include_router(company.router)
app.include_router(group.router)
app.include_router(category.router)
app.include_router(transaction.router)