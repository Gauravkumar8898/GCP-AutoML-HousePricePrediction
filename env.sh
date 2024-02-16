export PROJECT_ID=$(gcloud config list project --format "value(core.project)")
export REPO_NAME=customrepo
export IMAGE_NAME=kubeflow
export IMAGE_TAG=latest_pipeline
export IMAGE_URI=us-central1-docker.pkg.dev/${PROJECT_ID}/${REPO_NAME}/${IMAGE_NAME}:${IMAGE_TAG}


docker build -f Dockerfile -t ${IMAGE_URI} ./

docker push ${IMAGE_URI}
