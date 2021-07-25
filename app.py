from flask import Flask, render_template, request, redirect
from user_db import db, fetch_db, mod_db, del_user, del_all
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
        elif request.form.get("delete"):
            return render_template("delete.html")
    else:
        return redirect('/')


@app.route("/modification", methods=["POST"])
def user_mod():
    if request.method == "POST":
        email = request.form.get("email")
        # return (str(request.form.get("User_Details")))
        if str(request.form.get("User_Details")) == "Name":
            name = request.form.get("in")
        else:
            name = None
        if str(request.form.get("User_Details")) == "Faculty Name":
            company = request.form.get("in")
        else:
            company = None
        if str(request.form.get("User_Details")) == "Contact Number":
            contact = request.form.get("in")
        else:
            contact = None
        if str(request.form.get("User_Details")) == "Remarks":
            message = request.form.get("in")
        else:
            message = None
        res, code = mod_db(name, email, company, contact, message)
        if code == True:
            return redirect('/')
        else:
            return("<h1>Failed to query !! <a href='output.html'>Go back!</a></h1>")
    else:
        return("<h1>Error 404</h1>")


@app.route("/delete", methods=["POST"])
def user_del():
    if request.method == "POST":
        if request.form.get("delete"):
            name = request.form.get("name")
            email = request.form.get("email")
            res, code = del_user(name, email)
            if(code == True):
                return("<h1 style='color:green'>User deleted successfully <a href='/'>Click to return</a></h1>")
            else:
                return("<h1>404 error</h1>")
        elif request.form.get("fetch"):
            res, code = fetch_db()
            if(code == True):
                html_code = render_template("output.html", res=res)
                return(html_code)
            else:
                return("<h1>404 error</h1>")
        elif request.form.get("delete_all"):
            code = del_all()
            if(code == True):
                return("<h1 style='color:green'>Your collection is clean <a href='/'>Click to return</a></h1>")


if __name__ == '__main__':
    app.run(debug=True)
