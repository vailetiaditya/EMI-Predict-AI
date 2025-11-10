

# 💰 EMIPredict AI

**EMIPredict AI** is an intelligent **financial risk assessment platform** that predicts a customer's **loan/EMI eligibility** and recommends the **maximum affordable EMI** using trained machine learning models.
It’s built using **Python, Streamlit, and scikit-learn**, making it a powerful yet simple web app for fintech or banking applications.

---

## 🚀 Features

* 🔍 Predicts **EMI Eligibility** (Eligible / Not Eligible)
* 💸 Estimates the **Maximum EMI Amount** a customer can afford
* 📊 Interactive **Streamlit** interface for instant prediction
* 🧠 Uses pre-trained **classification** and **regression** models
* ⚙️ Includes compatibility for latest **scikit-learn** versions
* 📈 Based on real-world financial parameters

---

## 🧩 Project Structure

```
📂 EMIPredict_AI
├── app.py                           # Main Streamlit web app
├── emi_prediction_dataset.csv        # Dataset used for model training
├── emi_eligibility_classifier.joblib # Trained classification model
├── max_emi_regressor.joblib          # Trained regression model
├── label_mapping.joblib              # Label encoder for eligibility
└── EMIPredict_AI_.ipynb              # Jupyter notebook for training
```

---

## ⚙️ Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/<your-username>/EMIPredict_AI.git
cd EMIPredict_AI
```

### 2️⃣ Create and activate a virtual environment

```bash
python -m venv venv
venv\Scripts\activate    # On Windows
source venv/bin/activate # On macOS/Linux
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

If you don’t have a `requirements.txt`, you can install manually:

```bash
pip install streamlit pandas numpy scikit-learn joblib
```

---

## ▶️ Run the Application

Start the Streamlit app:

```bash
streamlit run app.py
```

Then open the link shown in your terminal (usually `http://localhost:8501`).

---

## 🧠 How It Works

1. User inputs customer financial details:

   * Salary, credit score, employment info, dependents, etc.
2. The **classifier model** predicts **EMI eligibility**.
3. The **regressor model** predicts the **maximum EMI amount** the customer can handle.
4. The app displays:

   * ✅ Eligibility result
   * 💰 Predicted maximum EMI
   * 📊 Recommended EMI range (based on salary)

---

## 📊 Dataset Description

The dataset contains **404,800 financial records** with **27 features**, covering demographics, income, credit, and expenses.

| Column Name                                                                                       | Description                                                |
| ------------------------------------------------------------------------------------------------- | ---------------------------------------------------------- |
| `age`                                                                                             | Age of the customer                                        |
| `gender`                                                                                          | Gender (Male/Female)                                       |
| `marital_status`                                                                                  | Marital status (Single/Married)                            |
| `education`                                                                                       | Education level (Graduate, Professional, etc.)             |
| `monthly_salary`                                                                                  | Monthly income of the customer (INR)                       |
| `employment_type`                                                                                 | Type of employment (Private, Government, Self-employed)    |
| `years_of_employment`                                                                             | Number of years employed                                   |
| `company_type`                                                                                    | Organization type (Startup, MNC, etc.)                     |
| `house_type`                                                                                      | Residence status (Own, Rented, Family)                     |
| `monthly_rent`                                                                                    | Rent paid monthly (if applicable)                          |
| `family_size`                                                                                     | Number of family members                                   |
| `dependents`                                                                                      | Number of dependents                                       |
| `school_fees`, `college_fees`, `travel_expenses`, `groceries_utilities`, `other_monthly_expenses` | Monthly financial obligations                              |
| `existing_loans`                                                                                  | Whether the customer already has loans (Yes/No)            |
| `current_emi_amount`                                                                              | Total EMI amount currently being paid                      |
| `credit_score`                                                                                    | Credit score of the customer (300–850)                     |
| `bank_balance`                                                                                    | Current balance in the bank account                        |
| `emergency_fund`                                                                                  | Savings or funds available for emergencies                 |
| `emi_scenario`                                                                                    | Type of EMI requested (Education, Vehicle, Personal, etc.) |
| `requested_amount`                                                                                | Loan amount requested by the customer                      |
| `requested_tenure`                                                                                | Requested repayment tenure (in months)                     |
| `emi_eligibility`                                                                                 | Target label for classifier (Eligible / Not Eligible)      |
| `max_monthly_emi`                                                                                 | Target value for regressor (maximum EMI amount)            |

---

## 🧰 Technologies Used

| Category         | Tools/Frameworks     |
| ---------------- | -------------------- |
| Language         | Python               |
| Frontend         | Streamlit            |
| Machine Learning | scikit-learn, joblib |
| Data Handling    | pandas, numpy        |
| Visualization    | Streamlit UI         |
| Notebook         | Jupyter (.ipynb)     |

---

## 📸 App Preview

**Homepage:**
Displays financial input form and prediction results in real-time.

**Outputs:**

* ✅ EMI Eligibility
* 💸 Model-Predicted Maximum EMI
* 📊 Recommended EMI Range
* 💡 Adjusted EMI Suggestion

---


