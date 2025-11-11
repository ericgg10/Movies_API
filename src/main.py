from fastapi import FastAPI

app = FastAPI(
    title="Movies_API", description="A simple application for CRUD operations with movies"
)


@app.get("/")
def read_root():
    return {"Hola desde el proyecto sobre películas creado por Eric García"}
