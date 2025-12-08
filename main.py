from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import engine, Base
from routes import electricity, electronicName, electronic, calculator

Base.metadata.create_all(bind=engine)

openapi_tags = [
    {"name": "Electricity", "description": "Endpoints terkait biaya listrik"},
    {"name": "Electronic Name", "description": "Endpoints terkait alat elektronik"},
    {"name": "Electronic Data", "description": "Endpoints terkait alat elektronik"},
    {"name": "Calculator", "description": "Endpoints untuk kalkulasi biaya energi"}
]

app = FastAPI(openapi_tags=openapi_tags)

# 🔥 Tambahkan ini
origins = [
    "http://localhost",
    "http://localhost:8000",
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(electricity.router, prefix="/electricity", tags=["Electricity"])
app.include_router(electronicName.router, prefix="/electronic-name", tags=["Electronic Name"])
app.include_router(electronic.router, prefix="/electronic-data", tags=["Electronic Data"])
app.include_router(calculator.router, prefix="/calculator", tags=["Calculator"])
