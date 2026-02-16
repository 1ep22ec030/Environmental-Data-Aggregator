from google.cloud import pubsub_v1
import time
import random

# ✅ Your REAL Project ID
project_id = "envi-data-aggregator"

# ✅ Your Pub/Sub Topic name
topic_id = "environment-data"

# Create publisher client
publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path(project_id, topic_id)

print("Sending environmental data to Google Cloud...")

while True:
    # 🌡 Simulated sensor readings
    temperature = random.randint(20, 35)   # DHT22
    humidity = random.randint(40, 80)      # DHT22
    pressure = random.randint(980, 1050)   # BMP180

    data = f"Temp:{temperature}C Humidity:{humidity}% Pressure:{pressure}hPa"

    # Publish to Pub/Sub
    future = publisher.publish(topic_path, data.encode("utf-8"))
    print("Sent:", data)

    # Send every 5 seconds (fast demo)
    time.sleep(5)