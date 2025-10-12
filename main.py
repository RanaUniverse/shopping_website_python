import os


from dotenv import load_dotenv


from flask import Flask, render_template


app = Flask(__name__)

load_dotenv()

BUSINESS_NAME = os.environ.get("BUSINESS_NAME")


@app.route("/")
def home_page():
    return render_template(
        "index.html",
    )


@app.context_processor
def inject_global_variable():
    return dict(
        BUSINESS_NAME=BUSINESS_NAME,
    )


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=8000,
        debug=True,
    )
