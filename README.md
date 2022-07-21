# Kafka-ML Seminar Course

This course aims to provide an overview of the technologies related to [Kafka-ML](https://github.com/ertis-research/kafka-ml/) and the framework itself.

## 1. Docker and Kubernetes
An introduction to Docker and Kubernetes, creating our own containers and orchestrating them in Kubernetes.

## Requirements
- [Docker](https://www.docker.com/)
- [kubernetes>=v1.15.5](https://kubernetes.io/)

## 2. Apache Kafka
Exploring one of the most widely used message queues in big data systems and data streams. First producers and consumers with Kafka.

## Requirements
- [Python 3.6-3.9](https://www.python.org/downloads/)
- [Confluent Kafka library](https://pypi.org/project/confluent-kafka/)

## 3. TensorFlow
Hand-ons with one of the most widely used machine learning frameworks in use today.

## Requirements
Pull the Tensorflow image before class:
```bash
docker pull tensorflow/tensorflow:2.9.1-jupyter
```
## Steps
Execute the Tensorflow Jupyter:
```bash
docker run -it -p 8888:8888 tensorflow/tensorflow:2.9.1-jupyter
```

## 4. Kafka-ML
TBU