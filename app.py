import streamlit as st
import pandas as pd
import numpy as np
import joblib

# -----------------------------
# Load Models
# -----------------------------
@st.cache_resource
def load_models():
    clf = joblib.load(r"C:\Users\Windows\EMIPREDICT_AI\emi_eligibility_classifier.joblib")
    reg = joblib.load(r"C:\Users\Windows\EMIPREDICT_AI\max_emi_regressor.joblib")
    label_encoder = joblib.load(r"C:\Users\Windows\EMIPREDICT_AI\emi_eligibility_label_encoder.joblib")
    return clf, reg, label_encoder

clf, reg, label_encoder = load_models()

# -----------------------------
# Streamlit Configuration
# -----------------------------
st.set_page_config(
    page_title="💰 EMIPredict AI",
    layout="wide",
    page_icon="💡"
)

st.title("💰 EMIPredict AI")
st.markdown("### Intelligent Financial Risk Assessment Platform")

st.sidebar.header("Input Customer Financial Data")

# -----------------------------
# Sidebar Inputs
# -----------------------------
col1, col2 = st.sidebar.columns(2)

with col1:
    salary = st.number_input("Monthly Salary (INR)", min_value=1000.0, value=30000.0)
    credit_score = st.number_input("Credit Score", min_value=300, max_value=850, value=700)
    years_emp = st.number_input("Years of Employment", min_value=0.0, value=3.0)
    existing_emi = st.number_input("Current EMI Amount (INR)", min_value=0.0, value=0.0)
    requested_amount = st.number_input("Requested Loan Amount (INR)", min_value=10000.0, value=50000.0)

with col2:
    requested_tenure = st.slider("Requested Tenure (Months)", 3, 84, 12)
    employment_type = st.selectbox("Employment Type", ["Private", "Government", "Self-employed"])
    house_type = st.selectbox("House Type", ["Own", "Rented", "Family"])
    family_size = st.number_input("Family Size", min_value=1, value=3)
    dependents = st.number_input("Dependents", min_value=0, value=1)

# -----------------------------
# Create DataFrame for Prediction
# -----------------------------
input_data = pd.DataFrame([{
    "monthly_salary": salary,
    "credit_score": credit_score,
    "years_of_employment": years_emp,
    "current_emi_amount": existing_emi,
    "requested_amount": requested_amount,
    "requested_tenure": requested_tenure,
    "employment_type": employment_type,
    "house_type": house_type,
    "family_size": family_size,
    "dependents": dependents
}])

st.markdown("#### Input Summary")
st.dataframe(input_data)

# -----------------------------
# Add Missing Columns (for model compatibility)
# -----------------------------
expected_cols = [
    'age', 'gender', 'marital_status', 'education', 'monthly_salary', 'employment_type',
    'years_of_employment', 'company_type', 'house_type', 'monthly_rent', 'family_size',
    'dependents', 'school_fees', 'college_fees', 'travel_expenses', 'groceries_utilities',
    'other_monthly_expenses', 'existing_loans', 'current_emi_amount', 'credit_score',
    'bank_balance', 'emergency_fund', 'emi_scenario', 'requested_amount', 'requested_tenure',
    'total_expenses', 'debt_to_income', 'expense_to_income', 'savings_ratio',
    'affordability_ratio'
]

default_values = {
    'age': 30,
    'gender': 'Male',
    'marital_status': 'Single',
    'education': 'Graduate',
    'company_type': 'Private',
    'monthly_rent': 0,
    'school_fees': 0,
    'college_fees': 0,
    'travel_expenses': 0,
    'groceries_utilities': 0,
    'other_monthly_expenses': 0,
    'existing_loans': 0,  # ✅ FIXED: numeric to prevent string-to-float error
    'bank_balance': 10000,
    'emergency_fund': 5000,
    'emi_scenario': 'Personal Loan',
    'total_expenses': 0,
    'debt_to_income': 0,
    'expense_to_income': 0,
    'savings_ratio': 0,
    'affordability_ratio': 0
}

# Fill missing columns
for col in expected_cols:
    if col not in input_data.columns:
        input_data[col] = default_values.get(col, 0)

# Align with model training columns
if hasattr(clf, "feature_names_in_"):
    input_data = input_data.reindex(columns=clf.feature_names_in_, fill_value=0)

# ✅ Sanitize Data Types
# Convert "Yes"/"No" to numeric and enforce numeric dtype
if 'existing_loans' in input_data.columns:
    input_data['existing_loans'] = input_data['existing_loans'].replace({'Yes': 1, 'No': 0})
    input_data['existing_loans'] = pd.to_numeric(input_data['existing_loans'], errors='coerce').fillna(0)

# Convert everything possible to numeric (safety)
for col in input_data.columns:
    try:
        input_data[col] = pd.to_numeric(input_data[col])
    except Exception:
        pass

# -----------------------------
# Prediction Button
# -----------------------------
if st.button("🔍 Predict EMI Eligibility and Recommended EMI"):
    with st.spinner("Analyzing financial profile..."):
        # Classification Prediction
        pred_encoded = clf.predict(input_data)
        pred_label = label_encoder.inverse_transform(pred_encoded)[0]

        # Regression Prediction
        max_emi_pred = reg.predict(input_data)[0]

        # --- Business Rule Adjustment ---
        emi_min = 0.3 * salary
        emi_max = 0.5 * salary
        corrected_emi = max(emi_min, min(max_emi_pred, emi_max))

    # -----------------------------
    # Display Results
    # -----------------------------
    st.success(f"✅ **Predicted EMI Eligibility:** {pred_label}")
    st.info(f"💸 **Model-Predicted Maximum EMI:** ₹{max_emi_pred:,.2f}")
    st.info(f"📊 **Recommended EMI Range (30%-50% of salary): ₹{emi_min:,.2f} - ₹{emi_max:,.2f}**")
    st.success(f"💡 **Final Suggested EMI (Adjusted): ₹{corrected_emi:,.2f}**")

    # Dynamic Feedback
    if pred_label == "Eligible":
        st.success("This customer is financially strong for EMI approval ✅")
    elif pred_label == "High_Risk":
        st.warning("This customer may require additional verification ⚠️")
    else:
        st.error("This profile is **Not Eligible** for EMI at this time ❌")

# -----------------------------
# Footer
# -----------------------------
st.markdown("---")
st.caption("© 2025 EMIPredict AI | FinTech & Banking Risk Intelligence Platform")
