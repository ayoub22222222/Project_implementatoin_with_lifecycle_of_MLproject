# 🔥 Fire Weather Index (FWI) Prediction

This project predicts the **Fire Weather Index (FWI)** using meteorological and environmental features.  
It covers the **full machine learning workflow**: data cleaning, exploratory data analysis (EDA), model training, hyperparameter tuning, model serialization (pickling), and deployment through a **Flask API with HTML templates** for user interaction.

---

## 📌 Project Structure

project/

│
├── data/ # Raw and cleaned datasets
├── notebooks/ # Jupyter notebooks for EDA and experiments
├── models/ # Saved ML models (pickle files)
├── templates/ # HTML templates (welcome, prediction form)

│ ├── welcome.html
│ ├── predict.html
│ └── home.html

├── app.py # Flask app (API + routes)
├── requirements.txt # Dependencies
└── README.md # Project documentation


---

## 🚀 Workflow

### 1. Data Cleaning
- Handled missing values (`dropna`, `fillna` strategies).
- Standardized column names.
- Removed duplicates and irrelevant features.
- Converted categorical variables into numerical form.

### 2. Exploratory Data Analysis (EDA)
- Visualized distributions of variables (Temperature, RH, Rain, etc.).
- Analyzed correlations between input features and FWI.
- Identified patterns and outliers using plots and statistical summaries.
- Checked class/region balance.

### 3. Feature Engineering
- Scaled features using **StandardScaler**.
- Created derived variables where useful.
- Encoded categorical variables (`Classes`, `Region`).

### 4. Model Training
- Tested different ML algorithms:
  - Linear Regression
  - Ridge Regression
  - Random Forest
- Used **cross-validation** and **hyperparameter tuning** to select the best model.

### 5. Model Saving (Pickling)
- Finalized model (`ridge_model.pkl`) was saved with `pickle`.
- Scaler (`standard_scaler.pkl`) also saved to ensure consistent preprocessing during predictions.

### 6. API Development (Flask)
- Created a **Flask app** (`app.py`) with:
  - `/` → Welcome page
  - `/predict` → Prediction form
  - `/predictdata` → Handles form submission, runs model, and displays result
- Integrated HTML templates:
  - `welcome.html` → Minimalist landing page
  - `predict.html` → Input form with 9 features
  - `home.html` → Displays prediction results

### 7. Deployment
- App can be deployed on:
  - **Localhost** (Flask server)
  - **Cloud/Hosting** platforms (Heroku, Render, Railway, or AWS EC2)

---

## 🛠️ Technologies Used
- **Python 3.9+**
- **Pandas / NumPy** → Data cleaning & preprocessing
- **Matplotlib / Seaborn** → EDA & visualization
- **Scikit-learn** → Model building, scaling, hyperparameter tuning
- **Flask** → API development
- **HTML + CSS (Jinja2 templates)** → Frontend
- **Pickle** → Model persistence

---

## 📂 Input Features
The model takes the following 9 inputs:
- 🌡️ `Temperature`
- 💧 `Relative Humidity (RH)`
- 🌬️ `Wind Speed (Ws)`
- 🌧️ `Rain`
- 🔥 `FFMC`
- 🌲 `DMC`
- ⚡ `ISI`
- 📊 `Classes` (0 or 1)
- 🌍 `Region` (0 or 1)

---

## ▶️ How to Run the Project

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/fwi-prediction.git
cd fwi-prediction

