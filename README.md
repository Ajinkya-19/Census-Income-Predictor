
# Census Income Predictor

### Link = https://modular-coding-ml-project.onrender.com


 **Predict whether a person earns more or less than $50,000 per year using Census Data.**

---

## 📌 Project Overview

This project is a **classification problem** that predicts whether an individual earns more or less than **$50,000 per annum** based on various social-economic and demographic features. The model is trained using the **Adult Income Census dataset** and deployed with **Docker and CI/CD on Render Cloud Platform**.

- **End-to-End Machine Learning Pipeline** – Includes **data ingestion, validation, transformation, model training, and prediction**
- **Fully Automated CI/CD** – GitHub Actions ensures automatic pipeline execution on any updates
- **Cloud Deployment** – Docker containerized model deployed on **Render Cloud**

---

![Model Training Accuracy](images/model_accuracy.png)


## 🚀 Tech Stack

- **Programming Language:** Python  
- **Machine Learning Frameworks:** Scikit-Learn  
- **Model Used:** Random Forest Classifier (Best Fit)  
- **Data Processing:** Pandas, NumPy, Seaborn  
- **Web Framework:** Flask (API Deployment)  
- **Containerization:** Docker  
- **CI/CD Pipeline:** GitHub Actions  
- **Cloud Deployment:** Render  

---


## 📂 Project Structure

```
📁 Income_Prediction_Project
│── 📂 data                  # Dataset files
│── 📂 notebooks 
            # Jupyter Notebooks for EDA & training
│── 📂 src
│   ├── data_ingestion.py    # Fetch and preprocess dataset
│   ├── data_validation.py   # Validate dataset
│   ├── data_transformation.py # Transform categorical and numerical features
│   ├── model_training.py    # Train ML models (Decision Tree, RF, Logistic Regression)
│   ├── model_evaluation.py  # Evaluate and compare models
│   ├── prediction.py        # API endpoint for making predictions
│── 📂 docker                # Dockerfile & image configurations
│── 📂 cicd_pipeline         # GitHub Actions CI/CD workflow
│── README.md                # Project Documentation
```

---

## 🛠 Setup & Installation

### 1️⃣ Clone the Repository

```sh
git clone https://github.com/Ajinkya-19/Income_Prediction.git
cd Income_Prediction
```

### 2️⃣ Install Dependencies

```sh
pip install -r requirements.txt
```

### 3️⃣ Run the Flask App

```sh
python app.py
```

The application will be available at **http://localhost:5000**.

---

## 📊 Dataset Details

The model is trained on the **Adult Income Census dataset**, which contains **14 features**:

```yaml
['age', 'workclass', 'fnlwgt', 'education', 'education-num', 'marital-status', 'occupation',
 'relationship', 'race', 'sex', 'capital-gain', 'capital-loss', 'hours-per-week', 'country', 'salary']
```

📌 **Target Variable:** `salary` (`<=50K` or `>50K`)

---
![Model Training Accuracy](images/model_accuracy.png)


## 🤖 Model Training & Performance

Three models were trained:

- ✅ **Decision Tree**
- ✅ **Random Forest (Best Performing)**
- ✅ **Logistic Regression**

🎯 **Best Model:** `Random Forest Classifier`  

---

## 🎯 Key Features

✅ **User Input-Based Prediction** – Takes inputs like **age, workclass, education, occupation, marital status**, etc., and predicts salary class.  
✅ **Automated ML Pipeline** – Fully automated **data ingestion → model training → deployment**.  
✅ **CI/CD Integration** – Automated build, test, and deployment using **GitHub Actions**.  
✅ **Containerized Deployment** – Runs in an isolated **Docker container** and deployed on **Render Cloud**.  

![Model Training Accuracy](images/model_accuracy.png)

---

## 🐳 Docker Deployment

### 1️⃣ Build Docker Image

```sh
docker build -t income-prediction .
```

### 2️⃣ Run Docker Container

```sh
docker run -p 5000:5000 income-prediction
```

### 3️⃣ Push Docker Image to Docker Hub

```sh
docker tag income-prediction ajinkya19/income-prediction
docker push your-ajinkya19/income-prediction
```

---

## 🚀 CI/CD & Cloud Deployment

This project follows **continuous integration & deployment (CI/CD)** with **GitHub Actions**:

1. **GitHub Actions** – Triggers automated training & testing when new code is pushed.  
2. **Docker** – The model is containerized and pushed to **Docker Hub**.  
3. **Render Cloud** – The model is deployed in production on **Render Cloud Platform**.  

🖼 **_Add CI/CD workflow diagram or logs screenshot here._**  

---

## 🔥 Future Enhancements

- 🚀 Add a **frontend UI** for better user experience  
- 🚀 Deploy on **AWS/GCP using Kubernetes** for scalability  

---

## 🤝 Contributing

Feel free to fork the repo, raise issues, or submit pull requests!  

📧 Contact: ajinkyac7498@gmail.com  

⭐ If you like this project, consider giving it a **star** on GitHub! ⭐  

---

