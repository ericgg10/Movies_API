from fastapi import FastAPI

from src.routers import movies

app = FastAPI(
    title="Movies_API", description="A simple application for CRUD operations with movies"
)

app.include_router(movies.router)


@app.get("/")
def read_root():
    return {"Hola desde el proyecto sobre películas creado por Eric García"}
