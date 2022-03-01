from flask import Flask, render_template, request, redirect
from flask.helpers import url_for
from uwusify import uwusify

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def uwu():
    if request.args.get('sentence') == None:
        uwusentence = None
    else:
        uwusentence = uwusify(
            request.args.get('sentence'))

    return render_template("index.html", uwued=uwusentence)


if __name__ == "__main__":
    app.run(debug=True)
