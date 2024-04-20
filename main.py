import json
from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['POST'])
def receive_json():
    # Log incoming request details
    print("Received request:")
    print("Method:", request.method)
    print("Headers:", request.headers)
    print("Body:", request.get_data(as_text=True))
    # Get the JSON data from the request
    data = request.json

    # Print the JSON data
    print("Received JSON:", data)

    # Extract the string from the JSON data
    received_string = data.get("text")

    # Perform any processing with the received string
    print("Received string:", received_string)

    # Return a JSON response indicating success
    response_data = {'message': 'String received successfully'}
    return json.dumps(response_data), 200


if __name__ == '__main__':
    app.run(debug=True)








#***************** this is correct one ***********************

# from flask import Flask, request, jsonify
# import base64
# import json
# from PIL import Image
# import io

# app = Flask(__name__)

# @app.route('/', methods=['POST'])
# def upload_screenshot():
#     # Get the screenshot data from the request
#     screenshot_data = request.json.get('screenshot')

#     # Decode Base64-encoded screenshot data
#     screenshot_bytes = base64.b64decode(screenshot_data)

#     # Convert bytes to image
#     img = Image.open(io.BytesIO(screenshot_bytes))

#     # Save screenshot as JPEG file (or perform further processing)
#     img.save('screenshot.jpg', format='JPEG')

#     # Encode the image data back to Base64 (optional)
#     encoded_image = base64.b64encode(screenshot_bytes).decode('utf-8')

#     # Prepare the JSON response with success message and image data (optional)
#     response_data = {
#         'message': 'Screenshot received successfully',
#         'image_data': encoded_image
#     }

#     # Return the JSON response (optional)
#     return jsonify(response_data)

# if __name__ == '__main__':
#     app.run(debug=True)













# import json
#
# from flask import Flask, request
#
# app = Flask(__name__)
#
# @app.route('/', methods=['POST'])
# def upload_screenshot():
#     screenshot_data = request.json.get('screenshot')
#
#     # Decode Base64-encoded screenshot data
#     import base64
#     screenshot_bytes = base64.b64decode(screenshot_data)
#
#     # Save screenshot to file (or perform further processing)
#     with open('screenshot.png', 'wb') as f:
#         f.write(screenshot_bytes)
#
#     return json.dumps({'key':'Screenshot received successfully'},indent=4)
#
# if __name__ == '__main__':
#     app.run(debug=True)


















# import base64
# import json
#
# from flask import Flask, request
#
# app = Flask(__name__)
#
#
# @app.route('/', methods=['POST'])
# def upload_screenshot():
#     # screenshot_data = request.json.get('screenshot')
#
#     # # Decode Base64-encoded screenshot data
#     # import base64
#     # screenshot_bytes = base64.b64decode(screenshot_data)
#
#     # #Save screenshot to file (or perform further processing)
#     # with open('screenshot.png', 'wb') as f:
#     #     f.write(screenshot_bytes)
#
#     # Get the screenshot data from the request
#     screenshot_data = request.json.get('screenshot')
#
#     # Decode Base64-encoded screenshot data
#     screenshot_bytes = base64.b64decode(screenshot_data)
#
#     # Save screenshot to file (or perform further processing)
#     with open('screenshot.png', 'wb') as f:
#         f.write(screenshot_bytes)
#
#     # Encode the image data back to Base64
#     encoded_image = base64.b64encode(screenshot_bytes).decode('utf-8')
#
#     return json.dumps({
#         'message': 'Screenshot received successfully',
#         'image_data': encoded_image
#     }, indent=4)
#
#
# if __name__ == '__main__':
#     app.run(debug=True)


# import base64
# import json

# from flask import Flask, request

# app = Flask(__name__)


# @app.route('/', methods=['POST'])
# def upload_screenshot():
#     # screenshot_data = request.json.get('screenshot')

#     # # Decode Base64-encoded screenshot data
#     # import base64
#     # screenshot_bytes = base64.b64decode(screenshot_data)

#     # #Save screenshot to file (or perform further processing)
#     # with open('screenshot.png', 'wb') as f:
#     #     f.write(screenshot_bytes)

#     # Get the screenshot data from the request
#     screenshot_data = request.json.get('screenshot')

#     # Decode Base64-encoded screenshot data
#     screenshot_bytes = base64.b64decode(screenshot_data)

#     # Save screenshot to file (or perform further processing)
#     with open('screenshot.png', 'wb') as f:
#         f.write(screenshot_bytes)

#     # Encode the image data back to Base64
#     encoded_image = base64.b64encode(screenshot_bytes).decode('utf-8')

#     return json.dumps({
#         'message': 'Screenshot received successfully',
#         'image_data': encoded_image
#     }, indent=4)


# if __name__ == '__main__':
#     app.run(debug=True)
