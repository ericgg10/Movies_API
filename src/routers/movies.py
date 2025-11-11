from fastapi import APIRouter

from ..services.movies_db import get_movies_by_id

router = APIRouter(prefix="/movies", tags=["Movies"])


@router.get("/movie/{id}")
def get_movie(id: int):
    return get_movies_by_id(id)
