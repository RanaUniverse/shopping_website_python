import os


from dotenv import load_dotenv


from flask import Flask, render_template


app = Flask(__name__)

load_dotenv()


BUSINESS_NAME = os.environ.get("BUSINESS_NAME")

social_media_infos = [
    {"name": "Telegram", "url": "/about/telegram", "icon": "telegram"},
    {"name": "Facebook", "url": "/about/facebook", "icon": "facebook"},
    {"name": "X (Twitter)", "url": "/about/twitter", "icon": "twitter-x"},
    {"name": "Instagram", "url": "/about/instagram", "icon": "instagram"},
    {"name": "YouTube", "url": "/about/youtube", "icon": "youtube"},
]


@app.route("/")
def home_page():
    return render_template(
        "index.html",
    )


@app.context_processor
def inject_global_variable():
    return dict(
        BUSINESS_NAME=BUSINESS_NAME,
        social_media_infos=social_media_infos,
    )


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=8000,
        debug=True,
    )
