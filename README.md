# Kafka-ML Seminar Course

This course aims to provide an overview of the technologies related to [Kafka-ML](https://github.com/ertis-research/kafka-ml/) and the framework itself.

## 1. Docker and Kubernetes
An introduction to Docker and Kubernetes, creating our own containers and orchestrating them in Kubernetes. We will explore the example [Flightradar24-to-kafka-to-node-red-worldmap](https://github.com/ertis-research/flightradar24-to-kafka-to-node-red-worldmap) based on Docker containers to visualize the flights around Malaga in the worldmap Node-RED plugin.

### Requirements
- [Docker](https://www.docker.com/)
- [kubernetes>=v1.15.5](https://kubernetes.io/)

### Steps before class:
```bash
docker pull nodered/node-red:latest
docker pull zookeeper:3.5.4-beta
docker pull ertis/kafka:2.12-2.2.1
docker pull ertis/flightradar24tokafka
```

## 2. Apache Kafka
Exploring one of the most widely used message queues in big data systems and data streams. First producers and consumers with Kafka exploring its functionalities.

###  Requirements
- [Python 3.6-3.9](https://www.python.org/downloads/)
- [Confluent Kafka library](https://pypi.org/project/confluent-kafka/)

###  Steps before class:
Pull Zookeeper, Kafka and Kafka manager images from a terminal:
```bash
docker pull confluentinc/cp-zookeeper:7.0.1
docker pull confluentinc/cp-kafka:7.0.1
docker pull deltaprojects/kafka-manager:v3.0.0.6-2
```

And install the confluent kafka library:
```bash
python3 -m pip install confluent-kafka
```

## 3. TensorFlow
Hand-ons with one of the most widely used machine learning frameworks in use today. We will discuss some regression and classification examples and use machine learning to predict a soft sensor property of a river dataset.

###  Steps before class:
Pull the Tensorflow image before class:
```bash
docker pull tensorflow/tensorflow:2.9.1-jupyter
```

Execute the Tensorflow Jupyter:
```bash
docker run -it -p 8888:8888 tensorflow/tensorflow:2.9.1-jupyter
```

## 4. Kafka-ML
After the introduction of the main technologies around [Kafka-ML](https://github.com/ertis-research/kafka-ml/), we will start using this open-source framework to carry out machine learning with data streams. We will also discover the main features of Kafka-ML such as incremental learning and distributed model management.
 
###  Steps before class:
Pull the following images from a terminal:
```bash
docker pull ertis/kafka-ml-backend:v1.2
docker pull ertis/kafka-ml-frontend:v1.2
docker pull ertis/kafka-ml-kafka_control_logger:v1.0 
docker pull ertis/kafka-ml-pthexecutor:v1.0 
docker pull ertis/kafka-ml-tfexecutor:v1.0
docker pull ertis/kafka-ml-tensorflow_model_training:v1.2
docker pull ertis/kafka-ml-tensorflow_model_inference:v1.1
docker pull ertis/kafka-ml-pytorch_model_training:v1.0
docker pull ertis/kafka-ml-pytorch_model_inference:v1.0
docker pull confluentinc/cp-zookeeper:7.0.1
docker pull confluentinc/cp-kafka:7.0.1
docker pull deltaprojects/kafka-manager:v3.0.0.6-2
```