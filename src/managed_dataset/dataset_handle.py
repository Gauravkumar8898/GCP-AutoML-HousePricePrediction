from google.cloud import aiplatform
from google.cloud import storage
from src.utils.constant import client


class HandleDatasetForModel:
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

    def upload_dataset_to_bucket(self, source_file_name, destination_blob_name):
        """
        Uploads a file to a Google Cloud Storage bucket.
        Parameters:
            source_file_name (str): Local file path of the source dataset.
            destination_blob_name (str): Destination blob name in the Google Cloud Storage bucket.
        """
        storage_client = storage.Client()
        bucket = storage_client.get_bucket(self.bucket_name)
        blob = bucket.blob(destination_blob_name)
        blob.upload_from_filename(source_file_name, if_generation_match=0)

    @staticmethod
    def create_dataset(display_name, gcs_source):
        """
        Creates a tabular dataset.
        Parameters:
            display_name (str): Display name of the dataset.
            gcs_source (str): Google Cloud Storage (GCS) location of the dataset.
        Returns: Created tabular dataset object.
        """
        dataset = aiplatform.TabularDataset.create(
            display_name=display_name,
            gcs_source=gcs_source
        )
        return dataset

    def load_dataset(self, dataset_id):
        """
        Loads a tabular dataset.
        Parameters: ID of the dataset.
        Returns: Loaded tabular dataset object.
        """
        aiplatform.init(project=self.project, location=self.location)
        dataset = aiplatform.TabularDataset(f"projects/{self.project}/locations/{self.location}/datasets/{dataset_id}")
        return dataset

    def get_dataset_id(self, display_name):
        """
        Retrieves the ID of a dataset based on its display name.
        Parameters:Display name of the dataset.
        Returns: str: ID of the dataset.
        """
        datasets = client.list_datasets(parent=f"projects/{self.project}/locations/us-central1")
        dataset_id = ""
        for dataset in datasets:
            if dataset.display_name == display_name:
                dataset_id: str = dataset.name.split("/")[-1]
        return dataset_id

    def dataset_is_exist(self, dataset_id):
        """
        Checks if a dataset exists.
        Parameters:
            dataset_id (str): ID of the dataset.
        Returns:
            bool: True if the dataset exists, False otherwise.
        """
        dataset_name = f"projects/{self.project}/locations/{self.location}/datasets/{dataset_id}"
        try:
            _ = client.get_dataset(name=dataset_name)
            return True
        except Exception:
            return False
