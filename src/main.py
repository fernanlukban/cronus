from event_service import event_service_page
from flask import Flask

app = Flask(__name__)
app.register_blueprint(event_service_page)

if __name__ == '__main__':
    app.run()