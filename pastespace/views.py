from flask import render_template, request

from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter
from pygments import highlight

from pastespace import app


@app.route('/')
@app.route('/new', methods=['GET', 'POST'])
def new():
    if request.method == 'GET':
        return render_template("paste_form.html")
    if request.method == 'POST':
        title = request.form['title']
        text = request.form['text']
        lang = request.form['lang']
        lexer = get_lexer_by_name(lang, stripall=False)
        formatter = HtmlFormatter(linenos=True, cssclass="colorful")
        data = highlight(text, lexer, formatter)
        return render_template('show_paste.html', title=title, data=data)