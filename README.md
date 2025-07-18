# 🏨 Hotel Reservation Prediction (MLOps)

This MLOps project predicts whether a hotel reservation will be **honored** or **canceled** using machine learning. It helps improve **revenue management** through smart overbooking decisions, **targeted marketing** for reliable customers, and potential **fraud detection**.

> ⚠️ _Note: This app was deployed on **Google Cloud Run**, with resources like GCP buckets, GCR images, and Cloud Run services—all of which have now been deleted to avoid billing. The app is not currently running online or locally._

---

## 🎯 Problem Statement

Hotels face frequent last-minute cancellations, leading to loss in revenue and poor resource allocation. This model predicts if a reservation will be canceled, enabling:
- ✅ Overbooking strategies if cancellation risk is high
- ✅ Focused marketing for customers likely to honor bookings
- ✅ Risk flags for potential misuse or fraud

---

## 🧠 ML Approach

- **Model Used:** LightGBM (tuned with RandomizedSearchCV)
- **Feature Selection:** RandomForest feature importance
- **Target Variable:** `booking_status` (0 = Canceled, 1 = Not Canceled)

### 🔢 Features Used

| Feature | Description |
|--------|-------------|
| `lead_time` | Days between booking & arrival |
| `avg_price_per_room` | Booking price per room |
| `arrival_month` / `arrival_date` | Stay timing |
| `market_segment_type` | Source of booking |
| `type_of_meal_plan` | Selected meal plan |
| `room_type_reserved` | Room category |
| `no_of_special_requests`, `repeated_guest`, `required_car_parking_space` | Behavioral features |
| _...plus several more_ |

---

## ⚙️ Tools & Technologies

| Category           | Tools Used                                      |
|--------------------|-------------------------------------------------|
| 🧠 ML               | Python, scikit-learn, LightGBM                  |
| 🌐 Web App          | Flask, HTML, Jinja2                             |
| 🔄 CI/CD            | Docker, Jenkins                                 |
| ☁️ Cloud Platform   | Google Cloud Platform (GCP)                     |
| 📦 Containerization | Docker Desktop, Google Container Registry (GCR)|
| 🚀 Deployment       | Google Cloud Run                                |
| 🧪 Tracking         | MLflow (experiment + model tracking)            |
| 📁 Storage          | Google Cloud Storage (buckets)                           |

---

## 🔁 MLOps Pipeline

A Upload CSV to GCP Bucket<br>
B Extract in VSCode using Service Account Key<br>
C Data Cleaning & Preprocessing<br>
 D RandomForest Feature Selection + Model selection<br>
 E Train LightGBM Model + MLflow Tracking <br>
 F  Flask App + Dockerize <br>
 G Jenkins CI/CD Pipeline<br>
 H Deploy via Cloud Run & GCR



---
🖥️ Web Application
Built with Flask + HTML + Jinja2

Takes 10 user input features

Shows:

Prediction (Canceled / Not Canceled)

Confidence Score (from predict_proba())
----

## 📹 Demo

A short video walkthrough (~2.4 mins) shows:
- Code flow
- MLOps integration
- App functionality
👉 [Watch the demo video on Google Drive](https://drive.google.com/file/d/1O0N-ljPudAXanFRtPmbCvv7U_XQLDviB/view?usp=sharing)
