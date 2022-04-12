from flask import Blueprint, render_template, redirect, url_for
from models import Article
from app import db
from flask import request
from .forms import ArticleForm
from flask_security import login_required


articles = Blueprint('articles', __name__, template_folder="templates")


@articles.route('/create', methods=['POST', 'GET'])
@login_required
def create_article():
    if request.method == 'POST':
        title = request.form['title']
        text = request.form['text']
        if title:
            try:
                article = Article(title=title, text=text)
                db.session.add(article)
                db.session.commit()
            except:
                print('сломався')
            return redirect(url_for('articles.index'))

    form = ArticleForm()
    return render_template('articles/create_article.html', form=form)


@articles.route('/<slug>/edit', methods=['POST', 'GET'])
@login_required
def edit_article(slug):
    article = Article.query.filter(Article.slug==slug).first_or_404()

    if request.method == 'POST':
        form = ArticleForm(formdata=request.form, obj=article)
        form.populate_obj(article)
        db.session.commit()

        return redirect(url_for('articles.article_detail', slug=article.slug))
    form = ArticleForm(obj=article)
    return render_template('articles/edit.html', article=article, form=form)


@articles.route('/<slug>/delete')
@login_required
def delete_article(slug):
    article = Article.query.filter(Article.slug==slug).first_or_404()
    try:
        db.session.delete(article)
        db.session.commit()
        return redirect('articles.index')
    except:
        return "проблемка"


@articles.route('/')
def index():
    page = request.args.get('page')
    if page and page.isdigit():
        page = int(page)
    else:
        page = 1

    articles = Article.query

    pages = articles.paginate(page=page, per_page=2)
    return render_template('articles/index.html', articles=articles, pages=pages)


@articles.route('/<slug>')
def article_detail(slug):
    article = Article.query.filter(Article.slug==slug).first_or_404()
    return render_template('articles/article_detail.html', article=article)




