# app.py
from flask import Flask, request, jsonify, send_file
from flask import request
from PIL import Image, ImageDraw
from io import BytesIO
import urllib.parse
import json

app = Flask(__name__)


def sample_image(size):
    #size = 5
    cell_size = 50
    divider_size = 5

    img_width = img_height = (size * cell_size
                              + (size+1) * divider_size)

    img = Image.new('RGB', (img_width, img_height), 
                    color = 'white')

    draw = ImageDraw.Draw(img)

    for i in range(size+1):
        for j in range(size+1):

            x1 = i * (cell_size + divider_size)
            x2 = x1 + (cell_size + divider_size)

            y1 = j * (cell_size + divider_size)
            y2 = y1 + divider_size

            draw.rectangle([x1, y1, x2, y2],
                           fill = 'black', width = 0)
            draw.rectangle([y1, x1, y2, x2], 
                           fill = 'black', width = 0)

    return img

def serve_pil_image(pil_img):
    img = BytesIO()
    pil_img.save(img, format='JPEG')
    img.seek(0)
    return send_file(img, mimetype='image/jpeg')

@app.route('/image', methods=['GET'])
def get_image():

    url_encoded = request.args.get('json')
    json_encoded = urllib.parse.unquote_plus(url_encoded)
    data = json.loads(json_encoded)

    print(data)

    return serve_pil_image(sample_image(data['size']))



if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)
