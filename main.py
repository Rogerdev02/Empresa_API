from fastapi import FastAPI
from app.routers import enterprise
from app.database.connection import Base, engine
from app.models.enterprise_model import Enterprise


app = FastAPI(title='API de Empresas')

app.include_router(enterprise.router)

Base.metadata.create_all(bind=engine)