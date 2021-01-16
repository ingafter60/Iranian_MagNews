# Iranian_MagNews
Building Django Magazine News
https://github.com/ingafter60/Iranian_MagNews

## SECTION 01 - Basic setup

### 01.1.1 - Create remote (Github) repository

        modified:   .gitignore
        modified:   LICENSE
        modified:   README.md
        new file:   manage.py

### 01.2.2 - Create django project 'myproject' 

        modified:   .gitignore
        modified:   README.md
        new file:   myproject/__init__.py
        new file:   myproject/settings.py
        new file:   myproject/urls.py
        new file:   myproject/wsgi.py

## SECTION 02 - Hellow world

### 02.1.3 - Create django app 'main'

        modified:   README.md
        new file:   main/__init__.py
        new file:   main/admin.py
        new file:   main/apps.py
        new file:   main/migrations/__init__.py
        new file:   main/models.py
        new file:   main/tests.py
        new file:   main/views.py

### 02.2.4 - Using templates, views, urls and settings to render Hello World 

        modified:   README.md
        new file:   main/templates/main/home.html
        new file:   main/urls.py
        modified:   main/views.py
        modified:   myproject/settings.py
        modified:   myproject/urls.py

## SECTION 03 - HTML Template and Static files

### 03.1.5 - Add Static files and its root path

        modified:   README.md
        new file:   main/static/front/IMG_Previews/01_HomePage_v1.jpg
        new file:   main/static/front/IMG_Previews/02_HomePage_v2.jpg
        ...
        new file:   main/static/front/IMG_Previews/03_HomePage_v3.jpg
        modified:   myproject/settings.py

### 03.2.6 - Add Html template for the home page and load static files

        modified:   README.md
        modified:   main/templates/main/home.html 


### 03.3.7 - Create about page

        modified:   .gitignore
        modified:   README.md
        new file:   main/templates/main/front/about.html
        renamed:    main/templates/main/home.html -> main/templates/main/front/home.html
        modified:   main/urls.py
        modified:   main/views.py

### 03.4.8 - Using template inheritance to render pages 

        modified:   .gitignore
        modified:   README.md
        modified:   main/templates/main/front/about.html
        modified:   main/templates/main/front/home.html
        new file:   main/templates/main/front/master.html


## SECTION 04 - Site setting


### 04.1.9 - Template Partials and Link Address

        modified:   README.md
        modified:   main/templates/main/front/master.html
        new file:   main/templates/main/front/partials/footer/footer.html
        new file:   main/templates/main/front/partials/head/head.html
        new file:   main/templates/main/front/partials/header/logo.html
        new file:   main/templates/main/front/partials/header/main-menu.html
        new file:   main/templates/main/front/partials/header/topbar.html
        
### 04.2.10 - Setup MySQL DB and creat Main model

        modified:   README.md
        modified:   main/admin.py
        new file:   main/migrations/0001_initial.py
        modified:   main/models.py
        modified:   myproject/settings.py

### 04.3.11 - Add static page title

        modified:   README.md
        modified:   main/models.py
        modified:   main/templates/main/front/partials/head/head.html
        modified:   main/views.py

### 04.4.12 - Show Data In Template (Dynamic page title)

        modified:   README.md
        modified:   main/templates/main/front/partials/footer/footer.html
        modified:   main/templates/main/front/partials/head/head.html
        modified:   main/views.py

### 04.5.13 - Add Title To Page

### 04.6.14 - Cofigure model for site settings + (04.5.13 - Add Title To Page)

        modified:   main/migrations/0001_initial.py
        modified:   main/models.py
        modified:   main/templates/main/front/about.html
        modified:   main/templates/main/front/home.html
        modified:   main/templates/main/front/master.html
        modified:   main/templates/main/front/partials/head/head.html
        modified:   main/views.py

### 04.7.15 - Add social networks

        modified:   README.md
        new file:   main/migrations/0002_auto_20210116_2015.py
        modified:   main/models.py
        modified:   main/templates/main/front/partials/footer/footer.html
        modified:   main/templates/main/front/partials/header/topbar.html
        
### 04.8.16 - Other site settings

        modified:   README.md
        modified:   main/templates/main/front/about.html
        modified:   main/templates/main/front/home.html
        modified:   main/templates/main/front/master.html
        modified:   main/templates/main/front/partials/footer/footer.html


## SECTION 05 - App News

### 05.1.17 - Create app 'news', News model and register the app

        modified:   README.md
        new file:   main/migrations/0003_auto_20210116_2133.py
        modified:   main/templates/main/front/home.html
        modified:   myproject/settings.py
        modified:   myproject/urls.py
        new file:   news/__init__.py
        new file:   news/admin.py
        new file:   news/apps.py
        new file:   news/migrations/0001_initial.py
        new file:   news/migrations/__init__.py
        new file:   news/models.py
        new file:   news/tests.py
        new file:   news/urls.py
        new file:   news/views.py

### 05.2.18 - Rendering news to template using for loop

        modified:   README.md
        modified:   main/templates/main/front/home.html
        modified:   main/views.py
        modified:   news/admin.py
        modified:   news/models.py


### 05.3.19 - Detail news render without key/id/pk

        modified:   README.md
        modified:   main/templates/main/front/home.html
        new file:   main/templates/main/front/news_detail.html
        modified:   main/urls.py
        modified:   main/views.py
        modified:   news/urls.py
        modified:   news/views.py












































































































