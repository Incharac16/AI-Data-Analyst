from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import analysis, insights, upload

app = FastAPI(
    title="AI Data Analyst API",
    description="Upload datasets, get summaries, charts, and AI insights.",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "https://ai-data-analyst-6oib13v8v-inchara-c-s-projects.vercel.app",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(upload.router)
app.include_router(analysis.router)
app.include_router(insights.router)

@app.get("/health")
async def health():
    return {"status": "ok"}