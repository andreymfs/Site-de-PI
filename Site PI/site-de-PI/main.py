from flask import Flask, redirect, url_for,render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route("/admin")
def admin():
    return render_template('admin.html')

@app.route("/user>")
def guest():
    return render_template('user.html')


if __name__ == "__main__":
    app.run(debug=True)
