# MLDiaries 04 — Exploring the Limits of Regression

This repository documents **MLDiaries 04**, a learning-first machine learning project where the goal was **not to chase high accuracy**, but to understand *how far regression models can realistically go* when predicting student performance — and where they naturally fall short.

This project focuses on **thinking like an ML practitioner**:
- diagnosing bias vs variance  
- interpreting models instead of worshipping scores  
- knowing when to **stop and reject a model**

---

## 🎯 Project Objectives

- Build a **leakage-free regression model** for student performance  
- Analyze **feature correlations and relationships**  
- Study **bias–variance behavior** using learning curves  
- Test whether **increasing complexity actually helps**  
- Build a **What-If Analyzer** for counterfactual reasoning  
- Practice **responsible model rejection**

---

## 📊 Dataset Overview

The dataset contains **academic, demographic, family, and lifestyle features**, including:

- Study time, failures, absences  
- Parental education and jobs  
- School and family support  
- Motivation indicators (e.g. intent for higher education)

### 🎯 Target Variable
- `G3` — Final grade

⚠️ **Important:**  
Early grades (`G1`, `G2`) were intentionally excluded to **avoid data leakage**.

---

## 🏗️ Modeling Pipeline

All experiments are built using a **scikit-learn Pipeline** to ensure:
- clean preprocessing
- reproducibility
- no leakage

### Pipeline Design
- **Numeric features**
  - `StandardScaler`
  - `PolynomialFeatures` (tested, later rejected)
- **Categorical features**
  - `OneHotEncoder`
- **Model**
  - Linear Regression (baseline)
  - Ridge Regression (stability analysis)

📌 **Pipeline architecture:**

![Pipeline Diagram](data.image/pipeline.png)

---

## 📈 Baseline Model Performance

The linear regression baseline produced:

- **MAE ≈ 3.4**
- **RMSE ≈ 4.2**
- **R² ≈ 0.14**

Learning curves showed **early convergence**, indicating:

- low variance  
- **high bias (underfitting)**  

📌 This was not a tuning issue — it was a **model capacity limitation**.

---

## 🔬 Polynomial Regression Experiment

To address underfitting, polynomial features were introduced.

### Result:
- MAE worsened to ≈ 4.1  
- RMSE increased to ≈ 5.0  
- **R² dropped to −0.22**

📌 Interpretation:
> Increasing complexity amplified noise instead of capturing signal.

The polynomial model was **deliberately rejected** — a key ML decision.

---

## 🔎 Feature Influence & Stability

Feature coefficients were analyzed and compared with **Ridge Regression** to test signal stability.

Key observations:
- Motivation for higher education → strong positive signal  
- Prior failures → strong negative signal  
- Support features appear negative due to **reactive patterns**  

📌 **Coefficient stability comparison:**

![Feature Coefficients](data/coefficients.png)

This step confirmed that the model’s insights were **stable, not accidental**.

---

## 🔁 What-If Analyzer (Counterfactual Reasoning)

Instead of only predicting, the model was used as a **simulation tool**.

> “What happens if one factor changes while everything else stays constant?”

### Example Scenarios

| Scenario | Predicted Grade |
|--------|-----------------|
| Baseline | 1.88 |
| +2 Study Time | 3.40 |
| −1 Failure | 3.74 |
| −5 Absences | 1.75 |

📌 **What-If results:**

![What-If Analyzer](data/scenarios.png)

### Insights:
- Preventing failures matters more than small effort increases  
- Motivation has stronger leverage than attendance alone  
- Not all features move the needle equally  

⚠️ These are **model-based insights**, not causal guarantees.

---

## 🧠 Key Learnings

- More complexity ≠ better learning  
- Learning curves can tell you **when to stop**  
- Rejecting a model is sometimes the *most correct outcome*  
- ML is about **judgment**, not just metrics  

> Sometimes the most honest model is the one that admits its limits.

---

