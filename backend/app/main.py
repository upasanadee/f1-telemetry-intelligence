from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# ==========================================================
# APP
# ==========================================================

app = FastAPI(
    title="F1 Telemetry Intelligence API",
    description="Research-grade AI telemetry backend for Formula 1 analytics.",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

# ==========================================================
# CORS
# ==========================================================

origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ==========================================================
# ROOT
# ==========================================================

@app.get("/")
def root():
    return {
        "project": "F1 Telemetry Intelligence",
        "version": "1.0.0",
        "status": "running",
        "docs": "/docs",
    }

# ==========================================================
# HEALTH CHECK
# ==========================================================

@app.get("/health")
def health():
    return {
        "status": "healthy",
        "backend": "FastAPI",
        "version": "1.0.0",
    }