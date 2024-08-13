from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.api.router import api_router


app = FastAPI(title='API Preditor de Tempo')
app.include_router(api_router)


@app.get("/", include_in_schema=False)
def index():
    return {"message": "Default API, index url"}

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(
        "app:app",
        reload=True,
        host="0.0.0.0", 
        port=8000
    )