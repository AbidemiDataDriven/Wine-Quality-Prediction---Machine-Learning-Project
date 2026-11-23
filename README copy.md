## End to End Wine Quality Prediction | Machine Learning Project Implementation
----
## Project Objectives:
This project is about creating a machine learning algorithm that can predict the quality of wine based on the given dataset. Different machine learning algorithms such as Logistic Regression, ElasticNet, Decision Tree and Random Forest are compared to see which model gives the best accuracy.
----
<h2>Tech stack</h2>
<ul>
  <li><strong>Data and machine learning</strong> · Python, pandas, NumPy, scikit-learn (Elastic Net), joblib</li>
  <li><strong>Exploration and visualization</strong> · Matplotlib, seaborn, missingno</li>
  <li><strong>Web app</strong> · Flask, Jinja templates, HTML, CSS, JavaScript</li>
  <li><strong>Configuration and tooling</strong> · YAML, PyYAML, python-box, ensure, tqdm, setuptools, pip</li>
  <li><strong>Additional declared dependencies</strong> · Flask-Cors, types-PyYAML</li>
</ul>

**Abidemi Avoseh** · [LinkedIn](https://www.linkedin.com/in/abidemi-avoseh-811b7615a/) · [GitHub](https://github.com/AbidemiDataDriven) · [Kaggle](https://www.kaggle.com/abidemiavoseh) · [Medium](https://medium.com/@aavoseh) · [X](https://x.com/avoseh_emma) · [Instagram](https://www.instagram.com/abidemi_avoseh/)
# Project workflows:
1. Update config.yaml

2. Update schema.yaml

3. Update params.yaml

4. Update the entity

5. Update the configuration manager in src config

6. Update the components

7. Update the pipeline

8. Update the main.py

9. Update the app.py


A Python machine learning project that estimates red wine quality from 11 physicochemical measurements. The project pairs a staged scikit-learn training pipeline with a Flask form for scoring one sample at a time.

## Data and model

The pipeline uses [a red wine CSV archive](https://github.com/AbidemiDataDriven/raw-dataset/blob/main/winequality-red.csv.zip). The target is the recorded `quality` score. Inputs include fixed and volatile acidity, citric acid, residual sugar, chlorides, free and total sulfur dioxide, density, pH, sulphates, and alcohol.

The trainer fits **Elastic Net regression** with `alpha=0.2` and `l1_ratio=0.1`. The app returns a continuous quality estimate. Evaluation computes **RMSE**, **MAE**, and **R²** on a held-out test split. The repository does not include a metrics report. The 75/25 split has no fixed seed, so reruns can produce different scores.

## Training and inference workflow

| Stage | What it does | Output |
| --- | --- | --- |
| Ingestion | Downloads and extracts the configured dataset archive | `artifacts/data_ingestion/winequality-red.csv` |
| Validation | Checks observed column names against the YAML schema and writes a status file | `artifacts/data_validation/status.txt` |
| Transformation | Splits the dataset into training and test sets | `artifacts/data_transformation/train.csv` and `test.csv` |
| Training | Fits Elastic Net on the training set and serializes it with joblib | `artifacts/model_trainer/model.joblib` |
| Evaluation | Loads the trained model and scores the test set | `artifacts/model_evaluation/metrics.json` |
| Inference | Reads 11 measurements from a Flask form and loads the saved model to predict quality | Prediction displayed in the browser |

## Project layout

| Path | Role |
| --- | --- |
| [`main.py`](main.py) | Orchestrates the five training stages |
| [`app.py`](app.py) | Serves the prediction form and results |
| [`src/WinequalityMachineLearningProject/`](src/WinequalityMachineLearningProject) | Pipeline stages, model components, and configuration utilities |
| [`config/config.yaml`](config/config.yaml) | Dataset source and artifact paths |
| [`schema.yaml`](schema.yaml) | Expected columns and target name |
| [`params.yaml`](params.yaml) | Elastic Net hyperparameters |

## Run locally

From the repository root, create a virtual environment and install the dependencies:

```bash
git clone https://github.com/AbidemiDataDriven/Wine-Quality-Prediction---Machine-Learning-Project.git
cd Wine-Quality-Prediction---Machine-Learning-Project
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

**Current training blocker.** The training entry point imports the ingestion class from the package root, but the class lives in [`pipeline/stage_01_data_ingestion.py`](src/WinequalityMachineLearningProject/pipeline/stage_01_data_ingestion.py). The configuration and evaluation modules also reference `config_entity` at the package root, although it lives under [`entity/`](src/WinequalityMachineLearningProject/entity), and the trainer still imports `mlProject`. Resolve those imports before training from a fresh checkout.

Once the imports are corrected, run:

```bash
python main.py
python app.py
```

Training needs network access to download the dataset archive. Once the model artifact has been generated, open [http://localhost:8080](http://localhost:8080) and submit the wine measurements. The Flask app runs in debug mode for local development.
