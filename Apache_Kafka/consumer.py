from confluent_kafka import Consumer

def main():
    
    # Consumer creation
    consumer = Consumer({
        'bootstrap.servers': 'localhost:9092', # Kafka Brokers, configure properly
        'group.id': 'incheon', # Group ID. Keep same ID for costumer in the group
        'auto.offset.reset': 'earliest' # Offset configuration: earliest, latest
    })

    consumer.subscribe(['iot']) # Consumer subscribes to a list of topics

    running = True
    # Infinite loop until Ctrl->C is entered
    while running:
        try:
            msg = consumer.poll(timeout=10) # Waits for messages 10s
            if msg is None: # No message
                continue
            if msg.error(): # Error Message
                print("Consumer error: {}".format(msg.error()))
                continue
            print("Message received from partition %d: %s value " % (msg.partition(),
                                                                     str(msg.value().decode('utf8'))))
        except KeyboardInterrupt:
            running = False
        
    print("Bye!")
    consumer.close()
 
if __name__ == "__main__":
    main()
