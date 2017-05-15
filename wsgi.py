from flask import Flask
import socket

application = Flask(__name__)

@application.route("/")
def hello():
    return "Hello World!"

@application.route("/hostname")
def test():
    return socket.gethostname()

if __name__ == "__main__":
    application.run()
