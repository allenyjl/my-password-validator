import flask


# TODO: change this to your academic email
AUTHOR = "allenyjl@seas.upenn.edu"


app = flask.Flask(__name__)


# This is a simple route to test your server


@app.route("/")
def hello():
    return f"Hello from my Password Validator! &mdash; <tt>{AUTHOR}</tt>"


# This is a sample "password validator" endpoint
# It is not yet implemented, and will return HTTP 501 in all situations


@app.route("/v1/checkPassword", methods=["POST"])
def check_password():
    data = flask.request.get_json() or {}
    pw = data.get("password", "")

    # FIXME: to be implemented
    valid = True
    reason = ""
    if len(pw) < 8:
        valid = False
        reason = "Password must be at least 8 characters long"
    elif not any(c.isupper() for c in pw):
        valid = False
        reason = "Password must contain at least one uppercase letter"
    elif not any(c.isdigit() for c in pw):
        valid = False
        reason = "Password must contain at least one digit."
    elif not any(c in "!@#$%^&*" for c in pw):
        valid = False
        reason = "Password must contain at least one special character from !@#$%^&*."

    return flask.jsonify({"valid": valid, "reason": reason}), 200
