import os


from dotenv import load_dotenv


from flask import Flask, render_template


from webapp.footer_sections.routes import footers_bp

app = Flask(__name__)

app.register_blueprint(footers_bp)


load_dotenv()


BUSINESS_NAME = os.environ.get("BUSINESS_NAME")

social_media_infos = [
    {"name": "Telegram", "url": "/about/telegram", "icon": "telegram"},
    {"name": "Facebook", "url": "/about/facebook", "icon": "facebook"},
    {"name": "X (Twitter)", "url": "/about/twitter", "icon": "twitter-x"},
    {"name": "Instagram", "url": "/about/instagram", "icon": "instagram"},
    {"name": "YouTube", "url": "/about/youtube", "icon": "youtube"},
]


know_about_us_links = [
    {"name": "About Us", "url": "/about"},
    {"name": "Contact Us", "url": "/contact"},
    {"name": "Our Address", "url": "/about/address"},
    {"name": "Our Certificate", "url": "/about/certificate"},
    {"name": "Our Achievements", "url": "/about/achievements"},
    {"name": "FAQs", "url": "/faqs"},
]

help_section_links = [
    {"name": "Your Account", "url": "/account"},
    {"name": "Returns Centre", "url": "/about/returns"},
    {"name": "Help Section", "url": "/help"},
    {"name": "Recalls and Product Safety Alerts", "url": "/about/recalls"},
    {"name": "100% Purchase Protection", "url": "/about/protection"},
    {"name": "Download Our App", "url": "/app-download"},
    {"name": "Pricing Informations", "url": "/pricing"},
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
        know_about_us_links=know_about_us_links,
        help_section_links=help_section_links,
    )


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=8000,
        debug=True,
    )
