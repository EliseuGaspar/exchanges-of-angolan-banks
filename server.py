from src.app import app_io, app
from src.routes import *

if __name__ == '__main__':
    app_io.run(
        app=app,
        host='0.0.0.0',
        port=3500,
        debug=True
    )
