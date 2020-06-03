# tasty_dishes
This is a simple URL Hide/Shortener application.

# General Features
- Registered users can create hide/short URL and showing link's statistics.
- And delete URL's, also update password.
- Anonymous people can only use hide/short URL.

# Link Features
-

# Installation
$ git clone https://github.com/eibrahimarisoy/url-hide-app.git
$ cd url-hide-app/
$ virtualenv venv
$ . venv/bin/activate
$ pip3 install -r requirements.txt
$ python3 manage.py migrate
$ python3 manage.py runserver
$ open http://127.0.0.1:8000/