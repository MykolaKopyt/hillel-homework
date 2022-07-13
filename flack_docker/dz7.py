from flask import Flask, request, render_template
from datetime import datetime
from random import choices

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/whoami')
def whoami():
    user_agent = request.user_agent
    remote_address = request.remote_addr
    time = datetime.now().strftime('%H:%M:%S')
    return render_template('whoami.html', user_agent=user_agent, remote_address=remote_address, time=time)


@app.route('/source_code/')
def source_code():
    code = []
    with open(__file__, 'r') as file:
        file_line = file.readlines()
        for line in file_line:
            code.append(line)
        return render_template('source_code.html', data=code)


@app.route('/random', methods=['POST', 'GET'])
def random_string():
    if request.method == 'POST':
        length = request.form['length']
        specials = request.form['specials']
        digits = request.form['digits']
        string = [chr(letter) for letter in list(range(65, 91)) + list(range(97, 123))]
        string += [chr(sign) for sign in list(range(33, 48))] if int(specials) else ""
        string += [chr(number) for number in list(range(48, 58))] if int(digits) else ""
        result = "".join(choices(string, k=int(length)))
        return render_template('random.html', result=result)
    else:
        return render_template('random.html')


if __name__ == "__main__":
    app.run(debug=True)
