# 🌫️ Air Quality Index (AQI) Prediction Using Random Forest Regressor

## 🧠 Overview

This project aims to **predict the next day’s Air Quality Index (AQI)** using historical pollutant measurements.
The dataset contains hourly readings of pollutants such as **CO, NH₃, NO₂, O₃, PM10, PM2.5, and SO₂**, which are aggregated into daily averages for modeling.

A **Random Forest Regressor** is used to capture the nonlinear relationships between pollutant levels and AQI.
Features include both pollutant concentrations and temporal attributes such as **month** and **weekday**.

---

## 💡 Motivation

With **Diwali approaching**, I wanted to observe how AQI levels deviate during the festival period —
since air quality typically worsens significantly due to fireworks and increased emissions.

---

## 📊 Model Performance

### ✅ Pre-Festival (Seen Data)

Predictions before Diwali were highly accurate, as shown by standard regression metrics:

* **MAE**, **MSE**, and **R²** scores indicated solid performance,
  with **R² ≈ 0.86** on seen data.

**Score Results:**

<img width="298" height="81" alt="Model Score Screenshot" src="https://github.com/user-attachments/assets/c4de7b88-de2d-44d2-b7e2-90810b6fb992" />

**Predicted vs Actual Graph:**

<img width="597" height="440" alt="Predicted vs Actual Graph" src="https://github.com/user-attachments/assets/c0b63ca2-6bd1-42c9-a537-8eed5df1d09c" />

---

### ⚠️ Festival Period (Unseen Data)

Predictions during Diwali were **less consistent**, often off by **20–25 AQI points**.
This drop in performance occurred because **Diwali arrived earlier than usual**,
and the **month/weekday features couldn’t effectively capture** the sudden festival-related changes in emissions.

---
### 💢 Stress Test (Removing pervious day AQI feature)
In the feature importance graph we could see that **AQI** was the most important feature. Stress test was done to see models perfomance without this important data.

***With AQI Feature***

<img width="603" height="533" alt="image" src="https://github.com/user-attachments/assets/dfe0d644-761c-47f8-9cbd-9d02bb38a65e" />

---

***Without AQI Feature***

<img width="660" height="550" alt="image" src="https://github.com/user-attachments/assets/3304f206-96d7-4c7e-9804-df9f54338d33" />


## 🧩 Summary

* **Model:** Random Forest Regressor
* **Data:** Daily averages of major air pollutants
* **Goal:** Next-day AQI prediction
* **Result:** Strong general accuracy (R² ≈ 0.86) on seen data, reduced accuracy during unmodeled festival events
