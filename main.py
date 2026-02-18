from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello from Skill City demo!"}

@app.get("/health")
def health_check():
    return {"status": "ok"}
