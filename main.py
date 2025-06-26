import os
from src.preprocessing import preprocess_image
from src.segmentation import detect_iris_boundaries
from src.normalization import normalize_iris
from src.feature_extraction import extract_features
from src.matching import match_iris
from src.utils import load_image

# Replace with actual paths
img_path = 'CASIA-Iris-Image-Database-Sample.jpg'

image = load_image(img_path)
preprocessed = preprocess_image(image)
pupil, limbus = detect_iris_boundaries(image)

if pupil is not None and limbus is not None:
    normalized = normalize_iris(preprocessed, pupil, limbus)
    features = extract_features(normalized)

    # Simulate a small database
    database = {
        "user1": features  # Just as a placeholder
    }

    matched_name, score = match_iris(features, database)
    print(f"Matched: {matched_name}, Score: {score}")
else:
    print("Failed to detect iris boundaries.")
