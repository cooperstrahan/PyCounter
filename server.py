from flask import Flask, render_template, request, redirect, session
import base64
app = Flask(__name__)
app.secret_key = 'the most secret of the keys'

@app.route('/')
def index():  
    # print(session['value'])
    print(session)
    if 'count' in session:
        session['count'] = session.get('count') + 1
    else:
        session['count'] = 1
    return render_template("index.html")

@app.route('/destroy_session')
def destroy_session():
    session.clear()
    return redirect('/')

if __name__ =="__main__":
    app.run(debug=True)