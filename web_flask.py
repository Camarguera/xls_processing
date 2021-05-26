from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route('/xls_processing', methods=["GET", "POST"])
def xls_processing():
    if request.method == "POST":
        min_limit = request.form.get("min_limit")
        max_limit = request.form.get("max_limit")
        file_name = request.form.get("formFile")


if __name__ == "__main__":
    app.run(debug=True)
