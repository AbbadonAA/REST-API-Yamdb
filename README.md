# REST API Yamdb

![Yamdb workflow](https://github.com/AbbadonAA/yamdb_final/actions/workflows/Yamdb_workflow/badge.svg)

## Описание

API для проекта Yamdb, позволяющий регистрироваться, просматривать описания произведений, читать и публиковать отзывы и комментарии к ним.

API доступен по адресу: http://localhost/api/v1/

## Технологии
- Python 3.8.10
- Django 3.0.0
- Django REST Framework
- Docker
- PostgreSQL
- WSL2 / Ubuntu-20.04

## Документация к API
После установки доступна по адресу: http://localhost/redoc/

## Инструкция по установке и запуску в контейнерах
1. Клонируйте репозиторий:
```
git clone git@github.com:AbbadonAA/infra_sp2.git
```
2. Установите и активируйте виртуальной окружение:
```
python3 -m venv venv
source venv/bin/activate ИЛИ source venv/Scripts/activate
```
3. Установите зависимости:

Файл requirements.txt находится по адресу: /infra_sp2/api_yamdb/requirements.txt
```
pip install -r requirements.txt
```
4. Создайте файл .env в директории nginx со следующим наполнением:
```
SECRET_KEY=<УКАЖИТЕ КЛЮЧ>
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=<ЗАДАЙТЕ СВОЙ ПАРОЛЬ>
DB_HOST=db
DB_PORT=5432
```
5. Запустите docker-compose:
```
docker-compose up -d
```
6. Выполните миграции, подключите статику:
```
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py collectstatic --no-input
```
7. Проект уже запущен по адресу: http://localhost/
8. Для заполнения базы тестовыми данными, выполните команду (не обязательно):
```
docker-compose exec web python manage.py loaddata fixtures.json
```
9. Создайте суперпользователя:
```
docker-compose exec web python manage.py createsuperuser
```
10. Для остановки работы контейнеров выполните команду:
```
docker-compose down -v
```
## Образ Yamdb на DockerHub
Может быть скачан из репозитория:
```
docker pull abbadon666666/yamdb:v2
```

## Лицензия
- ### **MIT License**

### Автор
Pushkarev Anton

pushkarevantona@gmail.com