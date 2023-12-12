from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import qrcode_generator

app = FastAPI(debug=False)

origins = [
    "*",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(qrcode_generator.router)
