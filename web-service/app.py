# app.py
from flask import Flask, request, jsonify, send_file
from PIL import Image, ImageDraw
from io import BytesIO

app = Flask(__name__)


def sample_image():
    size = 5
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
    return serve_pil_image(sample_image())



if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)
