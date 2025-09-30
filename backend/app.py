# backend/app.py

from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from predict import predict_breed 

app = Flask(__name__)
CORS(app)  # allow requests from frontend

# Upload folder
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(BASE_DIR, "uploads")
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

@app.route("/predict", methods=["POST"])
def predict():
    if "file" not in request.files:
        return jsonify({"error": "No file in request"}), 400

    image_file = request.files["file"]
    if image_file.filename == "":
        return jsonify({"error": "Empty filename"}), 400

    # Save temporarily
    image_path = os.path.join(app.config["UPLOAD_FOLDER"], image_file.filename)
    image_file.save(image_path)

    try:
        # Get actual prediction from PyTorch model
        result = predict_breed(image_path)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        # Delete uploaded file
        try:
            os.remove(image_path)
        except Exception as e:
            print(f"Warning: could not delete image: {e}")

    return jsonify(result), 200

@app.route("/health", methods=["GET"])
def health_check():
    return jsonify({"status": "ok"}), 200

@app.route("/", methods=["GET"])
def home():
    return "<h2>Cattle & Buffalo Breed Recognition API is running!</h2>"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)










# from flask import Flask, request, jsonify
# from flask_cors import CORS
# import os
# from predict import predict_breed  # dynamic PyTorch prediction

# app = Flask(__name__)
# CORS(app)  # allow requests from React frontend

# # Upload folder (temporary storage)
# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# UPLOAD_FOLDER = os.path.join(BASE_DIR, "uploads")
# os.makedirs(UPLOAD_FOLDER, exist_ok=True)
# app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# @app.route("/predict", methods=["POST"])
# def predict():
#     # Check if file is in request
#     if "file" not in request.files:
#         return jsonify({"error": "No file in request"}), 400

#     image_file = request.files["file"]
#     if image_file.filename == "":
#         return jsonify({"error": "Empty filename"}), 400

#     # Save temporarily
#     image_path = os.path.join(app.config["UPLOAD_FOLDER"], image_file.filename)
#     image_file.save(image_path)

#     # Predict using trained model
#     result = predict_breed(image_path)

#     # Delete uploaded file
#     try:
#         os.remove(image_path)
#     except Exception as e:
#         print(f"Warning: could not delete image: {e}")

#     return jsonify(result), 200

# @app.route("/health", methods=["GET"])
# def health_check():
#     return jsonify({"status": "ok"}), 200

# @app.route("/", methods=["GET"])
# def home():
#     return "<h1>Cattle & Buffalo Breed Recognition API</h1><p>Use /predict endpoint to POST an image</p>"

# if __name__ == "__main__":
#     # host="0.0.0.0" allows access from frontend
#     app.run(debug=True, host="0.0.0.0", port=5000)




# from flask import Flask, request, jsonify
# from flask_cors import CORS
# import os
# from predict import predict_breed  # model loads automatically on import

# # Flask app
# app = Flask(__name__)
# CORS(app)

# # Folder to save uploaded images temporarily
# UPLOAD_FOLDER = "uploads"
# os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# @app.route("/")
# def home():
#     return "Backend for Breed Recognition is running."

# @app.route("/predict", methods=["POST"])
# def predict():
#     if "file" not in request.files:
#         return jsonify({"error": "No file part in request"}), 400

#     file = request.files["file"]
#     if file.filename == "":
#         return jsonify({"error": "No file selected"}), 400

#     # Save the file temporarily
#     file_path = os.path.join(UPLOAD_FOLDER, file.filename)
#     file.save(file_path)

#     try:
#         # Predict breed
#         result = predict_breed(file_path)
#         # Remove temporary file
#         os.remove(file_path)
#         return jsonify(result)
#     except Exception as e:
#         print("Prediction error:", e)
#         return jsonify({"error": str(e)}), 500

# if __name__ == "__main__":
#     print("Starting Flask server...")
#     app.run(host="0.0.0.0", port=5000, debug=True)


# #updated one
# from flask import Flask, request, jsonify
# from flask_cors import CORS
# import os
# from predict import predict_breed
# from werkzeug.utils import secure_filename

# app = Flask(__name__)
# CORS(app)  # Allow cross-origin requests

# UPLOAD_FOLDER = "uploads"
# os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# @app.route('/predict', methods=['POST'])
# def predict():
#     if 'file' not in request.files:
#         return jsonify({"error": "No file uploaded"}), 400

#     file = request.files['file']
#     if file.filename == '':
#         return jsonify({"error": "No selected file"}), 400

#     filename = secure_filename(file.filename)
#     filepath = os.path.join(UPLOAD_FOLDER, filename)
#     file.save(filepath)

#     try:
#         result = predict_breed(filepath)
#         # Remove file after prediction
#         os.remove(filepath)
#         # Only send breed and confidence
#         return jsonify({
#             "breed": result['breed'],
#             "confidence": result['confidence']
#         })
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500

# if __name__ == "__main__":
#     app.run(debug=True)
