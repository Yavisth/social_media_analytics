# Social Media Analytics

Social Media Analytics is a Flask application for analyzing social media data.

## Table of Contents

- [Introduction](#introduction)
- [Scaling and Infrastructure](#Scaling-and-Infrastructure)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Running the Application](#running-the-application)
- [Database Setup](#database-setup)

## Introduction

This Flask application provides tools for social media data analytics. Users can analyze trends, track hashtags, and gain insights into their social media presence.

## Scaling and Infrastructure

The application uses Flask for the web framework, PostgreSQL for the database, Celery for background tasks, and RabbitMQ as the message broker.

1. Flask: The lightweight web framework is suitable for this application due to its simplicity and ease of use.
2. PostgreSQL: Chosen for the relational database for data consistency and support for complex queries.
3. Celery: Used for handling asynchronous tasks such as post analysis.
4. RabbitMQ: Serves as the message broker for Celery.

## Features

- Database Choice: PostgreSQL was chosen for its relational model and the need for data integrity in a social media analytics application.
- Asynchronous Processing: Celery and RabbitMQ were chosen to handle background tasks asynchronously to improve application responsiveness.
- Flask Application Structure: The application follows a modular structure with separate files for models, views, and tasks to enhance maintainability.

## Getting Started

### Prerequisites

- Python (version 3.9)
- PostgreSQL (or your preferred database)

### Installation

1. Clone the repository:

  ```bash
   git clone https://github.com/your-username/social-media-analytics.git
  ```
2. Navigate to the project directory:
   ```bash
   cd social-media-analytics
   ```
3. Create a virtual environment:
   ```bash
    python -m virtualenv env
   ```
4. Activate the virtual environment:
    ```bash
    .\env\Scripts\activate
   ```
5. Install the required dependencies:
   ```bash
    pip install -r requirements.txt
   ```
6. Make sure your rabbitmq, celery, and postgresql database are setup and running. Edit the configuration accordingly in ```__init.py__```

## Running the Application

- Run the following command to start the Flask development server:
```bash
  python run.py
```
- Run the following to start the worker service (celery):
```bash
  python -m celery -A app.celery worker --loglevel=info
```
Visit http://localhost:5000 in your web browser to access the application.

-Visit endpoint '/api/v1/posts/', wherein a json in the form of {<"id">, <"content">} can be sent to populate the database
-Visit endpoint '/api/v1/posts/<post_id>/analysis/', is a celery worker that is an analysis endpoint that returns
  the number of words and average word length in a post.

##  Database Setup
1. Make sure your PostgreSQL server is running.
2. Initialize the database and create tables:
   ```bash
   python -m flask db upgrade
   ```
