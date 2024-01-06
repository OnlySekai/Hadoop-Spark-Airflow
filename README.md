# Project 3

## Run pipeline

1. Install dependency

    ```bash
    pip3 install -r requirement
    ```

1. Run cluster

    ```bash
    docker-compose up -d
    ```

1. Install airflow

    ```bash
    export AIRFLOW_HOME=/working/dir/airflow/dags
    ./install-airflow.sh
    ```

1. Run pipeline

    ```bash
    airflow standalone
    ```

## Crawl data

1. change ```NAME_NODE_ID``` in ```/crawler/constants.py``` by name node container id.

1. Run bash

    ```bash
    cd crawler
    python3 crawler.py
    ```

## Run spark application

1. change ```containerId``` in ```/client/run.sh``` by spark container id.

1. change ```fileName``` in ```/client/run.sh``` by application want run.

1. Run bash

    ```bash
    /client/run.sh
    ```
