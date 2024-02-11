from src.utils.constant import data_directory
from google.cloud import storage
import pandas as pd
import io


class BatchPredictionForHousePricePrediction:

    def __init__(self, my_project, location, bucket_name):
        """
         Parameters:
             my_project (str): Google Cloud project ID.
             location (str): Location of the Google Cloud resources.
             bucket_name (str): Name of the Google Cloud Storage bucket.
         """
        self.project = my_project
        self.location = location
        self.bucket_name = bucket_name

    @staticmethod
    def batch_prediction_for_model(input_data, output_data, model):
        """
        :param input_data: Google Cloud Storage (GCS) location of the input data in CSV format.
        :param output_data: Prefix of the GCS destination where the batch-predicted data will be stored.
        :param model: Model used for batch prediction.
        :return: None
        """
        _ = model.batch_predict(
            job_display_name="tabular_regression_batch_predict_job",
            gcs_source=input_data,
            instances_format="csv",
            predictions_format="csv",
            gcs_destination_prefix=output_data)

    def fetch_batch_prediction_data_from_bucket(self):
        """
        Fetches batch-predicted data from a Google Cloud Storage bucket and concatenates it into a DataFrame.
        Returns:
            None
        """
        # Initialize an empty DataFrame to store the batch-predicted data
        df = pd.DataFrame()
        for i in range(9):
            # Formulate the name of the batch prediction file
            data = f"prediction.results-0000{i}-of-00009.csv"
            file_name = f'output/prediction-auto-ml-house-2024_02_11T03_30_15_401Z/{data}'

            # Connect to Google Cloud Storage and download the batch prediction file
            client = storage.Client(project=self.project)
            bucket = client.get_bucket(self.bucket_name)
            blob = bucket.blob(file_name)
            data = blob.download_as_string()

            # Read the downloaded CSV data into a DataFrame
            batch_dataset = pd.read_csv(io.BytesIO(data))

            # Concatenate the batch dataset with the existing DataFrame
            df = pd.concat([df, batch_dataset])
            print(batch_dataset.head())
        # Save the concatenated DataFrame to a CSV file
        df.to_csv(f"{data_directory}/batch_predicted_dataset.csv")
