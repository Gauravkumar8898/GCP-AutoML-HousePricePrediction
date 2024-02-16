import kfp.dsl as dsl
from src.components.components_model import manage_data, manage_model
from src.utils.constant import pipeline_name,description


@dsl.pipeline(
    name=pipeline_name,
    description=description
)
def kube_pipeline():
    step = manage_data()
    manage_model().after(step)



