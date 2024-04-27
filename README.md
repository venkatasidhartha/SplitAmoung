# SplitAmoung
---

## Getting Started with Django

### Installation

1. Install Python: Make sure you have Python installed on your system. You can download and install Python from the [official Python website](https://www.python.org/).


### Virtual Enviroment 

Create Virtual Enviroment for python, run the following command:

```
pyhton3 -m venv env
```
Replace `env` with the name you like it.


### Django Commands

#### Installing Python Requirements 

Use requirements.txt to install, run the following command:

```
pip install -r requirements.txt
```


#### Creating a Django App

To create a new Django app within your project, navigate to your project directory and run the following command:

```
python3 manage.py startapp myapp
```

Replace `myapp` with the name of your app.

#### Running Migrations

Django migrations are used to propagate changes you make to your models (adding a field, deleting a model, etc.) into your database schema.

1. Generate migrations for your app by running:

    ```
    python3 manage.py makemigrations myapp
    ```

    Replace `myapp` with the name of your app.

2. Apply migrations to your database by running:

    ```
    python3 manage.py migrate
    ```

#### Creating a Superuser

To create a superuser (an admin user) for your Django project, run the following command:

```
python3 manage.py createsuperuser
```

Follow the prompts to enter the username, email, and password for the superuser.

#### Running the Development Server

To start the Django development server, run the following command:

```
python manage.py runserver
```

By default, the server will run on `http://127.0.0.1:8000/`. You can access your Django project by visiting this URL in your web browser.

### Additional Resources

- [Django Documentation](https://docs.djangoproject.com/): Official documentation for Django.
- [Django Girls Tutorial](https://tutorial.djangogirls.org/): A beginner-friendly tutorial for Django.
- [Mozilla Developer Network (MDN) Django Tutorial](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django): Another comprehensive tutorial for Django.

---

Feel free to customize and expand upon this guide to better suit your project's needs and your users' level of experience with Django.