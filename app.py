from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "mitutee`s Flask is here!"

if __name__==("__main__"):
    app.run()