from flask import Blueprint, render_template


footers_bp = Blueprint(
    "footers",
    import_name=__name__,
    template_folder="templates",
)


@footers_bp.get("/about")
def about_section():
    return render_template("about.html")


@footers_bp.get("/features")
def features_section():
    """
    When Features Section of the website in the footer is pressed, this will execute
    """
    return render_template("features.html")


@footers_bp.get("/pricing")
def pricing_section():
    """
    When Pricing Section of the website in the footer is pressed, this will execute
    """
    return render_template("pricing.html")


@footers_bp.get("/faqs")
def faq_section():
    """
    When FAQ Section of the website in the footer is pressed, this will execute
    """
    return render_template("faq.html")


@footers_bp.get("/contact")
def contact_section():
    """
    When Contact Section of the website in the footer is pressed, this will execute
    """
    return render_template("contact.html")
