from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "Hello World!"

@application.route("/test")
def test():
    return "UEOoooooooooo !! This is another URL !"

if __name__ == "__main__":
    application.run()
