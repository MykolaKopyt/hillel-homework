from flask import Flask, request
from datetime import datetime
from random import choices

app = Flask(__name__)


@app.route('/whoami')
def whoami():
    return (f"<h1 align='center'>Client: {request.user_agent}</h1>"
            f"<h1 align='center'>IP address: {request.remote_addr}</h1>"
            f"<h1 align='center'>Server time: {datetime.now().strftime('%H:%M:%S')}</h1>")


@app.route('/source_code/')
def source_code():
    with open(__file__, 'r') as file:
        return f"<plaintext>{file.read()}"


@app.route('/random')
def random_string():
    length = int(request.values.get('length', 0))
    specials = int(request.values.get('specials', 0))
    digits = int(request.values.get('digits', 0))
    result = ""
    if length not in range(1, 101) or specials not in (0, 1) or digits not in (0, 1):
        result += f"<p>Length is not valid</p>" if length not in range(1, 101) else ""
        result += f"<p>Specials is not valid</p>" if specials not in (0, 1) else ""
        result += f"<p>Digits is not valid</p>" if digits not in (0, 1) else ""
    else:
        string = [chr(letter) for letter in list(range(65, 91)) + list(range(97, 123))]
        string += [chr(number) for number in list(range(48, 58))] if specials else ""
        string += [chr(number) for number in list(range(33, 48))] if digits else ""
        result = "".join(choices(string, k=length))
    return result
