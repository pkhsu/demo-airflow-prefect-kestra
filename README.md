# Data Pipeline Orchestration Demos

This repository contains demonstrations of data pipeline orchestration using Airflow, Prefect, and Kestra. Each tool is setup within its own Docker environment for ease of use and reproducibility.

## Overview

The purpose of this repository is to provide practical examples and comparisons between three of the most popular data pipeline orchestration tools:

- Apache Airflow
- Prefect
- Kestra

These examples focus on a simple bash and data pipeline process, which is implemented separately in each orchestration tool to illustrate their unique features and usage.

There are another simple data lifecycle management (DLM) process only with Prefect.

## Getting Started

To get started with these demos, you will need Docker and Docker Compose installed on your machine. Follow the instructions below to setup and run the environments.

### Prerequisites

- Docker
- Docker Compose

### Installation

1. **Clone the Repository**

   Clone this repository to your local machine using the following command:

   ```bash
   git clone https://github.com/pkhsu/demo-airflow-prefect-kestra.git
   cd demo-airflow-prefect-kestra
   ```

### Running the Docker Compose Environments

Navigate to the directory of the tool you wish to run and use Docker Compose to start the services:

```bash
cd <tool_name>  # Replace <tool_name> with airflow, prefect, or kestra
docker-compose up -d
```

This command will build the necessary Docker images and start the services defined in the docker-compose.yml file.

## Usage

Each tool's directory contains specific instructions on how to interact with the orchestration environments:

- **Airflow**:
  - Access the Airflow web UI at http://localhost:8080.
  - Login with the default credentials if required (username: airflow, password: airflow).

- **Prefect**:
  - Access the Prefect UI at http://localhost:4200.
  - Use the provided flows to manage data through Prefect's interface.

- **Kestra**:
  - Access the Kestra UI at http://localhost:8080.
  - Explore the provided workflows directly from the web interface.

## Directory Structure

- /airflow: Contains all files necessary for running Apache Airflow.
- /prefect: Contains all files necessary for running Prefect.
- /kestra: Contains all files necessary for running Kestra.

## Customization

You can modify the workflows and configurations as needed to suit your specific requirements or to test different scenarios.

Thank you for exploring the data pipeline orchestration demos with Airflow, Prefect, and Kestra!
