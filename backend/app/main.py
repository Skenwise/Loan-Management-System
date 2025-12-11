from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Loan Management System ")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "https://vat-management-system-choma.vercel.app", "http://localhost:8080", "http://localhost/"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
