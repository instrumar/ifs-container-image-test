import pulsar
import time
import pickle

# Pulsar configuration
pulsar_service_url = 'pulsar://10.16.2.28:6650'
input_topic = 'persistent://unifiyadkinville/ifs/fibersensordata'
output_topic = 'persistent://unifiyadkinville/ifs/output'

# Initialize Pulsar client
client = pulsar.Client(pulsar_service_url)

# Create consumers
consumer = client.subscribe(input_topic, subscription_name='subscribe_1', consumer_type=pulsar.ConsumerType.Exclusive)

# Create a producer
producer = client.create_producer(output_topic)

# Variable to store the last processed message ID in memory
last_message_id = None

while True:
    messages = []
    message_ids = []
    start_time = time.time()
    
    while time.time() - start_time < 30 and len(messages) < 100000:
        try:
            msg = consumer.receive(timeout_millis=100)
            messages.append(msg.data())
            message_ids.append(msg.message_id())
        except Exception as e:
            print(e)
            pass

    # Serialize the batch of messages into a single payload (as bytes)
    batch_payload = pickle.dumps(messages)

    # Send the serialized batched payload
    producer.send(batch_payload)
    
    # Acknowledge the last message of the batch and update the last_message_id
    if message_ids:
        last_message_id = message_ids[-1]
        consumer.acknowledge(last_message_id)
    
    print(f"Processed {len(messages)} messages.")

# Clean up
consumer.close()
producer.close()
client.close()
