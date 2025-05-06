from fastapi import FastAPI
from app.routers import auth
from app.routers import test
from app.routers import router
from app.database import engine, Base

# Create database tables
Base.metadata.create_all(bind=engine)

#app = FastAPI()
app = FastAPI(
    title="MyApp",
    version="0.1.0",
    description="API для моего проекта",
    docs_url="/docs",         # <-- Swagger UI
    redoc_url="/redoc",       # <-- ReDoc
    openapi_url="/openapi.json"
)
app.include_router(auth.router)
app.include_router(test.router)
app.include_router(router.router)
