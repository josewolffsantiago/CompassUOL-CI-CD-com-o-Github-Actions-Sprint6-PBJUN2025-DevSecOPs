from fastapi import FastAPI
app = FastAPI()
@app.get("/")
async def root():
    return {"message": "Hello World 3ffadc495fd30fdc7cf08504ada4fbe0bea0d74e"}
