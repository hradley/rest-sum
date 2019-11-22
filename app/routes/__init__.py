from app.routes import total


def init_app(app):
    app.register_blueprint(total.total_bp)
