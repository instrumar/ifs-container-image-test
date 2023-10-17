import pulsar
import time

# Pulsar configuration
pulsar_service_url = 'pulsar://10.16.2.28:6650'
input_topic = 'persistent://unifiyadkinville/ifs/fibersensordata'
output_topic = 'persistent://unifiyadkinville/ifs/output'

# Initialize Pulsar client
client = pulsar.Client(pulsar_service_url)

# Create producers and consumers for the input and output topics
consumer = client.subscribe(input_topic, subscription_name='subscribe_2', consumer_type=pulsar.ConsumerType.Exclusive)
producer = client.create_producer(output_topic)

last_msg_id = None

while True:
    try:
        # If we've received messages before, start consuming from the last message ID
        if last_msg_id:
            print("consuming messages based on last message id")
            msg = consumer.receive(start_message_id=last_msg_id, timeout_millis=5000)
        else:
            print("consuming messages without last message id")
            msg = consumer.receive(timeout_millis=5000)

        print(msg)

        payload = msg.data()
        producer.send(payload)
        
        # Acknowledge the message and store its ID
        consumer.acknowledge(msg)
        last_msg_id = msg.message_id()
        
        print(f"Received message from {input_topic} and sent it to {output_topic}: {payload.decode('utf-8')}")
    except pulsar.exceptions.Timeout:
        # No message received in the timeout period
        pass
    except Exception as e:
        print(f"Error: {str(e)}")

    time.sleep(30)

# Clean up when the task is stopped (not reached in this example)
consumer.close()
producer.close()
client.close()
