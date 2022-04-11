from flask_migrate import Migrate
from app import app, db
from models import Article

migrate = Migrate(app, db)
