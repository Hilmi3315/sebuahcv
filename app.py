from flask import Flask, render_template
from flask_ngrok import run_with_ngrok

app = Flask(__name__)

@app.route("/")
def halamancv():
    return render_template("sa-2.html")
    return render_template("sa-2.css")
   
if __name__ == "__main__":
    run_with_ngrok(app)
    app.run()