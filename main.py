from flask import Flask, request, render_template
from flasgger import Swagger
from pymongo import MongoClient
from database import save_email
from email_service import send_email

app = Flask(__name__)

client = MongoClient("mongodb://admin:password@localhost:27017")

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
    send_email("buketvarilci@gmail.com", user_email, "halllloo", "I am the body")
    save_email(client, user_email)
    print(f"NEW SUBSCRIBER!!! Email: {user_email}")
    return f"<h1> Success!</h1><p>Thanks {user_email}has been added. </p><a href='/butet'>Go back</a>"

if __name__ == "__main__":
    app.run(debug=True)