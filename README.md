# Project Title
## Environmental Data Aggregator with Raspberry Pi and GCP

---

## Project Description
This project presents an Environmental Data Aggregator system that collects environmental parameters such as temperature, humidity, and atmospheric pressure and sends them to the cloud for storage and analysis. The system is designed using Raspberry Pi and environmental sensors like DHT22 and BMP180. The sensor data is read periodically using a Python script and transmitted to the cloud using a publish–subscribe messaging service.
Due to hardware limitations, the sensor readings were simulated using Python to demonstrate the working of the system. The simulated data is generated at regular intervals and published to a cloud topic using Pub/Sub services available on Google Cloud Platform. A subscription is used to receive the data, thereby validating successful transmission.
The project demonstrates how Internet of Things (IoT) devices can collect real-time environmental data and integrate with cloud platforms for remote monitoring, data storage, and future analytics. It also highlights handling of connectivity and authentication while sending data securely to the cloud.
This system can be extended for real-time weather monitoring, smart agriculture, pollution tracking, and smart city applications.

---

## Objectives

-To simulate environmental data collection,
-To send data to cloud using messaging service,
-To visualize data using cloud monitoring tools,
-To understand IoT + Cloud integration.

---

## Technologies Used
-Python
-Google Cloud Platform
-Cloud Pub/Sub
-Raspberry Pi (conceptual/demo)
-Command Prompt

---

## How It Works
-Environmental data is generated using Python code.
-Data is sent to Cloud Pub/Sub topic.
-Cloud services receive and process the data.
-Graphs and metrics are displayed in cloud console.

---

## Output
-Real-time data transmission
-Monitoring graphs in cloud dashboard
-Successful message publishing and pulling

---

## Applications
-Smart cities
-Pollution monitoring
-Weather tracking
-Environmental research

---

## Developed By
-Fresher student passionate about IoT and Cloud Technologies 

---

## Future Improvements
-Add real sensors (temperature, humidity)
-Use actual Raspberry Pi hardware
-Mobile app dashboard

---

## Thank You
