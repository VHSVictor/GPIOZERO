from datetime import datetime
from flask import Flask, request, render_template, jsonify
from flask_json import FlaskJSON, JsonError, json_response, as_json
from gpiozero import LED
from signal import pause
import sys

app = Flask(__name__)
FlaskJSON(app)

sts = 1
door = 0
@app.route('/')
def output():
    return render_template('interface.html')

@app.route('/porta', methods=['POST'])
def porta():
    data = request.get_json(force=True)
    energy = data['status']
    LED2(energy)
    return jsonify(data)

def LED2(op):
   global door
   if door == 0:
       door = LED(17)

   if op == 1:
       door.on()	
   elif op == 0:
       door.off()

   sys.stdout.flush()	
   pause()
   
if __name__ == '__main__':
    app.run()

