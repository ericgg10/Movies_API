import pandas as pd

try:
    database_movies = pd.read_csv("data/movies.csv")
except FileNotFoundError:
    print("No se ha encontrado el archivo con la ruta que me has proporcionado")
