# Catalyst-Media Assignment

## Overview
Catalyst-Count is a web application built with Django 3.x/4.x, PostgreSQL, and Bootstrap 4/5. The application allows users to log in and upload large CSV files (up to 1GB) with a visual progress indicator for the upload. Once uploaded, the data is stored in a PostgreSQL database. Users can filter the data using a form and view the count of records based on the applied filters.

## Features
1. User Authentication: Authentication is handled via django-allauth.
2.  File Upload: Users can upload large CSV files with a visual progress bar.
3. Data Storage: Uploaded data is stored in a PostgreSQL database.
4. Data Filtering: Users can filter the data and view the count of records based on the applied filters.
5. Responsive UI: The application uses Bootstrap 4/5 for a responsive and modern UI.

## Project Setup
### Prerequisites
Python 3.x
Django 3.x/4.x
PostgreSQL
Git

### Installation
Clone the repository:
git clone https://github.com/shashiprajj/catalyst_count.git
cd catalyst-count

### Create and activate a virtual environment:
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

### Install dependencies:
pip install -r requirements.txt

### Set up environment variables:
Create a .env file in the project root.
Add your environment-specific variables (e.g., database credentials).
Example .env file:
   DEBUG=True
   SECRET_KEY=your_secret_key
   DATABASE_URL=postgres://user:password@localhost:5432/catalyst_count

### Apply migrations:
python manage.py migrate

### Create a superuser:
python manage.py createsuperuser

### Run the development server:
python manage.py runserver

## Application Structure
### Models
   1. UploadedFile: Stores information about the uploaded files.
   2. CompanyData: Stores the data extracted from the uploaded CSV files.
### Forms
   1. UploadFileForm: Handles file uploads.
   2. QueryForm: Handles data filtering.
### Views
   1. upload_data: Manages file uploads and updates the database with the file contents.
   2. query_builder: Handles data filtering and displays the count of records based on the filters.
### Templates
   1. base.html: Base template with navigation.
   2. upload_data.html: Template for the upload data page.
   3. query_builder.html: Template for the query builder page.

### Usage
   1. Login: -Users can log in using the authentication system provided by django-allauth.

### Upload Data
   1. Navigate to the Upload Data page.
   2.Choose a CSV file and click "Start Upload".
   3. The file upload progress will be displayed.
   4. Once uploaded, the data will be saved to the database.

### Query Builder
   1. Navigate to the Query Builder page.
   2. Use the form to apply filters.
   3. Submit the form to view the count of records that match the filters.


### Acknowledgements
The test data set used is https://www.dropbox.com/scl/fi/r97699phgl1xbjzlenfgi/free-7-million-company-dataset.zip?rlkey=9xi6i2pl0kv4giifaae9sshj0&e=1&dl=0.
The project uses django-allauth for authentication and Bootstrap for the UI.
