import json

from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['POST'])
def upload_screenshot():
    # screenshot_data = request.json.get('screenshot')

    # # Decode Base64-encoded screenshot data
    # import base64
    # screenshot_bytes = base64.b64decode(screenshot_data)

    # #Save screenshot to file (or perform further processing)
    # with open('screenshot.png', 'wb') as f:
    #     f.write(screenshot_bytes)

    
    # Get the screenshot data from the request
    screenshot_data = request.json.get('screenshot')

    # Decode Base64-encoded screenshot data
    screenshot_bytes = base64.b64decode(screenshot_data)

    # Save screenshot to file (or perform further processing)
    with open('screenshot.png', 'wb') as f:
        f.write(screenshot_bytes)

    # Encode the image data back to Base64
    encoded_image = base64.b64encode(screenshot_bytes).decode('utf-8')

    return json.dumps({
        'message': 'Screenshot received successfully',
        'image_data': encoded_image
    },indent=4)

if __name__ == '__main__':
    app.run(debug=True)

