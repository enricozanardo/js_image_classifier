import zappa
import logging
from flask import Flask, render_template, jsonify, make_response, abort, url_for, redirect, request

app = Flask(__name__)
logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

@app.route('/ic')
def image_classifier():
    return render_template('image_classifier.html')

@app.route('/')
def index():
    user = "Enrico"
    return render_template('index.html', name=user)

# We only need this for local development.
if __name__ == '__main__':
    app.run(debug=True)