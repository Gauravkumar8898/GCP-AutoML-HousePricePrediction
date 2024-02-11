from pathlib import Path
from google.cloud import aiplatform

# Define project, location, and bucket name
project = "marine-might-413408"
location = "us-central1"
bucket_name = 'marine-might-413408'

# Define file paths
curr_path = Path(__file__).parents[1]
data_directory = curr_path / 'data'
training_house_dataset_path = data_directory / "training.csv"
prediction_house_dataset_path = data_directory / "input.csv"

# Define destination blob name and display name
destination_blob_name = "house_price_predictions"
display_name = "house_prediction_"

# Define Google Cloud Storage (GCS) source for training dataset
gcs_source_training = "gs://marine-might-413408/house_price_predictions"

# Initialize AI Platform Dataset Service Client
client = aiplatform.gapic.DatasetServiceClient(client_options={"api_endpoint": "us-central1-aiplatform.googleapis.com"})

# Define target column and column transformations
target_column = "Price"
column_transformations = [
    {"numeric": {"column_name": "SquareFeet"}},
    {"numeric": {"column_name": "Bedrooms"}},
    {"numeric": {"column_name": "Bathrooms"}},
    {"numeric": {"column_name": "YearBuilt"}}]

# Define input and output data paths for batch prediction
input_data = "gs://marine-might-413408/input.csv"
output_data = "gs://marine-might-413408/output"

# Define model resource ID for importing the model
model_resource = "638453416900689920"
