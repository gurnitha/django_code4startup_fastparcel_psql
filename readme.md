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












































































