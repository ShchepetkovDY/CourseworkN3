from flask import Flask, send_from_directory
from main.views import main_blueprint
from bookmarks.views import bookmarks_blueprint
from api.api import api_blueprint

POST_PATH = 'data/posts.json'
UPLOAD_FOLDER = 'uploads/images'

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

# регистрация блупринтов
app.register_blueprint(main_blueprint)
app.register_blueprint(bookmarks_blueprint)
app.register_blueprint(api_blueprint)


@app.errorhandler(404)
def page_404(error):
    return "404 NOT FOUND"


@app.errorhandler(500)
def page_500(error):
    return "500 Internal Server Error"


if __name__ == '__main__':
    app.run()
