# Django App - ToDo APP

A Simple Web Application made using python-django with user authentication functionality, and stores the data in sqlite database. It performs crud. You need to add your gmail credentials in order forget password functionality to work. 

## More about CRUD
The acronym CRUD stands for create, read, update and delete. These are the four basic functions of persistent storage.
* CREATE procedures: Performs the INSERT statement to create a new record.
* READ procedures: Reads the table records based on the primary keynoted within the input parameter.
* UPDATE procedures: Executes an UPDATE statement on the table based on the specified primary key for a record within the WHERE clause of the statement.
* DELETE procedures: Deletes a specified row in the WHERE clause.

## Requirements

The python dependencies are managed using pip and listed in
`requirements.txt`

## Setting up Local Development

First, clone this repository:

    git clone https://github.com/kush225/django_todo.git

You can use pip, virtualenv and virtualenvwrapper to install the requirements:

    pip install -r requirements.txt
    
Migrate tables to sqlite3 database using commands:

    python manage.py migrate
    
Setting up the values of Environment Variables or you can manually at this at todo_django/settings.py file:

    SECRET_KEY - you can set any values you want
    USER_EMAIL - set this to your gmail email address.
    USER_PASSWORD - set this to your gmail password.
    
    
Start the server by running `python manage.py runserver`:

	python manage.py runserver

Browse to [localhost](http://127.0.0.1:8000) for the index page


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.


## APP LINK
[APP](http://kushagra225.pythonanywhere.com/)
