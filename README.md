# Argo Machine Learning Example

This repository demonstrates a few techniques for using argo
and docker in a machine learning workflow. 

The `/code` directory contains some source code in python to
train and serve a scikit-learn model. 

The `/workflows` directory contains argo workflows and templates
to demonstrate a kubernetes based ML pipeline (although admittely over simplified).


In order to run, you'll need access to a kubernetes cluster. You can start
a local cluster using [minikube](https://kubernetes.io/docs/tasks/tools/install-minikube/)
or [docker-for-mac](https://docs.docker.com/docker-for-mac/install/). You could also use a cloud
managed kubernetes service such as [Google's GKE](https://cloud.google.com/kubernetes-engine).

To run this workflow, you'll need to [install Argo](https://github.com/argoproj/argo/blob/master/docs/getting-started.md).

In the templates with s3 configured artifacts, you will need to change the s3 paths
to your own bucket. Finally, you need to configure secrets in the kubernetes cluster
to access the bucket. 