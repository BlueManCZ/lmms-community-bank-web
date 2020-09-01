from web import app

app.debug=True

from werkzeug.debug import DebuggedApplication
app.wsgi_app = DebuggedApplication(app.wsgi_app, True)

if __name__ == "__main__":
    app.run()
