from flask import Flask
# from flask_login import LoginManager

from config import Configuration
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

app = Flask(__name__)
app.config.from_object(Configuration)

db = SQLAlchemy(app)

# login_manager = LoginManager(app)

from models import *


class BaseModelView(ModelView):
    def on_model_change(self, form, model, is_created):
        model.generate_slug()
        return super(BaseModelView, self).on_model_change(form, model, is_created)


class ArticleAdminView(BaseModelView):
    form_columns = ['title', 'text']


admin = Admin(app)
admin.add_view(ArticleAdminView(Article, db.session))


