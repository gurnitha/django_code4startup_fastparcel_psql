## MEMBUAT APLIKASI FASTPARCEL MENGGUNAKAN DJANGO

https://github.com/gurnitha/django_code4startup_fastparcel_psql

### 1. BASIC SETUP

#### 1.1 Membuat root folder dan local repository

        new file:   .gitignore
        new file:   readme.md

#### 1.2 Membuat remote repository di Github

        https://github.com/gurnitha/django_code4startup_fastparcel_psql
        modified:   readme.md		

#### 1.3 Membuat virtual environment

       λ python -m venv venv3931
        modified:   .gitignore
        modified:   readme.md

#### 1.4 Menginstall django v3.1

       λ venv3931\scripts\activate
       (venv3931) λ python -m pip install django==3.1
       (venv3931) λ python -m pip install --upgrade pip
        modified:   readme.md

### 2. DJANGO PROYEK

#### 2.1 Inisiasi django proyek dgn nama 'config'
		.
		├── config
		│   ├── __init__.py
		│   ├── __pycache__
		│   ├── asgi.py
		│   ├── settings.py
		│   ├── urls.py
		│   └── wsgi.py
		├── db.sqlite3
		├── manage.py
		├── readme.md
		└── venv3931
		    ├── Include
		    ├── Lib
		    ├── Scripts
		    └── pyvenv.cfg

### 3. DJANGO APP

#### 3.1 Membuat folder untuk semua Django App dgn nama 'apps'

        (venv3931) λ mkdir apps
        modified:   readme.md

#### 3.4 Membuat folder dengan nama 'core' di dalam folder 'apps'

		(venv3931) λ mkdir apps\core
		.
		├── apps
		│   └── core

        modified:   readme.md

#### 3.5 Membuat django app dengan 'core' di dalam folder 'apps'

		(venv3931) λ python manage.py startapp core apps/core

		.
		├── apps
		│   └── core
		│       ├── __init__.py
		│       ├── admin.py
		│       ├── apps.py
		│       ├── migrations
		│       ├── models.py
		│       ├── tests.py
		│       └── views.py
		├── config
		...
		└── venv3931
        modified:   readme.md

#### 3.6 Memodifikasi file core/apps.py agar django app 'core' dapat diakses

        modified:   apps/core/apps.py
        modified:   readme.md

#### 3.7 Meregistrasi django app 'core' pada django proyek 'config/settings.py'

        modified:   config/settings.py
        modified:   readme.md

#### 3.8 Jalankan server untuk testing

       (venv3931) λ python manage.py runserver
       Watching for file changes with StatReloader
       Performing system checks...

       System check identified no issues (0 silenced).

       You have 18 unapplied migration(s). Your project may not work properly until       
       you apply the migrations for app(s): admin, auth, contenttypes, sessions.

       Run 'python manage.py migrate' to apply them.
       June 24, 2021 - 11:40:50
       Django version 3.1, using settings 'config.settings'
       Starting development server at http://127.0.0.1:8000/
       Quit the server with CTRL-BREAK.

        modified:   readme.md


### 4. DATABASE

#### 4.1 Membuat postgres database

		λ psql
		psql (13.0)
		WARNING: Console code page (437) differs from Windows code page (1252)
		         8-bit characters might not work correctly. See psql reference
		         page "Notes for Windows users" for details.
		Type "help" for help.

		hp=# CREATE DATABASE django_code4startup_fastparcel_psql;
		CREATE DATABASE
		hp=#

        modified:   readme.md

#### 4.2 Install django-environ 

        (venv3931) λ pip install django-environ
        Collecting django-environ
        Using cached django_environ-0.4.5-py2.py3-none-any.whl (21 kB)
        Installing collected packages: django-environ
        Successfully installed django-environ-0.4.5

        NOTE:
        .Django-environ memungkinkan Anda menggunakan variabel lingkungan yang diilham 12faktor untuk mengonfigurasi aplikasi Django Anda.

        modified:   readme.md

#### 4.3 Initialisasi environ pada django proyek config/settings.py

        modified:   config/settings.py
        modified:   readme.md

#### 4.4 Membuat .env file di dalam django proyek 'config/.env' 

        new file:   config/.env
        modified:   readme.md

#### 4.5 Membubuhkan SECRET_KEY django proyek dan kredensial database pada .env file 

        modified:   .gitignore
        modified:   config/.env
        modified:   readme.md

#### 4.6 Mengkoneksi proyek dgn database berdasarkan kredensial pada .env file 

        (venv3931) λ python -m pip install psycopg2
        modified:   config/settings.py
        modified:   readme.md

