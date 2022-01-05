import flask
import flask_wtf
import wtforms

import model


app = flask.Flask(__name__)


class Form(flask_wtf.Form):
    value = wtforms.StringField("value")
    submit = wtforms.SubmitField("submit")


@app.route("/", methods=["GET", "POST"])
def index():
    if flask.request.method == "GET":
        return flask.render_template("index.html", form=Form())

    elif flask.request.method == "POST":
        form = Form(flask.request.form)
        value = int(form.value.data)
        result = model.predict(value)

        return str(result)
