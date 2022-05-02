import os


def get_sqlite_memory_uri():
    pass


def get_sqlite_file_url():
    return f"sqlite:///orders.db"


def get_api_url():
    host = os.environ.get("API_HOST", "localhost")
    port = 5005 if host == "localhost" else 80
    return f"http://{host}:{port}"
