# Тестовое задание

Необходимо написать небольшое приложение на django и django_rest_framework/django-ninja


Модели:

Category - категории объявлений, поля: name<br />
City - город объявления, поля: name<br />
Advert - объявление, поля: created (дата создания), title, description, city, category, views


Вью:

/api/advert-list/ - json список объявлений со всеми полями + название города + название категории<br />
/api/advert/\<advert-pk>\/ - json detail view одного объявления со всеми полями, просмотр данного вью увеличивает счётчик просмотров в объявлении


Завернуть проект в докер (в конфигурации для локальной разработки). БД - любая. Добавление данных через админку. 


Стоит уделить внимание производительности вашего решения. Кэширование использовать не нужно, достаточно оптимизации работы с базой данных.



🔧 Как запустить 
1. Установите Docker и Docker Compose 

Если ещё не установлено: 

    Docker 
    Docker Compose 

2. Клонируйте репозиторий:
   git clone https://github.com/bobojon97/larixon_test.git 
   cd larixon_test

3. Соберите и запустите контейнер:
   docker-compose up -d --build

4. Создайте суперпользователя:

   docker-compose exec web python manage.py createsuperuser

 Открыть в браузере 

    Админка:  http://localhost:8001/admin 
    API список объявлений:  http://localhost:8001/api/advert-list/ 
     

   
