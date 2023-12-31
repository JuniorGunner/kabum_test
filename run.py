from flask import Flask
from blueprints.quote import quote_blueprint


def create_app():
    """
    Cria e configura uma instância do aplicativo Flask.

    Retorna:
        app: Instância do aplicativo Flask.
    """
    app = Flask(__name__)
    app.register_blueprint(quote_blueprint, url_prefix='/api') # TODO: update with blueprint
    return app


if __name__ == "__main__":
    app = create_app()
    app.run(host='0.0.0.0', debug=True)
