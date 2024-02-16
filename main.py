from kfp import compiler
from src.pipeline.pipeline_model import kube_pipeline


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    compiler.Compiler().compile(kube_pipeline, '../../pipeline.json')
