from flask import Flask, render_template, request 
from pwdGen import pwdGenerator
import db

# DB_PATH = "database/site_log.db"
DB_PATH = "/home/KerimkulovaB/database/site_log.db"

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/page_2", methods=["GET", "POST"])
def p_2():
    result = ""
    if request.method == "POST":
        password = request.form.get("pwd")
        salt = request.form.get("salt")
        n_char = request.form.get("num_char")

        if password != "":
            result = pwdGenerator(password, salt, n_char)
            db.write_db(DB_PATH, [(password, salt, n_char,result)])

    return render_template("page_2.html", par_1=result)

@app.route("/page_3")
def p_3():
    return render_template("page_3.html", data=db.read_db(DB_PATH))

# тут обрабатываются GET-запросы с параметрами 
# пример: http://127.0.0.1:5000/test_page?par_1=Begaiym&val_2=abc
# @app.route("/test_page")
# def test():
#     value_1 = request.args.get("par_1")
#     value_2 = request.args.get("val_2")
#     return f"hello from test. Par 1 = {value_1}, Val 1 = {value_2}"

if __name__ == "__main__":
    db.create_db(DB_PATH)
    app.ru() #debug=True)