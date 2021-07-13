from flask import Flask, render_template, request, redirect
from user_db import db, fetch_db, mod_db
app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/output", methods=["POST"])
def form_details():
    if request.method == 'POST':
        if request.form.get("submit"):
            name = request.form.get("name")
            email = request.form.get("email")
            company = request.form.get("company")
            phone = request.form.get("phone")
            message = request.form.get("message")
            res, code = db(name, email, company, phone, message)
            if(code == True):
                html_code = render_template("output.html", res=res)
                return(html_code)
            else:
                return("<h1>404 error</h1>")
        elif request.form.get("fetch"):
            res, code = fetch_db()
            if(code == True):
                html_code = render_template("output.html", res=res)
                return(html_code)
            else:
                return("<h1>404 error</h1>")
    else:
        return redirect('/')


@app.route("/mod", methods=["POST"])
def mod():
    if request.method == "POST":
        if request.form.get("update"):
            pass


if __name__ == '__main__':
    app.run(debug=True)
