# Автоматизация тестирования авторизации на SauceDemo

Проект содержит автоматизированные тесты для проверки функционала авторизации на сайте [SauceDemo](https://www.saucedemo.com/).

## Структура проекта

- `src/pages/` - Page Object
- `src/tests/` - тестовые сценарии
- `conftest.py` - фикстуры Pytest
- `requirements.txt` - требуемые зависимости Python
- `Dockerfile` - конфигурация Docker
- `docker-compose.yml` - конфигурация Docker Compose

## Установка и запуск

### Локальная установка

1. Клонировать репозиторий:
```bash
git clone <repository-url>
cd saucedemo-auth-tests
```

2. Установить зависимости:

```bash
pip install -r requirements.txt
```

Запустить тесты:

bash
# Запуск всех тестов
pytest

# Запуск с генерацией отчета Allure
pytest --alluredir=./allure-results

# Просмотр отчета Allure
allure serve allure-results
Запуск в Docker
Собрать и запустить контейнер:

bash
docker-compose up --build
После выполнения тестов отчеты будут доступны в директории allure-results

Для просмотра отчета:

bash
allure serve allure-results
Тестовые сценарии
Успешный логин - проверка входа с валидными учетными данными

Логин с неверным паролем - проверка обработки неверного пароля

Логин заблокированного пользователя - проверка блокировки пользователя

Логин с пустыми полями - проверка валидации пустых полей

Логин пользователем performance_glitch_user - проверка работы при возможных задержках

Тестовые пользователи
standard_user / secret_sauce

locked_out_user / secret_sauce

problem_user / secret_sauce

performance_glitch_user / secret_sauce

Генерация отчетов
Для генерации отчетов Allure:

bash
# Генерация HTML отчета
allure generate allure-results -o allure-report --clean

# Открытие отчета в браузере
allure open allure-report
Запуск в headless режиме
bash
pytest --headless
Запуск конкретного теста
bash
pytest src/tests/test_login.py::TestLogin::test_successful_login
Лицензия
MIT

text

## Инструкция по запуску

### Быстрый старт:

1. **Клонировать проект и установить зависимости:**
```bash
git clone <repository-url>
cd saucedemo-auth-tests
pip install -r requirements.txt
Запустить тесты локально:

bash
pytest --alluredir=./allure-results
Просмотреть отчет:

bash
allure serve allure-results
Запуск в Docker:
Собрать и запустить:

bash
docker-compose up --build
После выполнения тестов просмотреть отчет:

bash
allure serve allure-results
Особенности реализации:
Page Object Pattern - каждая страница представлена отдельным классом

Allure отчеты - детальные шаги и скриншоты при падениях

Docker поддержка - возможность запуска в изолированном окружении

Ожидания - использование явных ожиданий для стабильности тестов

Модульность - легко добавлять новые тесты и страницы