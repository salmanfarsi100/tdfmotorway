from flask import Flask, request, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

from tdfmotorway.config import Config


db = SQLAlchemy()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    from tdfmotorway.numberplate.routes import numberplate
    from tdfmotorway.optimalframe.routes import camerabp
    from tdfmotorway.configurations.routes import configbp
    from tdfmotorway.speedmonitor.routes import speedbp

    @app.route("/", methods=["GET", "POST"])
    def home():
        if request.form:
            if request.form["submit_button"] == "Go to Configurations":
                return redirect(url_for('configbp.config'))
            if request.form["submit_button"] == "Go to Camera API":
                return redirect(url_for('camerabp.deepstream'))
            if request.form["submit_button"] == "Go to Camera Records":
                return redirect(url_for('camerabp.ofe_views'))
        return render_template("home.html")

    app.register_blueprint(numberplate)
    app.register_blueprint(camerabp, url_prefix="/camera")
    app.register_blueprint(configbp, url_prefix="/config")
    app.register_blueprint(speedbp, url_prefix="/speed")

    return app
