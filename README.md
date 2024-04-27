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

---


#### Django models datatypes to create a model

Here's a list of common Django model field data types along with their arguments:

1. **AutoField**: An integer field that automatically increments.
   - `primary_key`: If set to `True`, this field will be the primary key for the model.

2. **BigIntegerField**: A 64-bit integer field.
   - `verbose_name`: A human-readable name for the field.
   - `null`: If set to `True`, the field may be null in the database.
   - `blank`: If set to `True`, the field may be left blank in forms.

3. **BooleanField**: A boolean (True/False) field.
   - `default`: The default value for the field.

4. **CharField**: A string field with a maximum length.
   - `max_length`: The maximum length of the field.
   - `verbose_name`, `null`, `blank`

5. **DateField**: A date field.
   - `auto_now`: Automatically set the field to the current date every time the object is saved.
   - `auto_now_add`: Automatically set the field to the current date when the object is first created.

6. **DateTimeField**: A datetime field.
   - `auto_now`, `auto_now_add`, `verbose_name`, `null`, `blank`

7. **DecimalField**: A fixed-point decimal number field.
   - `max_digits`: The maximum number of digits.
   - `decimal_places`: The number of decimal places.

8. **DurationField**: A field for storing a duration of time.

9. **EmailField**: A string field for storing email addresses.
   - `max_length`, `verbose_name`, `null`, `blank`

10. **FileField**: A file upload field.
    - `upload_to`: The directory where uploaded files will be stored.

11. **FloatField**: A floating point number field.

12. **ForeignKey**: A many-to-one relationship.
    - `to`: The related model.
    - `on_delete`: The behavior to follow when the referenced object is deleted.

13. **ImageField**: A field for storing images.
    - `upload_to`

14. **IntegerField**: A 32-bit integer field.
    - `verbose_name`, `null`, `blank`

15. **ManyToManyField**: A many-to-many relationship.
    - `to`, `related_name`

16. **OneToOneField**: A one-to-one relationship.
    - `to`, `on_delete`, `related_name`

17. **PositiveIntegerField**: A positive integer field.
    - `verbose_name`, `null`, `blank`

18. **PositiveSmallIntegerField**: A positive small integer field.
    - `verbose_name`, `null`, `blank`

19. **SlugField**: A field for storing a short label for a URL.
    - `max_length`, `verbose_name`, `null`, `blank`

20. **SmallIntegerField**: A 16-bit integer field.
    - `verbose_name`, `null`, `blank`

21. **TextField**: A large text field.
    - `verbose_name`, `null`, `blank`

22. **TimeField**: A time field.
    - `auto_now`, `auto_now_add`, `verbose_name`, `null`, `blank`

These are the most commonly used field types in Django models along with some of their arguments. Depending on your requirements, you can use these fields and their arguments to define the structure of your models.