# Loan_Approval_Prediction
🏦 Loan Approval Prediction
This project is a machine learning application that predicts whether a loan application will be approved or not, based on applicant details such as income, education, credit history, and property area.

The model is trained on the Loan Prediction Dataset from Kaggle, preprocessed, and then deployed as a Streamlit web app for interactive usage.

📊 Dataset
Source: [Kaggle - Loan Prediction Dataset] (commonly publicly available dataset)

Contains applicant details such as:

Gender, Marital Status, Dependents

Education, Self-Employed status

Applicant and Co-applicant Income

Loan Amount & Loan Term

Credit History & Property Area

Loan Status (Approved / Not Approved ✅❌)

⚙️ Project Workflow
Data Preprocessing & Cleaning

Removed rows with missing/null values

Applied label encoding to categorical features (e.g., Gender, Married, Education, Property Area)

Applied log transformation for skewed numerical features (ApplicantIncome, LoanAmount, Loan_Amount_Term, etc.)

Created new features such as Total Income log

Model Training

Trained a classification model to predict Loan_Status (Y/N)

Saved the trained model as loan_approval_model.pkl using Joblib

Deployment with Streamlit

Built a user-friendly web app (app.py)

User enters details (income, education, loan amount, etc.)

The model predicts:

✅ Loan Approved

❌ Loan Not Approved

🛠️ Tech Stack
Python

Pandas / NumPy – Data Cleaning & Processing

Scikit-learn – Machine Learning Model

Joblib – Model Serialization

Streamlit – Web Application Deployment
