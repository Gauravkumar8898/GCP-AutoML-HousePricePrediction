import kfp.dsl as dsl
import logging
from src.utils.helpers import manage_data, decision_classifier
from src.utils.constant import base_image
import kfp.dsl.component_factory

logging.basicConfig(level=logging.INFO)


manage_data = kfp.dsl.component_factory.create_component_from_func(
    func=manage_data,
    base_image=base_image,
    packages_to_install=['pandas==2.0.3', 'numpy==1.24.4', 'scikit-learn==1.3.2']
)

manage_model = kfp.dsl.component_factory.create_component_from_func(
    func=decision_classifier,
    base_image=base_image,
    packages_to_install=['scikit-learn==1.3.2']
)


