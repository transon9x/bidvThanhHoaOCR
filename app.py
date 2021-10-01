from flask import Flask
from flask import request
import json
from flask_cors import CORS
import socket
import data
import def_type

app = Flask(__name__)
CORS(app)
ip = socket.gethostbyname(socket.gethostname())


@app.route("/bidvOCR", methods=['POST'])
def get_OCR():
    images = json.loads(request.data)['index']
    data_return = {'index': []}
    for image in images:
        type_id = image['type']
        name_type = def_type.def_type[type_id]
        data.data[name_type]['type'] = type_id
        data.data[name_type]['id'] = image['id']
        data_return['index'].append(data.data[name_type])
    return data_return


if __name__ == '__main__':
    app.run(host=ip, debug=True, port=50)
