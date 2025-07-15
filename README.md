# Stroke Prediction 🚑

## Author: Mahmoud Mohamed Shatia 

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)  
![scikit-learn](https://img.shields.io/badge/scikit--learn-1.1%2B-orange)  
![License](https://img.shields.io/badge/License-MIT-green)  

A machine learning pipeline to predict the likelihood of a stroke using patient health data.

---

## 📌 Table of Contents
1. [Overview](#overview)  
2. [Features](#features)  
3. [Installation](#installation)  
4. [Usage](#usage)  
5. [Project Structure](#project-structure)  
6. [Contact](#contact)  

---

## 🔍 Overview

This project presents a complete end-to-end machine learning pipeline that leverages a real-world healthcare dataset from Kaggle, consisting of 5,110 patient records. The goal is to develop predictive models that can accurately classify whether a patient is at risk of experiencing a stroke based on a range of clinical and demographic features such as age, hypertension, heart disease history, average glucose level, and BMI.

The pipeline covers all essential stages of a data science workflow:

- **Exploratory Data Analysis** to understand feature distributions and correlations  
- **Preprocessing**: handling missing values & encoding categorical data  
- **Handling Class Imbalance** with resampling (SMOTE, oversampling, etc.)  
- **Model Training**: various classifiers such as Logistic Regression, Random Forest, XGBoost, etc.  
- **Evaluation** using metrics like precision, recall, F1-score, and confusion matrices  

The final outcome is a set of interpretable and scalable models that can assist in early detection of stroke risk, potentially helping healthcare professionals prioritize patient care.

---

## 🚀 Features

✅ Full end-to-end ML pipeline  
✅ Multiple models – Logistic Regression, Random Forest, XGBoost  
✅ Handles missing values & imbalanced data  
✅ Visualizations: correlation plots, confusion matrices  
✅ Modular notebooks for easy updates and experimentation  

---

## 🛠 Installation

1. *Clone the Repository*:
   bash
   git clone https://github.com/MahmoudShatia7/Stroke-Prediction.git
   cd Stroke-Prediction

2. *Install Dependencies*:
   bash
   pip install -r requirements.txt

---
## 📌 Usage
### 🔹 EDA Notebook:
      Perform Exploratory Data Analysis (EDA) — visualize distributions, check correlations, and identify missing data.


### 🔹 Evaluating the Model:
       Execute the core ML pipeline: data preprocessing, handling imbalances (e.g., SMOTE, oversampling), model training and evaluation with Logistic Regression, Random Forest, XGBoost, etc.

---

## 📁 Project Structure
Stroke‑Prediction/
├── healthcare-dataset-stroke-data.csv
├── last_trail.ipynb
├── Test The Model.ipynb
├── Stroke prediction Deploy.ipynb
├── requirements.txt
└── README.md  

---

## 🤝 Contributing
Contributions are welcome! To contribute:
1. *Fork the repository.*
2. *Create a new branch:*  
   bash
   git checkout -b feature/YourFeature
   
3. *Commit your changes:*  
   bash
   git commit -m "Add new feature"
   
4. *Push to the branch:*  
   bash
   git push origin feature/YourFeature
   
5. *Open a Pull Request.*

---

## 📧 Contact
For questions or feedback, feel free to reach out:
📩 *Email:* shatiamahmoud33@gamil.com  
🔗 *GitHub:* [Mahmoud Shatia](https://github.com/MahmoudShatia7) 

---

📌 *If you find this project helpful, don't forget to ⭐ the repository!* 🚀
