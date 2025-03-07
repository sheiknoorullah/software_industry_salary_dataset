from fastapi import FastAPI
from routers import salaries

app = FastAPI()

app.include_router(salaries.router, tags=["salaries"])