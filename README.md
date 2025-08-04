# Student Placement Prediction Using Logistic Regression

## 🧠 Overview
This project uses a Logistic Regression model to predict whether a student is likely to be placed based on their CGPA and IQ. The project walks through the entire machine learning pipeline from data preprocessing to model deployment.

---

## 📁 Dataset
- **Source**: Custom CSV with 100 student entries
- **Features**:
  - `cgpa` (Cumulative Grade Point Average)
  - `iq` (Intelligence Quotient)
- **Target**:
  - `placement` (0 = Not Placed, 1 = Placed)

---

## 🔧 Workflow
1. **Data Preprocessing** – Cleaning and selecting relevant features.
2. **Exploratory Data Analysis (EDA)** – Visualizing relationships between features.
3. **Train-Test Split** – 90% training, 10% testing.
4. **Feature Scaling** – Using `StandardScaler`.
5. **Model Training** – Logistic Regression.
6. **Model Evaluation** – Accuracy score.
7. **Decision Boundary Visualization** – With `mlxtend`.

---

## 📊 Results
- Model achieved high accuracy on unseen test data.
- Visualization shows clearly separated decision regions between placed and unplaced students.

---

## 🛠️ Tools & Libraries
- Python
- NumPy
- Pandas
- Scikit-learn
- Matplotlib
- Mlxtend
- Pickle

---

## 📦 How to Run

1. Clone this repository:
   ```bash
   git clone https://github.com/ShreyaSarma21/student-placement-prediction.git
   cd student-placement-prediction
