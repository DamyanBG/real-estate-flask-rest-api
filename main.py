from config import create_app
from db import db
# from search import es


app = create_app()
app.config["INITIALIZED"] = False

db.init_app(app)


@app.before_request
def init_request():
    if not app.config["INITIALIZED"]:
        db.create_all()
        # es.reindex_homes()
        app.config["INITIALIZED"] = True


if __name__ == "__main__":
    app.run()
