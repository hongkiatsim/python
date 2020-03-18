from flask import Flask
app = Flask(__name__, static_folder='/')

@app.route('/')
def root():
    return app.route('/')
