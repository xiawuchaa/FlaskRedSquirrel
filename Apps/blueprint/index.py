from flask import render_template
from Apps.blueprint import api


@api.route('/index')
def hello_world():
    return render_template('index.html')