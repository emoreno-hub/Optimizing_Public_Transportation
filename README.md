# Project: optimizing_public_transportation
This project constructs a streaming event pipeline around Apache Kafka and its ecosystem. Using public data from the Chicago Transit Authority. We will construct an event pipeline around Kafka that allows us to simulate and display the status of train lines in real time.

## Project Architecture
The Chicago Transit Authority (CTA) has asked us to develop a dashboard displaying system status for its commuters. We have decided to use Kafka and ecosystem tools like REST Proxy and Kafka Connect to accomplish this task.

Our architecture will look like so:



## Project Structure
The project consists of two main directories, **producers** and **consumers**.

The following directory layout indicates the files that the student is responsible for modifying by adding a * indicator. Instructions for what is required are present as comments in each file.

The following directory layout indicates the files that the student is responsible for modifying by adding a * indicator. Instructions for what is required are present as comments in each file.

```
Optimizing Public Transportation
|____README.md
|____startup.sh
|
|____ producer
| |____ __init__.py
| |____ connector.py                 * Kafka Connect to Postgres
| |____ simulation.py
| |____ logging.ini
| |____ requirements.txt
| |
| |____ data                         * Data for simulation
| | |____ ridership_curve.csv
| | |____ cta_stations.csv
| | |____ README.md
| | |____ ridership_seed.csv
| |
| |____ models                       * Define Kafka Producer
| | |____ __init__.py
| | |____ producer.py
| | |____ station.py
| | |____ turnstile.py
| | |____ weather.py
| | |____ turnstile_hardware.py
| | |____ line.py
| | |____ train.py
| | |
| | |____ schemas                    * Define Avro schema
| | | |____ arrival_key.json
| | | |____ arrival_value.json
| | | |____ turnstile_key.json
| | | |____ turnstile_value.json
| | | |____ weather_value.json
| | | |____ weather_key.json
|
|____ consumer
| |____ __init__.py
| |____ server.py                    * Server for running Web UI
| |____ logging.ini
| |____ requirements.txt
| |____ topic_check.py
| |____ faust_stream.py              * Using Faust to tranform station data
| |____ consumer.py
| |____ ksql.py                      * Using KSQL to transform turnstile data
| |____ templates
| | |____ status.html
| |
| |____ models                       * Define Kafka Consumer
| | |____ __init__.py
| | |____ line.py
| | |____ weather.py
| | |____ lines.py
| | |____ station.py

```
## Running and Testing
To run the simulation, you must first start up the Kafka ecosystem on their machine utilizing Docker Compose.

%> docker-compose up

Docker compose will take a 3-5 minutes to start, depending on your hardware. Please be patient and wait for the docker-compose logs to slow down or stop before beginning the simulation.
