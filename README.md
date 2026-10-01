DL-03 - Shipping What You Build

A simple Flask application used to practise deploying a Python application to a public hosting platform.

What This Project Demonstrates

Running a Flask application locally

Managing Python dependencies with requirements.txt

Using environment variables for configuration

Deploying a Flask application to Render

Using Gunicorn to start the application in a deployed environment

Testing a deployed application through public routes

Project Structure

DL-03-Shipping/
├── app.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md

.env and .venv/ are local files and should not be committed to GitHub.

Running Locally

Create and activate a virtual environment, then install the dependencies:

pip install -r requirements.txt

Create a .env file containing:

JWT_SECRET_KEY=your-local-secret

Start the Flask application:

python app.py

The application will be available at:

http://127.0.0.1:5000

Routes

Route

Purpose

/

Confirms that the application is running

/health

Health check endpoint

/config-check

Checks that the required environment variable is configured

Deployment

The application is deployed to Render using:

Build command

pip install -r requirements.txt

Start command

gunicorn app:app

The JWT_SECRET_KEY environment variable is configured directly in the hosting platform rather than committed to the repository.

Learning Goal

The goal of this project is to practise taking a Python application from a local development environment to a publicly accessible deployment and troubleshooting common deployment issues.