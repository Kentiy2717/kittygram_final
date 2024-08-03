### Контейнеры и CI/CD для Kittygram
Работа выполнен в рамках обучения на курсе "Python разработчик буткемп" Яндекс Практикума. Настройка автодеплоя на сервер в Docker.

![example workflow](https://github.com/Kentiy2717/kittygram_final/actions/workflows/main.yml/badge.svg)

Ивент

![example event parameter](https://github.com/Kentiy2717/kittygram_final/actions/workflows/main.yml/badge.svg?event=push)

Бранч

![example branch parameter](https://github.com/Kentiy2717/kittygram_final/actions/workflows/main.yml/badge.svg?branch=badge)

Август 2024.

### Технологии

Python, Django, Pytest, Flake8, Docker

### Команда проекта

Исполнитель:

Иннокентий Мотрий (https://github.com/Kentiy2717).

Наставники:

Ритис Бараускас, Николай Минякин. 

Ревьюер:

Евгений Салахутдинов.

### Как запустить проект

Проект "Tasky" - доступен по адресу https://sherrycask.zapto.org
Проект "Kittygram" - доступен по адресу https://sherrycask.mooo.com

#  Как работать с репозиторием финального задания

## Что нужно сделать

Настроить запуск проекта Kittygram в контейнерах и CI/CD с помощью GitHub Actions

## Как проверить работу с помощью автотестов

В корне репозитория создайте файл tests.yml со следующим содержимым:
```yaml
repo_owner: ваш_логин_на_гитхабе
kittygram_domain: полная ссылка (https://доменное_имя) на ваш проект Kittygram
taski_domain: полная ссылка (https://доменное_имя) на ваш проект Taski
dockerhub_username: ваш_логин_на_докерхабе
```

Скопируйте содержимое файла `.github/workflows/main.yml` в файл `kittygram_workflow.yml` в корневой директории проекта.

Для локального запуска тестов создайте виртуальное окружение, установите в него зависимости из backend/requirements.txt и запустите в корневой директории проекта `pytest`.

## Чек-лист для проверки перед отправкой задания

- Проект Taski доступен по доменному имени, указанному в `tests.yml`.
- Проект Kittygram доступен по доменному имени, указанному в `tests.yml`.
- Пуш в ветку main запускает тестирование и деплой Kittygram, а после успешного деплоя вам приходит сообщение в телеграм.
- В корне проекта есть файл `kittygram_workflow.yml`.