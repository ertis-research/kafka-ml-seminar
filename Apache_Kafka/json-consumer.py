

from confluent_kafka import DeserializingConsumer
from confluent_kafka.schema_registry.json_schema import JSONDeserializer
from confluent_kafka.serialization import StringDeserializer
from confluent_kafka.schema_registry import SchemaRegistryClient

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
    boostrap_servers = "localhost:9092,localhost:9093"
    schema_url = "http://localhost:8081/"
    json_deserializer = JSONDeserializer(schema_str)
    string_deserializer = StringDeserializer('utf_8')

    consumer_conf = {'bootstrap.servers': boostrap_servers,
                     'key.deserializer': string_deserializer,
                     'value.deserializer': json_deserializer,
                     'group.id': "group",
                     'auto.offset.reset': "beginning"}

    consumer = DeserializingConsumer(consumer_conf)
    consumer.subscribe([topic])

    while True:
        try:
            msg = consumer.poll(1.0)
            if msg is None:
                continue

            user = msg.value()
            if user is not None:
                print("User record {}: firstName: {}\n"
                      "\tlastName: {}\n"
                      "\tage: {}\n"
                      .format(msg.key(), user['firstName'],
                              user['lastName'],
                              user['age']))
        except KeyboardInterrupt:
            break

    consumer.close()
    
if __name__ == '__main__':
    main()