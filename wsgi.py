from flask import Flask
import socket
import time

application = Flask(__name__)

@application.route("/")
def hello():
    return "Hello World!"

@application.route("/hostname")
def hostname():
    return "Yipee !! this host is %s" % socket.gethostname()

@application.route("/stress")
def stress():
    t = time.time()
    while time.time() -t < 10:
        pass
    return "CPU consuming loop has been running for 10 seconds"

@application.route("/load")
def load():
    html = socket.gethostname()
    for i in 5000:
      html += "\n<BR>%d" % i

    return html

if __name__ == "__main__":
    application.run()
