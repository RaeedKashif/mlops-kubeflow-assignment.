# MLOps Assignment: MLflow Pipeline for Carlifornia Housing

## Project Overview
This project demonstrates a full MLOps workflow using MLflow, DVC, and GitHub Actions.  
The ML task is **predicting housing prices (Boston Housing dataset)** using a Random Forest regressor.  
The pipeline includes:

1. **Data extraction** from DVC remote storage  
2. **Preprocessing**: cleaning, scaling, train-test split  
3. **Model training** with Random Forest  
4. **Evaluation**: calculating MSE and R² metrics  
5. **Logging**: all artifacts and metrics logged in MLflow  

---

## Setup Instructions

### 1. Clone the repository
```
git https://github.com/RaeedKashif/mlops-kubeflow-assignment
cd mlops-kubeflow-assignment
```
2. Install dependencies
```
python -m venv venv
call venv\Scripts\activate
pip install --upgrade pip
pip install -r requirements.txt
```
3. Set up DVC remote storage
```
dvc remote add -d localstore dvc_storage
dvc pull
```

Note: DVC stores the dataset and pipeline artifacts versioned.

4. Set up MLflow
```
mlflow ui
```

Then open http://localhost:5000 to view experiments.

## Pipeline Walkthrough
Run the pipeline
```
call venv\Scripts\activate
python pipeline_runner.py
```

Step 1: Pulls data from DVC remote storage

Step 2: Preprocesses the data (scaling, splitting)

Step 3: Trains a Random Forest model and logs it to MLflow

Step 4: Evaluates the model, saves metrics to models/metrics.txt

## Continuous Integration

GitHub Actions runs the pipeline on every push automatically

All pipeline logs are available in Jenkins or GitHub Actions console


## Training Component Inputs and Outputs

### Training Component (MLflow version)

#### Inputs

train_data.csv / train_X / train_y — preprocessed training dataset

model_params (optional) — hyperparameters for Random Forest

#### Outputs

model — trained Random Forest model saved as rf_model.joblib

metrics.txt — evaluation metrics (MSE, R²) saved to models/metrics.txt

MLflow logs — all parameters, metrics, and artifacts tracked in the MLflow server

Inputs come from the preprocessing step; outputs are stored both as files and logged in MLflow.

URL to the repository

https://github.com/RaeedKashif/mlops-kubeflow-assignment

Screenshot Deliverables

Main page of the GitHub repo showing README.md and project structure

MLflow dashboard showing experiment logs (optional but recommended)


---

# **2️⃣ Explanation of Training Component Inputs/Outputs**

| **Component**      | **Inputs**                                         | **Outputs**                                   |
|-------------------|---------------------------------------------------|-----------------------------------------------|
| Model Training     | - `train_X` / `train_y` (training data) <br> - `model_params` (optional hyperparameters) | - `rf_model.joblib` (trained model artifact) <br> - `metrics.txt` (MSE, R²) <br> - MLflow logs (parameters, metrics, artifacts) |

- Inputs are taken from the **preprocessing step**  
- Outputs are saved **locally in `models/`** and **logged in MLflow** for reproducibility

---

#  **3️⃣ Push Everything to GitHub**

```bash
git add README.md
git commit -m "Add Task 5 README and documentation"
git push
