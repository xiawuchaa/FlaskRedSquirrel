from flask import render_template
from Apps.blueprint import api


@api.route('/user')
def test():
    return render_template('user.html')