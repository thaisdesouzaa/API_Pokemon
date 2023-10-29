import os

class ApiConfig():
    URL = os.getenv("URL_POKEAPI")
    ARQ = os.getenv("ARQUIVO")