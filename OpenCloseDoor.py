from datetime import datetime
from flask import Flask, request, render_template, jsonify
from flask_json import FlaskJSON, JsonError, json_response, as_json
from gpiozero import LED
from signal import pause

app = Flask(__name__)
FlaskJSON(app)


@app.route('/')
def output():
    return render_template('interface.html')

@app.route('/porta', methods=['POST'])
def porta():
    data = request.get_json(force=True)
    energy = data['status']
    LED(energy)
    return jsonify(data)

def LED(op):
    porta = LED(11)

    if op==1:
        porta.on()
    elif op==0:
        porta.off()

    pause()

if __name__ == '__main__':
    app.run()
