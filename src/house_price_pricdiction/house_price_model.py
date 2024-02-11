from google.cloud import aiplatform
from src.utils.constant import target_column, column_transformations


class HousePricePredictionAutoML:
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
    def create_model():
        """
        Creates an AutoML Tabular model for house price prediction.
        Returns: AutoML Tabular training job object.
        """
        job = aiplatform.AutoMLTabularTrainingJob(
            display_name="house-model",
            optimization_prediction_type="regression",
            column_transformations=column_transformations)
        return job

    @staticmethod
    def run_model(dataset, job):
        """
          Parameters:
            dataset: Dataset used for training the model.
            job: AutoML training job object.
        Returns: Trained model object.
        """
        model = job.run(
            dataset=dataset,
            training_fraction_split=0.8,
            validation_fraction_split=0.1,
            test_fraction_split=0.1,
            target_column=target_column,
            budget_milli_node_hours=1000,
            model_display_name="auto-ml-house",
            disable_early_stopping=False
        )
        return model

    @staticmethod
    def import_model(model_resource):
        """
        Imports a pre-trained model.
        Parameters:model_resource (str): Resource name of the pre-trained model.
        Returns: Imported model object.
        """
        model = aiplatform.Model(model_name=model_resource)
        return model
