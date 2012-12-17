from flask import Flask

app = Flask(__name__)
app.config.from_object('pastespace.config')

from pastespace import views
