from fastapi import FastAPI

from app.database.connection import Base, engine
from app.models.enterprise_model import Enterprise
from app.routers import enterprise

app = FastAPI(title='API de Empresas')

app.include_router(enterprise.router)

Base.metadata.create_all(bind=engine)
