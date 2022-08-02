# REST API Yamdb

![Yamdb_workflow](https://github.com/AbbadonAA/yamdb_final/workflows/Yamdb_workflow/badge.svg)

## Описание

Учебный групповой проект по созданию API для сервиса по сбору отзывов пользователей на произведения.

Пользователи имеют возможность зарегистрироваться, пройти аутентификацию, добавлять отзывы, оценивать произведения и оставлять комментарии к отзывам.

Прозведение должно быть отнесено к определенной категории. А каждому произведению, в свою очередь, присваиваются определенные жанры. 

В проекте настроен CI/CD – при пуше в master обновляются контейнеры Docker, и происходит деплой новой версии на сервер.


## Стек технологий
- Python
- Django
- Django REST Framework
- PostgreSQL
- Docker
- Github Actions

## Документация к API
 - После запуска доступна по адресу: http://<ip-адрес>/redoc/

## Для запуска на собственном сервере:
1. Скопируйте из репозитория файлы, расположенные в директории infra:
    - docker-compose.yml
    - nginx.conf
2. На сервере создайте директорию yamdb;
3. В директории yamdb создайте директорию infra и поместите в неё файлы:
    - docker-compose.yml
    - default.conf
    - .env (пустой)
4. Файл .env должен быть заполнен следующими данными:
```
SECRET_KEY=<КЛЮЧ>
DB_ENGINE=django.db.backends.postgresql
DB_NAME=<ИМЯ БАЗЫ ДАННЫХ>
POSTGRES_USER=<ИМЯ ЮЗЕРА БД>
POSTGRES_PASSWORD=<ПАРОЛЬ БД>
DB_HOST=db
DB_PORT=5432
```
5. В директории infra следует выполнить команды:
```
docker-compose up -d
docker-compose exec backend python manage.py makemigrations
docker-compose exec backend python manage.py migrate
docker-compose exec backend python manage.py collectstatic --no-input
```

6. Для создания суперпользователя выполните команду:
```
docker-compose exec backend python manage.py createsuperuser
```

7. Проект запущен со следующими доступными эндпоинтами:
    - http://<ip-адрес>/redoc/ - документация с подробным описанием всех возможностей API и всех эндпоинтов
    Остальные эндпоинты предпочтительно просматривать с использованием Postman:
    - http://<ip-адрес>/api/v1/auth/signup/ - регистрация
    - http://<ip-адрес>/api/v1/auth/token/ - получение JWT-токена
    - http://<ip-адрес>/api/v1/categories/ - получение списка доступных категорий
    - http://<ip-адрес>/api/v1/genres/ - получение списка доступных жанров
    - http://<ip-адрес>/api/v1/titles/ - получение списка доступных произведений
    - http://<ip-адрес>/api/v1/titles/{title_id}/reviews/ - получение списка отзывов к произведению
    и др.


## Лицензия
- ### **MIT License**

### Автор
Pushkarev Anton

pushkarevantona@gmail.com
