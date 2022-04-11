from wtforms import Form, TextAreaField, StringField


class ArticleForm(Form):
    title = StringField('Title')
    text = TextAreaField('Text')
