# 👁️ Iris Recognition System

An end-to-end **Iris Recognition System** built using classical image processing techniques. This system performs **image preprocessing, iris segmentation, pupil and limbus boundary detection, normalization, feature extraction**, and **feature matching** to identify individuals from iris images.

> 📌 Developed as part of a Machine Learning job assignment at **DevifyX**.

---

## 🚀 Features

- ✅ Image Preprocessing (grayscale, denoising, contrast enhancement)
- ✅ Iris Segmentation using Hough Circle Transform
- ✅ Pupil & Limbic Boundary Detection
- ✅ Iris Normalization (rubber sheet model)
- ✅ Feature Extraction (Laplacian sign-based encoding)
- ✅ Feature Matching using Hamming Distance
- ✅ Evaluation with Accuracy, Precision, Recall & F1 Score

---

## 🖼 Sample Flow

1. Raw Eye Image → Preprocessed
2. Iris + Pupil Detected → Normalized Iris Strip
3. Feature Extracted → Compared with Database

---

## 🛠️ Tech Stack

- **Language:** Python 3.7+
- **Libraries:** OpenCV, NumPy, scikit-image, scikit-learn, matplotlib

---

## 📁 Project Structure

ris_recognition_system/
├── data/ # Sample iris images
├── notebooks/
│ └── evaluate.ipynb # Evaluation metrics notebook
├── results/ # Output visualizations
├── src/ # Source modules
│ ├── preprocessing.py
│ ├── segmentation.py
│ ├── normalization.py
│ ├── feature_extraction.py
│ ├── matching.py
│ └── utils.py
├── main.py # Runs complete pipeline
├── requirements.txt # Python dependencies
└── README.md


---

## ⚙️ Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/iris_recognition_system.git
cd iris_recognition_system

### Install Dependencies
pip install -r requirements.txt

### Run the file
python main.py

### Evaluation
notebooks/evaluate.ipynb

### Example Output

✅ Iris boundaries correctly segmented
✅ Iris normalized to polar coordinates
✅ Matching result displayed with similarity score

###  ✔️ Sample result metrics:
Accuracy: 0.80
Precision: 0.83
Recall: 0.83
F1 Score: 0.80
