from src.utils.constant import template_path, project, staged_path,pipeline_job_name
from google.cloud import aiplatform


aiplatform.init(project=project, staging_bucket=staged_path)

job = aiplatform.PipelineJob(
    display_name=pipeline_job_name,
    template_path=template_path
)
job.run()
