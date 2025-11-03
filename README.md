## Part 1: Short Answer Questions (30 points)

### 1. Problem Definition (6 points)
**Hypothetical AI Problem:** Predicting student dropout risk in online courses.

**Objectives**
1. Identify at-risk students early to provide interventions.
2. Improve overall course completion rates.
3. Reduce institutional financial loss due to dropouts.

**Stakeholders**
- Teachers
- Students/Learners

**KPI**
- If the dropout prediction accuracy is ≥ **85%** the student is higly likely to dropout.

---

### 2. Data Collection & Preprocessing (8 points)

**Data Sources**
1. LMS activity logs i.e login frequency, assignment submissions etc.
2. Student & academic records database.

**Potential Bias**
- Students with poor internet access may appear disengaged and incorrectly be labeled as high dropout risk.

**Preprocessing Steps**
1. Handle missing values i.e missing grades.
2. Normalize numeric features i.e, number of logins.
3. Convert categorical variables to numerical format i.e gender.

---

### 3. Model Development (8 points)
**Chosen Model:** Random Forest. 

**Reason:** Works well with mixed data types, provides feature importance, robust to noise.

**Data Split Strategy:**  
- 70% training  
- 30% validation 

**Hyperparameters to Tune**
1. `n_estimators` – controls number of trees, affects performance and overfitting
2. `max_depth` – limits tree depth to avoid overfitting

---

### 4. Evaluation & Deployment (8 points)
**Evaluation Metrics**
- **Precision:** Avoids wrongly labeling students as at-risk  
- **Recall:** Ensures at-risk students are identified.
  
**Concept Drift** is a change in the relationship between the features & the labels.
- **Monitor** it by Track model accuracy each semester and retrain if performance is poor.
- 
**Deployment Challenge**
- Scaling the model to support predictions for thousands of students in real time.

---

## Part 2: Case Study Application (40 points)

### 1. Problem Scope (5 points)
**Problem:** Predict whether a patient will be readmitted within 30 days of hospital discharge.  

**Objectives:** 
- Reduce avoidable readmissions
- Improve patient care
- Lower hospital costs.
  
**Stakeholders:** Doctors, nurses, patients.

---

### 2. Data Strategy (10 points)

**Data Sources**
- Electronic Health Records (EHRs)
- Patient demographics i.e age
- Medication & discharge summary records
  
**Ethical Concerns**
1. Patient privacy & sensitive data handling.
2. Model bias against age, gender, or income groups.

**Preprocessing Pipeline**
1. Remove personal identifiers i.e HIPAA compliance
2. Assign missing lab values to Null
3. Feature engineering i.e past 6-month admission count
4. One-hot encode diagnosis codes
5. Standardize numeric fields i.e blood pressure, length of stay

---

### 3. Model Development (10 points)
**Chosen Model:** XGBoost (Gradient Boosting)  
**Reason:** Excellent for structured medical datasets, handles nonlinear relationships.

**Hypothetical Confusion Matrix**

|                       | Predicted Readmit | Predicted No Readmit |
|-----------------------|-------------------|----------------------|
| **Actual Readmit**    | 80 (TP)           | 20 (FN)              |
| **Actual No Readmit** | 30 (FP)           | 170 (TN)             |

**Precision** = 80 / (80 + 30) = **0.727**  
**Recall** = 80 / (80 + 20) = **0.80**

---

### 4. Deployment (10 points)
**Integration Steps**
1. Deploy model as API connected to hospital EHR
2. Run prediction automatically at discharge
3. Display risk score to doctors in dashboard
4. Log predictions for auditing & retraining
5. Set alerts for high-risk patients

**Regulatory Compliance**
- Encrypt stored & transmitted data  
- Follow HIPAA or local medical data laws  

---

### 5. Optimization (5 points)
**Overfitting Reduction Strategy:**  
- Reduce tree depth in XGBoost.

---

## Part 3: Critical Thinking (20 points)

### Ethics & Bias (10 points)
**Impact of Data Bias**
- If historical data under-treated certain groups, the model may predict them as higher risk, leading to unequal care.
  
**Mitigation**
- Perform fairness testing.
  
---

### Trade-offs (10 points)

**Interpretability vs Accuracy**
The trade-off is using a model that provides high enough accuracy to be clinically useful while still being interpretable enough for doctors to understand and trust its decisions. 
Instead of extreme options like black-box deep learning or overly simple models, hospitals often choose explainable models like XGBoost with SHAP to balance both needs.

**Limited Hospital Compute Resources**
- Lightweight models are chosen i.e Random Forest or Logistic Regression
- Use Batch predictions instead of real-time if it's needed

---

## Part 4: Reflection & Workflow Diagram (10 points)

### Reflection (5 points)
Most challenging step was designing an ethical, privacy-compliant pipeline because of medical regulations.  
Improve with time-series device data i.e wearables.

---

### Workflow Diagram using CRISP-DM framework (5 points)
Business understanding
        ↓
Data understanding
        ↓
Data preprocessing
        ↓
Modelling
        ↓
Evaluation
        ↓
Deployment

