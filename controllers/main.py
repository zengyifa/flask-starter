from flask import *
from extensions import mysql

main = Blueprint('main', __name__, template_folder='templates')

@main.route('/')
def main_route():
    return render_template("index.html")
@main.route('/hello')
def hello():
    cur = mysql.connection.cursor()
    cur.execute('''SELECT * FROM discussion1.messages''')    
    msgs = cur.fetchall()
    output = "<br>".join("Message #{0}: {1}".format(msgs.index(msg), msg[0]) for msg in msgs)
    return output
