# Catalyst Media Assignment
# catalyst count

## Brief description of your project.
The Catalyst Count web application is built using Django 3.x/4.x, PostgreSQL, and Bootstrap 4/5. It allows users to upload large CSV files (up to 1GB) with a visual progress bar, updates a PostgreSQL database with the file contents, and provides functionality to filter and query the data.

## Features
1. Login: Users can log in securely using django-allauth.
2. Upload Data: Supports uploading large CSV files with a visual progress bar.
Query Builder: Users can filter data using a form and view record counts based on applied filters.
Users: User management and authentication are handled through django-allauth.
Setup Instructions
To run this project locally, follow these steps:

## Prerequisites
Python 3.x
PostgreSQL installed and running
Git installed
Installation
Clone the repository:

bash
Copy code
git clone <repository-url>
cd catalyst-count
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Set up environment variables:

Create a .env file in the root directory based on .env.example and set necessary environment variables.
Database setup:

Ensure PostgreSQL is running.
Update settings.py with your PostgreSQL database configuration.
Apply database migrations:

bash
Copy code
python manage.py migrate
Start the development server:

bash
Copy code
python manage.py runserver
Access the application at http://localhost:8000.

Usage
Login: Navigate to the login page and authenticate using your credentials.
Upload Data: Go to the Upload Data page, select a CSV file, and monitor the progress bar for upload completion.
Query Builder: Use the Query Builder page to filter data based on various criteria and view the record counts.
Users: Manage users and authentication through django-allauth.

## Credits
Data set used: https://www.dropbox.com/scl/fi/r97699phgl1xbjzlenfgi/free-7-million-company-dataset.zip?rlkey=9xi6i2pl0kv4giifaae9sshj0&e=1&dl=0


## Setup Instructions

### Backend (Django)
1. Install Django and Django REST Framework
   
3. Clone the repository:

3. Navigate to the project directory
   
5. install all backend requirements using-> py -m pip freeze > requirements.txt
   
6. Run migrations:
   python manage.py makemigrations, 
   python manage.py migrate
   
8. Start the Django development server:
   python manage.py runserver


### Frontend (React)

1. Navigate to the frontend directory:

2. Install dependencies:
   npm install

4. Start the development server:
   npm start

## Technologies Used

- Django
- Django REST Framework
- React
- Axios (for HTTP requests)



