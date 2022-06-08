from fastapi import FastAPI
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware
from src.router.Log import log
from src.router.StatusSensor import statusSensor

from src.documentation.Doc import tags_metadatas
import uvicorn

app = FastAPI(
    title="REST API to passport system",
    description="By ISW UV",
    version="0.5",
    openapi_tags=tags_metadatas
)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(log, prefix='/api',tags=["Log"])
app.include_router(statusSensor, prefix='/api',tags=["Status"])

load_dotenv()

if __name__ == "__main__":
    uvicorn.run(app, port=9090, host="0.0.0.0")