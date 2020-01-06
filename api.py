from flask import Flask, jsonify, request, send_file
import os
from random_string import RandomString

app = Flask(__name__)

obj_random_string = RandomString(20)
obj_random_string.generate_random_string()
image_name = obj_random_string.get_image_name()


@app.route("/api/generate", methods=["POST"])
def generate_text():
    text = request.form["text_from_user"]
    print(text)
    print(image_name)
    os.system(f'python generate.py --noinfo --text="{text}" --filename="{image_name}" --bias=1. --style=3')
    return jsonify({
        "text_from_user": text,
        "image_name": f'{image_name}.png'
    })

@app.route("/api/get_last", methods=["GET"])
def get_last():
    filename = f'imgs/{image_name}.png'
    return send_file(filename, mimetype='image/gif')

@app.route("/api/get/<filename>", methods=["GET"])
def get(filename):
    return send_file(f'imgs/{filename}', mimetype='image/gif')

app.run(host='localhost', port='3000')
