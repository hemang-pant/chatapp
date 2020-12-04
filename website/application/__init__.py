from flask import Flask
from flask_ngrok import run_with_ngrok
#run_with_ngrok(app)  

def create_app():
    """Construct the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')
    

    with app.app_context():
       
        from .views import view
        from .filters import _slice
        from .database import DataBase

       
        app.register_blueprint(view, url_prefix="/")

      
        @app.context_processor
        def slice():
            return dict(slice=_slice)

        return app
