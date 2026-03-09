from flask import Flask, request, render_template
from flasgger import Swagger

app = Flask(__name__)

# Swagger configuration
swagger = Swagger(app)

@app.route("/butet")
def butet():
    """
    Example endpoint returning a rendered template.

    ---
    parameters:
      - name: name
        in: query
        type: string
        required: false
        default: Flask
        description: Name of the user
    responses:
      200:
        description: Rendered HTML page
    """
    name = request.args.get("name")
    return render_template("startpage.html", user_name=name)


@app.route("/basics")
def basics():
    """
    Another example endpoint.

    ---
    parameters:
      - name: name
        in: query
        type: string
        required: trufe
        default: Flask
        description: Name of the user
    responses:
      200:
        description: Rendered HTML page
    """
    name = request.args.get("name")
    return render_template("basics.html", user_name=name)

@app.route("/subscribe", methods=["POST"])
def subscribe():
    user_email = request.form.get("email")
    print(f"NEW SUBSCRIBER!!! Email: {user_email}")
    return f"<h1> Success!</h1><p>Thanks {user_email}has been added. </p><a href='/butet'>Go back</a>"

if __name__ == "__main__":
    app.run(debug=True)