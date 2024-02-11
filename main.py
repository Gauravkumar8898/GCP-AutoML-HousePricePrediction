from src.pipeline.house_price_prediction_pipeline import Pipeline
from google.cloud import aiplatform
from src.utils.constant import project, location, bucket_name

if __name__ == '__main__':
    aiplatform.init(project=project, location=location)
    pipeline_obj = Pipeline(project, location, bucket_name)
    dataset = pipeline_obj.managed_dataset_runner()
    model = pipeline_obj.house_price_model_runner(dataset)
    pipeline_obj.batch_prediction_runner(model)
