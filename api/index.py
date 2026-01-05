from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "BDKazi API Running on Vercel ✅"
