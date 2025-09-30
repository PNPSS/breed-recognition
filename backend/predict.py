# # backend/predict.py
# import torch
# from torchvision import transforms, models
# from PIL import Image
# import os

# DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")
# MODEL_PATH = os.path.join("models", "breed_model.pth")
# CLASSES = ['gir', 'ongole', 'redsindhi', 'sahiwal','kankrej']

# # Load model
# model = models.resnet18(weights=None)  # Don't load ImageNet weights
# model.fc = torch.nn.Linear(model.fc.in_features, len(CLASSES))
# model.load_state_dict(torch.load(MODEL_PATH, map_location=DEVICE))
# model.to(DEVICE)
# model.eval()

# # Transform for input images
# transform = transforms.Compose([
#     transforms.Resize((224, 224)),
#     transforms.ToTensor(),
#     transforms.Normalize([0.485, 0.456, 0.406],
#                          [0.229, 0.224, 0.225])
# ])

# def predict_breed(image_path):
#     image = Image.open(image_path).convert("RGB")
#     img_tensor = transform(image).unsqueeze(0).to(DEVICE)

#     with torch.no_grad():
#         outputs = model(img_tensor)
#         probs = torch.nn.functional.softmax(outputs, dim=1)
#         conf, pred = torch.max(probs, 1)

#     return {"breed": CLASSES[pred.item()], "confidence": conf.item()}








# import torch
# from torchvision import models, transforms
# from PIL import Image
# import os

# # Device
# DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# # Number of classes (update if you add/remove breeds)
# NUM_CLASSES = 5

# # Load model architecture
# model = models.resnet18(weights=None)
# model.fc = torch.nn.Linear(model.fc.in_features, NUM_CLASSES)

# # Load trained weights
# MODEL_PATH = "models/breed_model.pth"
# state_dict = torch.load(MODEL_PATH, map_location=DEVICE)
# model.load_state_dict(state_dict)
# model.to(DEVICE)
# model.eval()

# # Image transform (same as training)
# IMG_SIZE = 224
# transform = transforms.Compose([
#     transforms.Resize((IMG_SIZE, IMG_SIZE)),
#     transforms.ToTensor(),
#     transforms.Normalize([0.485, 0.456, 0.406],
#                          [0.229, 0.224, 0.225])
# ])

# def predict_breed(image_path):
#     # Load image
#     image = Image.open(image_path).convert("RGB")
    
#     # Transform to tensor
#     image_tensor = transform(image).unsqueeze(0).to(DEVICE)  # add batch dim

#     # Predict
#     with torch.no_grad():
#         outputs = model(image_tensor)
#         probs = torch.softmax(outputs, dim=1)
#         conf, pred = torch.max(probs, dim=1)

#     # Map index to class
#     class_names = ['gir', 'ongole', 'redsindhi', 'sahiwal', 'kankrej']  # update your breeds
#     return {"breed": class_names[pred.item()], "confidence": float(conf)}


# #updated 
# import torch
# from torchvision import models, transforms
# from PIL import Image
# import os

# # Device
# DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# # Path to the trained model
# MODEL_PATH = "models/breed_model.pth"

# # Image transformations
# IMG_SIZE = 224
# transform = transforms.Compose([
#     transforms.Resize((IMG_SIZE, IMG_SIZE)),
#     transforms.ToTensor(),
#     transforms.Normalize([0.485, 0.456, 0.406],
#                          [0.229, 0.224, 0.225])
# ])

# # Load model
# print("Loading model...")
# model = models.resnet18(weights=None)
# NUM_CLASSES = 5
# model.fc = torch.nn.Linear(model.fc.in_features, NUM_CLASSES)
# model.load_state_dict(torch.load(MODEL_PATH, map_location=DEVICE))
# model = model.to(DEVICE)
# model.eval()
# print(f"Model loaded with {NUM_CLASSES} classes.")

# # Class names
# CLASSES = ['gir', 'kankrej', 'ongole', 'redsindhi', 'sahiwal']

# # Breed info
# BREED_INFO = {
#     "gir": {
#         "Origin": "Gujarat, India",
#         "Characteristics": "Heat tolerant, good milk producer",
#         "Average Milk Yield": "6-8 liters/day",
#         "Color": "Light to dark red with white patches"
#     },
#     "sahiwal": {
#         "Origin": "Punjab, Pakistan/India",
#         "Characteristics": "High milk yield, disease resistant",
#         "Average Milk Yield": "8-12 liters/day",
#         "Color": "Light to dark brown"
#     },
#     "tharparkar": {
#         "Origin": "Rajasthan, India",
#         "Characteristics": "Dual purpose, drought resistant",
#         "Average Milk Yield": "4-6 liters/day",
#         "Color": "White to light gray"
#     },
#     "ongole": {
#         "Origin": "Andhra Pradesh, India",
#         "Characteristics": "Large size, good for draft work",
#         "Average Milk Yield": "3-5 liters/day",
#         "Color": "White with gray markings"
#     },
#     "kankrej": {
#         "Origin": "Rajasthan/Gujarat, India",
#         "Characteristics": "Good draft and milk breed",
#         "Average Milk Yield": "5-7 liters/day",
#         "Color": "Grayish-white with darker markings"
#     },
#     "redsindhi": {
#         "Origin": "Sindh region",
#         "Characteristics": "High milk yield, heat resistant",
#         "Average Milk Yield": "7-10 liters/day",
#         "Color": "Reddish-brown"
#     }
# }

