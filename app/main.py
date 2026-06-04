from fastapi import FastAPI

app = FastAPI(root_path="/api")

@app.get("/")
async def read_root():
    return {"message": "Hello from FastAPI!"}

@app.get("/health")
async def health_check():
    return {"status": "ok"}
