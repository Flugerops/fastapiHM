from .. import app


@app.get("/")
def home():
    return {"hello": "world"}

