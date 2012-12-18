from flask import render_template, request, redirect, url_for

from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter
from pygments import highlight

from app import app

from app import db
from models import Paste

from forms import PasteForm


@app.route('/')
@app.route('/new', methods=['GET', 'POST'])
def new():
    form = PasteForm(request.form)
    if request.method == 'POST' and form.validate():
        title = form.title.data
        text = form.text.data
        lang = form.language.data
        lexer = get_lexer_by_name(lang, stripall=False)
        formatter = HtmlFormatter(linenos=True, cssclass="colorful")
        data = highlight(text, lexer, formatter)

        paste = Paste(title=title, data=data, language=lang)
        db.session.add(paste)
        db.session.commit()
        return redirect(url_for('show', paste_id=paste.id))
    return render_template("paste_form.html", form=form)


@app.route('/show/<int:paste_id>')
def show(paste_id):
    paste = Paste.query.get(paste_id)
    return render_template('show_paste.html', paste=paste)


@app.route('/language/<lang>')
def list_pastes(lang):
    pastes = Paste.query.filter(Paste.language == lang)
    return render_template('list_by_language.html', pastes=pastes, lang=lang)
