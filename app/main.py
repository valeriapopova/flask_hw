from app import app
import view
from app import db
from articles.blueprint import articles

app.register_blueprint(articles, url_prefix='/articles')

if __name__ == '__main__':
    app.run()