#### 4.7 Jalankan ulang server untuk menguji

        (venv3931) λ python manage.py runserver
        Watching for file changes with StatReloader
        Performing system checks...

        System check identified no issues (0 silenced).

        You have 18 unapplied migration(s). Your project may not work properly until       
        you apply the migrations for app(s): admin, auth, contenttypes, sessions.

        Run 'python manage.py migrate' to apply them.
        June 24, 2021 - 12:13:56
        Django version 3.1, using settings 'config.settings'
        Starting development server at http://127.0.0.1:8000/
        Quit the server with CTRL-BREAK.

        modified:   readme.md


### 5. DJANGO ADMIN

#### 5.1 Mengaplikasikan default django apps pada database untuk membuat tabel-tabel

       (venv3931) λ python manage.py makemigrations
       No changes detected

       E:\workspace\django\Code4Startup\django_code4startup_fastparcel_psql (master)
       (venv3931) λ python manage.py migrate
       Operations to perform:
       Apply all migrations: admin, auth, contenttypes, sessions
       Running migrations:
       Applying contenttypes.0001_initial... OK
       Applying auth.0001_initial... OK
       ...
       Applying sessions.0001_initial... OK

       modified:   readme.md

#### 5.2 Membuat superuser

        (venv3931) λ python manage.py createsuperuser
        Username (leave blank to use 'hp'): ing
        Email address: ingafter60@outlook.com
        Password:
        Password (again):
        The password is too similar to the username.
        This password is too short. It must contain at least 8 characters.
        Bypass password validation and create user anyway? [y/N]: y
        Superuser created successfully.

        modified:   readme.md

#### 5.3 Modifikasi readme.md file

#### 5.4 Re-modifikasi readme.md file


### 6. MVT: MODEL, VIEW, TEMPLATE + URL

#### 6.1 Membuat Home Page Part 1/3: Membuat view function (controller and method or action)

        modified:   apps/core/views.py
        modified:   readme.md

#### 6.2 Membuat Home Page Part 2/3: Membuat path atu route untuk Home Page

        modified:   config/urls.py
        modified:   readme.md

#### 6.3 Membuat Home Page Part 3/3: Membuat Home Page template

        new file:   apps/core/templates/core/home.html
        modified:   readme.md

#### 6.4 Menginstall django-bootstrap

		(venv3931) λ python -m pip install django-bootstrap4==2.3.1
		...
		django-bootstrap4-2.3.1 soupsieve-2.2.1

#### 6.5 Meregistrasi bootstrap4 pada proyek 'core/settings.py'

        modified:   config/settings.py
        modified:   readme.md

#### 6.6 Home Page: Membuat navbar dan footer

        modified:   apps/core/templates/core/home.html
        modified:   readme.md

#### 6.7 Home Page: Membuat card untuk Customer dan Courier

        modified:   apps/core/templates/core/home.html
        modified:   readme.md

#### 6.8 Membuat view function dan path untuk halaman Customer dan Courier

        modified:   apps/core/views.py
        modified:   config/urls.py
        modified:   readme.md 

#### 6.9 Modifikasi Home page dgn menggunakan template inheritance

        new file:   apps/core/templates/base.html
        modified:   apps/core/templates/core/home.html
        modified:   readme.md


### 7. GIT

#### 7.1 Buat requirements.txt file dan modifikasi file .gitignore

        (venv3931) λ pip freeze > requirements.txt
        modified:   .gitignore
        modified:   readme.md
        new file:   requirements.txt 

#### 7.2 Log In form Part 1/4: Display default login form variable from LoginView

        new file:   apps/core/templates/registration/sign_in.html
        modified:   config/urls.py
        modified:   readme.md

#### 7.3 Log In form Part 2/4: Menngunakan bootstrap untuk login form dan didasarkan pada form variable

        modified:   apps/core/templates/registration/sign_in.html
        modified:   readme.md

#### 7.4 Log In form Part 3/4: Menambahkan kondisional untuk menampilkan form Customer atau Courier

        modified:   apps/core/templates/registration/sign_in.html
        modified:   readme.md

#### 7.5 Log In form Part 4/4: Kustomisasi login form dgn menampilkan email field dan bukan username yg default dalam django

        modified:   apps/core/templates/registration/sign_in.html
        modified:   readme.md

#### 7.6 Redirect user to Home Page after logged in

        modified:   config/settings.py
        modified:   readme.md

#### 7.7 Membuat dan menampilkan Sign Out menu pada navbar

        modified:   apps/core/templates/base.html
        modified:   readme.md


#### 7.8 Menampilkan menu Customer dan Courier jika user tidak log in atau jika user logged out dan modifiksi path


        modified:   apps/core/templates/base.html
        modified:   config/urls.py
        modified:   readme.md

#### 7.9 Membatasi akses user untuk masuk ke halaman tertentu

        modified:   apps/core/views.py
        modified:   readme.md

        NOTE:

        .Setiap User hrs login untuk bisa mengakses halaman
         Customer atau Courier.
        .Jika user login sbg customer, maka stlh login ia
         akan ditampilkan halaman customer.
        .Jika user login sbg courier, maka stlh login ia
         akan ditampilkan halaman courier. 