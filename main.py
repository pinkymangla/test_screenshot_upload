from flask import Flask, request

app = Flask(__name__)

@app.route('/upload-screenshot', methods=['POST'])
def upload_screenshot():
    screenshot_data = request.json.get('screenshot')

    # Decode Base64-encoded screenshot data
    import base64
    screenshot_bytes = base64.b64decode(screenshot_data)

    # Save screenshot to file (or perform further processing)
    with open('screenshot.png', 'wb') as f:
        f.write(screenshot_bytes)

    return 'Screenshot received successfully'

if __name__ == '__main__':
    app.run(debug=True)