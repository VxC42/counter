from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)

app.secret_key = 'F12Zr47j\3yX R~X@H!jmM]Lwf/,?KT'

def countSession():
    try:
        session['counter']+=1
    except KeyError:
        session['counter']=1

@app.route('/')
def index():
    countSession()
    return render_template("index.html", number = session['counter'])


app.run(debug=True)
