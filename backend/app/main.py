from fastapi import FastAPI
from app.routes.health import router as health_router
from app.routes.upload import router as upload_router
from app.routes.documents import router as documents_router

app = FastAPI()
app.include_router(health_router)
app.include_router(upload_router)
app.include_router(documents_router)
