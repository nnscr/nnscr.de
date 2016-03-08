# [nnscr.de](http://nnscr.de) Website

A simple blog written with [django](http://djangoproject.com).

# Features
Blog posts can be written using [Github Flavored Markdown]
(https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet) or HTML.

Static pages and blog posts can be written in the admin area, which is accessible with the `/admin` url.

Comments can only use GFM, HTML and suspicious `javascript:` stuff will be escaped.

Comments are moderated and must be approved by an administrator. There is a simple tool for that in the admin dashboard.

Only tested with Python 3.4+.

## Setup
First, copy `nnscr/settings_local.py.example` to `nnscr/settings_local.py` and adjust the settings as described.

Then run the following commands in the root directory of this application.

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
