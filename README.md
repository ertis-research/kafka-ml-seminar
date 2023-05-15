# Kafka-ML Seminar Course

This course aims to provide an overview of the technologies related to [Kafka-ML](https://github.com/ertis-research/kafka-ml/) and the framework itself.

## 1. Docker and Kubernetes
An introduction to Docker and Kubernetes, creating our own containers and orchestrating them in Kubernetes. We will explore the example [Flightradar24-to-kafka-to-node-red-worldmap](https://github.com/ertis-research/flightradar24-to-kafka-to-node-red-worldmap) based on Docker containers to visualize the flights around Malaga in the worldmap Node-RED plugin. 

> Lightweight virtualization technologies such as containers have enabled a way of scaling and reallocating components, services, and applications. Compared to traditional virtualization approaches, containers are similar to virtual machines, except they do not require a hypervisor to work with, as they only need a container runtime.

### Requirements
- [Docker Desktop](https://www.docker.com/products/docker-desktop/)

### Steps before class:
```bash
docker pull nodered/node-red:latest
docker pull zookeeper:3.5.4-beta
docker pull ertis/kafka:2.12-2.2.1
docker pull ertis/flightradar24tokafka
```

## 2. Apache Kafka
Exploring one of the most widely used message queues in big data systems and data streams. First producers and consumers with Kafka exploring its functionalities.

> Apache Kafka is a distributed publish/subscribe queue that can dispatch and consume large amounts of data at low latency. Its architecture comprises a set of brokers, which work together to serve the user-defined topics, the basic units in Kafka to serve and dispatch information. Topics are identified with a name and can have multiple partitions for ingesting large amounts of data (produce side) and increasing the parallelism on the consumer side (through a group of consumers). Finally, each partition can have different replicas for fault-tolerance of the data, which can be kept in Kafka for a period of time or until space is available.

###  Requirements
- [Python](https://www.python.org/downloads/)
- [Confluent Kafka library](https://pypi.org/project/confluent-kafka/)
- [Docker Desktop](https://www.docker.com/products/docker-desktop/)

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

> TensorFlow is one of the most-used end-to-end open-source platform for machine learning. TensorFlow offers a flexible ecosystem of tools, libraries and community resources to build and deploy machine learning powered applications. 


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

> Kafka-ML is an open-source framework that presents a paradigm shift from traditional and static datasets used in ML/AI frameworks into continuous and dynamic data streams, offering a user-friendly, ready-to-use and open platform to the community that allows managing ML/AI pipeline steps such as training and inference deployment in productions environments. All of the Kafka-ML components have been containerized so that they can run as Docker containers. This not only enables easy portability of the architecture, isolation between instances, and fast setup support for different platforms, but also their management and monitoring through Kubernetes. Kubernetes manages the life cycle of Kafka-ML and its components.

###  Steps before class:
Pull the following images from a terminal:
```bash
docker pull ertis/kafka-ml-backend:v1.0
docker pull ertis/kafka-ml-frontend:v1.0
docker pull ertis/kafka-ml-kafka_control_logger:v1.0 
docker pull ertis/kafka-ml-pthexecutor:v1.0 
docker pull ertis/kafka-ml-tfexecutor:v1.0
docker pull ertis/kafka-ml-tensorflow_model_training:v1.0
docker pull ertis/kafka-ml-tensorflow_model_inference:v1.0
docker pull ertis/kafka-ml-pytorch_model_training:v1.0
docker pull ertis/kafka-ml-pytorch_model_inference:v1.0
docker pull confluentinc/cp-zookeeper:7.0.1
docker pull confluentinc/cp-kafka:7.0.1
```
