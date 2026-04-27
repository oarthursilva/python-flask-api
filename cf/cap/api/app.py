from apifairy import APIFairy
from cfenv import AppEnv
from flask import Flask, request, abort
from sap import xssec

from config import Config

apifairy = APIFairy()
env = AppEnv()


def create_app(config_class=Config):
    app = Flask(__name__)

    app.config.from_object(config_class)
    apifairy.init_app(app)

    # blueprints
    from controllers import apiController
    app.register_blueprint(apiController, url_prefix='/api')

    @app.before_request
    def before_request():
        uaa = env.get_service(name='py-uaa')

        if uaa is None:
            return

        if 'authorization' not in request.headers:
            abort(403)

        uaa_service = uaa.credentials
        access_token = request.headers.get('authorization')[7:]
        security_context = xssec.create_security_context(access_token, uaa_service)
        isAuthorized = security_context.check_scope('uaa.resource')

        if not isAuthorized:
            abort(403)

    @app.route('/')
    def index():
        return 'API'

    @app.after_request
    def after_request(res):
        request.get_data()
        return res

    return app
