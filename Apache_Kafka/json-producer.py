from uuid import uuid4
import time
from confluent_kafka import SerializingProducer
from confluent_kafka.serialization import StringSerializer
from confluent_kafka.schema_registry import SchemaRegistryClient
from confluent_kafka.schema_registry.json_schema import JSONSerializer
import json

# python3 -m pip install  'jsonschema<4.0'
def delivery_callback(err, msg):
    if err is not None:
        print("Failed to deliver message: %s: %s" % (str(msg), str(err)))
    else:
        print("Message sent to topic %s partition %s with latency %f" % (str(msg.topic()), str(msg.partition()), msg.latency()))



def main():
    # JSON schema
    schema_str = """
    {
      "$id": "https://example.com/person.schema.json",
      "$schema": "https://json-schema.org/draft/2020-12/schema",
      "title": "Person",
      "type": "object",
      "properties": {
        "firstName": {
          "type": "string",
          "description": "The person's first name."
        },
        "lastName": {
          "type": "string",
          "description": "The person's last name."
        },
        "age": {
          "description": "Age in years which must be equal to or greater than zero.",
          "type": "integer",
          "minimum": 0
        }
      }
    }
    """
    topic = "json"
    boostrap_servers = "localhost:9092"
    schema_url = "http://localhost:8081/"
    
    schema_registry_conf = {'url': schema_url}
    schema_registry_client = SchemaRegistryClient(schema_registry_conf)

    json_serializer = JSONSerializer(schema_str, schema_registry_client)

    producer_conf = {'bootstrap.servers': boostrap_servers,
                     'key.serializer': StringSerializer('utf_8'),
                     'value.serializer': json_serializer}

    producer = SerializingProducer(producer_conf)

    jdata = {
                "firstName": "John",
                "lastName": "Doe",
                "age": "21",
                "type": 121
    }
    print("Producing user records to topic {}. ^C to exit.".format(topic))
    while True:
        producer.poll(0.0)
        try:
            producer.produce(topic=topic, value=jdata,
                             on_delivery=delivery_callback)
            time.sleep(1)
        except KeyboardInterrupt:
            break

    producer.flush()


if __name__ == '__main__':
    main()