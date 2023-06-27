from confluent_kafka import Producer
import socket

'''
    Kafka Producer used in class
'''

__author__ = 'Cristian Martin'


# Callback for message delivery confirmation
def delivery_callback(err, msg):
    if err is not None:
        print("Failed to deliver message: %s: %s" % (str(msg), str(err)))
    else:
        print("Message sent to topic %s partition %s with latency %f" % (str(msg.topic()), 
                                                                         str(msg.partition()), 
                                                                         msg.latency()))

def main():
    conf = {'bootstrap.servers': "localhost:9092"} # Kafka Brokers, configure properly
    producer = Producer(conf) # Define the producer
    # Send a message with Kafka
    producer.produce("iot", key="clave", value="Hello world!", callback=delivery_callback)
    producer.poll(1) # Polls the producer for events and calls the corresponding callbacks 
    producer.flush() # Wait for all messages in the Producer queue to be delivered
    
if __name__ == "__main__":
    main()
