from decouple import config

HOST = config("HOST", "0.0.0.0")
PORT = config("PORT", 3000)
DEBUG = config("DEBUG", True)
