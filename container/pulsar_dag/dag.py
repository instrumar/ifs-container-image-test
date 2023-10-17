import pulsar
import time

# Pulsar configuration
pulsar_service_url = 'pulsar://10.16.2.28:6650'
input_topic = 'persistent://unifiyadkinville/ifs/fibersensordata'
output_topic = 'persistent://unifiyadkinville/ifs/output'

# Initialize Pulsar client
client = pulsar.Client(pulsar_service_url)

# Create producers and consumers for the input and output topics
consumer = client.subscribe(input_topic, subscription_name='subscribe_1')
producer = client.create_producer(output_topic)

while True:
    try:
        msg = consumer.receive()
        payload = msg.data()
        producer.send(payload)
        consumer.acknowledge(msg)
        print(f"Received message from {input_topic} and sent it to {output_topic}: {payload.decode('utf-8')}")
    except Exception as e:
        print(f"Error: {str(e)}")

    time.sleep(30)

# Clean up when the task is stopped (not reached in this example)
consumer.close()
producer.close()
client.close()
