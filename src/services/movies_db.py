from utils.data_loader import database_movies


def get_movies_by_id(id: int):
    query = f"id == {id}"
    result = database_movies.query(query).to_dict(orient="records")[0]
    return result
