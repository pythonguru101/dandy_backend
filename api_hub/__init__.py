from flask import Flask


def settings_api_hub():
    api_init = Flask(__name__)
    api_init.config["DEBUG"] = True

    from .api_views import api_views

    api_init.register_blueprint(api_views, url_prefix="/")

    return api_init