# def predict_breed(image_path):
#     if not os.path.exists(image_path):
#         raise FileNotFoundError(f"Image not found: {image_path}")

#     image = Image.open(image_path).convert("RGB")
#     image_tensor = transform(image).unsqueeze(0).to(DEVICE)

#     with torch.no_grad():
#         outputs = model(image_tensor)
#         probs = torch.softmax(outputs, dim=1)
#         confidence, pred_class = torch.max(probs, 1)
#         breed_name = CLASSES[pred_class.item()]

#     return {
#         "breed": breed_name,
#         "confidence": float(confidence),
#         "details": BREED_INFO.get(breed_name, {})
#     }


# import torch
# from torchvision import models, transforms
# from PIL import Image
# import os

# # Device
# DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# # Path to the trained model
# MODEL_PATH = "models/breed_model.pth"

# # Image transformations
# IMG_SIZE = 224
# transform = transforms.Compose([
#     transforms.Resize((IMG_SIZE, IMG_SIZE)),
#     transforms.ToTensor(),
#     transforms.Normalize([0.485, 0.456, 0.406],
#                          [0.229, 0.224, 0.225])
# ])

# # Load model
# print("Loading model...")
# model = models.resnet18(weights=None)
# NUM_CLASSES = 5
# model.fc = torch.nn.Linear(model.fc.in_features, NUM_CLASSES)
# model.load_state_dict(torch.load(MODEL_PATH, map_location=DEVICE))
# model = model.to(DEVICE)
# model.eval()
# print(f"Model loaded with {NUM_CLASSES} classes.")

# # Class names
# CLASSES = ['gir', 'kankrej', 'ongole', 'redsindhi', 'sahiwal']

# # Breed info
# BREED_INFO = {
#     "gir": {"Origin": "Gujarat, India", "Characteristics": "Heat tolerant, good milk producer", "Average Milk Yield": "6-8 liters/day", "Color": "Light to dark red with white patches"},
#     "sahiwal": {"Origin": "Punjab, Pakistan/India", "Characteristics": "High milk yield, disease resistant", "Average Milk Yield": "8-12 liters/day", "Color": "Light to dark brown"},
#     #"tharparkar": {"Origin": "Rajasthan, India", "Characteristics": "Dual purpose, drought resistant", "Average Milk Yield": "4-6 liters/day", "Color": "White to light gray"},
#     "ongole": {"Origin": "Andhra Pradesh, India", "Characteristics": "Large size, good for draft work", "Average Milk Yield": "3-5 liters/day", "Color": "White with gray markings"},
#     "kankrej": {"Origin": "Rajasthan/Gujarat, India", "Characteristics": "Good draft and milk breed", "Average Milk Yield": "5-7 liters/day", "Color": "Grayish-white with darker markings"},
#     "redsindhi": {"Origin": "Sindh region", "Characteristics": "High milk yield, heat resistant", "Average Milk Yield": "7-10 liters/day", "Color": "Reddish-brown"}
# }

# def predict_breed(image_path):
#     if not os.path.exists(image_path):
#         raise FileNotFoundError(f"Image not found: {image_path}")

#     image = Image.open(image_path).convert("RGB")
#     image_tensor = transform(image).unsqueeze(0).to(DEVICE)

#     with torch.no_grad():
#         outputs = model(image_tensor)
#         probs = torch.softmax(outputs, dim=1)
#         confidence, pred_class = torch.max(probs, 1)
#         breed_name = CLASSES[pred_class.item()]

#     # Convert confidence to percentage
#     confidence_percent = round(float(confidence) * 100, 2)

#     return {
#         "breed": breed_name,
#         "confidence": confidence_percent,
#         "details": BREED_INFO.get(breed_name, {})
#     }


# reupdated

import torch
from torchvision import models, transforms
from PIL import Image
import os

# Device
DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Path to the trained model
MODEL_PATH = "models/breed_model.pth"

# Image transformations
IMG_SIZE = 224
transform = transforms.Compose([
    transforms.Resize((IMG_SIZE, IMG_SIZE)),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406],
                         [0.229, 0.224, 0.225])
])

# Load model
print("Loading model...")
model = models.resnet18(weights=None)
NUM_CLASSES = 6
model.fc = torch.nn.Linear(model.fc.in_features, NUM_CLASSES)
model.load_state_dict(torch.load(MODEL_PATH, map_location=DEVICE))
model = model.to(DEVICE)
model.eval()
print(f"Model loaded with {NUM_CLASSES} classes.")

# Class names
CLASSES = ['gir', 'kankrej','murrah', 'ongole', 'redsindhi', 'sahiwal']

def predict_breed(image_path):
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Image not found: {image_path}")

    image = Image.open(image_path).convert("RGB")
    image_tensor = transform(image).unsqueeze(0).to(DEVICE)

    with torch.no_grad():
        outputs = model(image_tensor)
        probs = torch.softmax(outputs, dim=1)
        confidence, pred_class = torch.max(probs, 1)
        breed_name = CLASSES[pred_class.item()]

    # Return only breed and confidence (percentage)
    confidence_threshold = 0.4 # 60%
    if confidence < confidence_threshold:
        return {"breed": "Unknown", "confidence": round(float(confidence)*100, 2)}
    else:
        return {
            "breed": breed_name,
            "confidence": round(float(confidence) * 100, 2)
            }
