# Instruction and Getting Started

## Required Dependency

This project runs on Python 3.6 or higher. It also uses virtualenv to manage virtual environments.

### Other Required Software Packages

These additional packages need to be installed too. All of them are listed in the `requirements.txt`.

| Name                      | Required version(s) | Notes            |
| :------------------------ | :------------------ | :--------------- |
| Django                    | 3.1 or higher       | A web framework based on python. |
| django-multiselectfield   | 0.1.12 or higher    | Model field and form field for getting a multiple select from a choices. |
| python-decouple           | 3.3 or higher       | Library that helps separate the settings parameters from source code. |
| Pillow                    | 8.0.1 or higher     | The Python Imaging Library adds image processing capabilities to your Python interpreter. |
| coverage                  | 5.3 or higher       | A test coverage reporting tool to show how much of your code is exercised with your tests. |

## Instructions

Steps to install and run the application.

### 1. Clone the repository and navigate to it

```python
git clone https://github.com/ZEZAY/real-estate-rental.git
cd <path/to/real-estate-rental>
```

### 2. Create a new virtual environment (first time only)

```python
virtualenv env
```

### 3. Activate the virtual environment

On Linux or MacOs:

```python
. env/bin/activate
```

On Windows:

```python
cmd> env\Scripts\activate
```

### 4. Install the required packages (first time only)

```python
(env)cmd> pip install -r requirements.txt
```

### 5. Do database migrations (first time only)

Make migrations.

```python
(env)cmd> python manage.py makemigrations
```

Commit the migrations to the database.

```python
(env)cmd> python manage.py migrate
```

Load the initial data from the .json file.

```python
(env)cmd> python manage.py loaddata initial_data.json
```

### 6. Create a configuration file (optional, first time only)

Create or edit the .env file in the ./estateSite directory.

example of ./estateSite/.env file:

```python
DEBUG=False
ALLOWED_HOSTS=localhost,127.0.0.1
SECRET_KEY='Your-Secret-Key'
DATABASE_ENGINE='django.db.backends.sqlite3'
DATABASE_NAME='db.sqlite3'
DATABASE_USER='test1'
DATABASE_PWD='Noneatall'
DATABASE_HOST='localhost'
TIME_ZONE='Asia/Bangkok'
```

for MacOs run this command to add environment variable define in the .env file

```python
export $(grep -v '^#' ./.env | xargs)
```

### 7. Run the application

```python
(env)cmd> python3 manage.py runserver [port number]
```

The default port number is 8000.

Use `CTRL-Break` to exit the application.

### 8. Exit the virtual environment

```python
(env)cmd> deactivate
```

## Test the Application

Using a web browser to browse at `http://<server url> [:port number]`

If the initial data is successfully load, there should be one condo in the index page name the city condo. In the condo page there should be one room information titled 1240.

There is also one account provided for login:

username: HarryPotter

password: hogwarts1010
