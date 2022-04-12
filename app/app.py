from flask import Flask, redirect, request, url_for
from config import Configuration
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_security import current_user, SQLAlchemyUserDatastore, Security

app = Flask(__name__)
app.config.from_object(Configuration)

db = SQLAlchemy(app)


from models import *


class AdminMixin:
    def is_accessible(self):
        return current_user.has_no_role('admin')

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('security.login', next=request.url))


class BaseModelView(ModelView):
    def on_model_change(self, form, model, is_created):
        model.generate_slug()
        return super(BaseModelView, self).on_model_change(form, model, is_created)


class ArticleAdminView(AdminMixin, BaseModelView):
    form_columns = ['title', 'text']


admin = Admin(app)
admin.add_view(ArticleAdminView(Article, db.session))
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)


