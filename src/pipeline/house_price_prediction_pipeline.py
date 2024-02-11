from src.managed_dataset.dataset_handle import HandleDatasetForModel
from src.house_price_pricdiction.house_price_model import HousePricePredictionAutoML
from src.utils.constant import (training_house_dataset_path, destination_blob_name,
                                display_name, gcs_source_training, model_resource,
                                input_data, output_data)
from src.batch_prediction.batch_prediction_house_prediction import BatchPredictionForHousePricePrediction


class Pipeline:
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

    def managed_dataset_runner(self):
        """
        Executes the pipeline for managing datasets.
        Returns: Loaded tabular dataset object.
        """
        dataset_obj = HandleDatasetForModel(self.project, self.location, self.bucket_name)
        dataset_obj.upload_dataset_to_bucket(training_house_dataset_path, destination_blob_name)
        dataset_obj.create_dataset(display_name, gcs_source_training)
        dataset_id = dataset_obj.get_dataset_id(display_name)
        dataset = dataset_obj.load_dataset(dataset_id)
        return dataset

    def house_price_model_runner(self, dataset):
        """
        Executes the pipeline for training the house price prediction model.
        Parameters:Loaded tabular dataset object.
        Returns:Imported model object.
        """
        model_obj = HousePricePredictionAutoML(self.project, self.location, self.bucket_name)
        job = model_obj.create_model()
        model_obj.run_model(dataset, job)
        model = model_obj.import_model(model_resource)
        return model

    def batch_prediction_runner(self, model):
        """
        Executes the pipeline for batch prediction.
        Parameters:
            model: Imported model object.
        """
        prediction_obj = BatchPredictionForHousePricePrediction(self.project,
                                                                self.location, self.bucket_name)
        prediction_obj.batch_prediction_for_model(input_data, output_data, model)
        prediction_obj.fetch_batch_prediction_data_from_bucket()

