# [nnscr.de](http://nnscr.de) Website

Early state of my new website, written with [django](http://djangoproject.com).

Only tested with Python 3.5.

## Setup

    $ pip install --user -r requirements    # Install Python library dependencies
    $ npm install                           # Install development Javascript dependencies
    $ jspm install                          # Install frontend Javascript dependencies
    $ gulp build                            # Build css and Javascript files (transpile less / ECMAScript 6)
    $ ./manage.py collectstatic -l          # Create /static, only required for prod. -l creates symlinks, copy otherwise
    $ ./manage.py migrate                   # Create database schema
    $ ./manage.py createsuperuser           # Create a user for admin backend
    $ ./manage.py runserver                 # Run the development webserver on http://127.0.0.1:8000

## Tests

    $ ./manage.py test
