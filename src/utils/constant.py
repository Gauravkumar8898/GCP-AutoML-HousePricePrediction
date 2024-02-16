from pathlib import Path

curr_path = Path(__file__).parents[1]
data_directory = curr_path / 'data'
data_gcs_path = "gs://marine-might-413408/healthcare-dataset-stroke-data.csv"
healthcare_dataset_path = data_directory / 'healthcare_dataset_stroke_data.csv'
bucket_name = "marine-might-413408"
model_bucket = 'output/model/model.joblib'
categorical_cols = ['gender', 'ever_married', 'work_type', 'Residence_type', 'smoking_status']

PROJECT_ID = bucket_name
REPO_NAME = "customrepo"
IMAGE_NAME = "kubeflow"
IMAGE_TAG = "latest_pipeline"

base_image = f'us-central1-docker.pkg.dev/{PROJECT_ID}/{REPO_NAME}/{IMAGE_NAME}:{IMAGE_TAG}'
staged_path = "gs://marine-might-413408/output"
pipeline_name = "dataset health"
project = "marine-might-413408"
location = "us-central1"
description = "creating pipeline on the healthcare datatset"
pipeline_job_name = 'pipeline-test-1'
template_path = '/home/nashtech/PycharmProjects/kubeflow/pipeline.json'
