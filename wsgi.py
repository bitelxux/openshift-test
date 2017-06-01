from flask import Flask
import socket

application = Flask(__name__)

@application.route("/")
def hello():
    return "Hello World!"

@application.route("/hostname")
def test():
    return "Yipee !! this host is %s" % socket.gethostname()

@application.route("/load")
def test():
    html = socket.gethostname()
    for i in 5000:
      html += "\n<BR>%d" % i

    return html

if __name__ == "__main__":
    application.run()
