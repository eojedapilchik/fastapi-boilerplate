import os
from fastapi import FastAPI
from dotenv import load_dotenv
from app.routers import health_router, hello_router

load_dotenv()

app = FastAPI()
app.include_router(health_router)
app.include_router(hello_router)

clean_cloud_api = os.getenv('CLEANCLOUD_API')
clearent_api = os.getenv('CLEARENT_API')

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000)
