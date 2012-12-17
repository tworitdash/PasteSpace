from flask import render_template, request

from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter
from pygments import highlight

from pastespace import app

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
        return render_template('show_paste.html', title=title, data=data)
    return render_template("paste_form.html", form=form)
