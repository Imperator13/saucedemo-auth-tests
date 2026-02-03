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

# Запуск всех тестов
```bash
pytest
```

# Запуск с генерацией отчета Allure
```bash
pytest --alluredir=./allure-results
```

# Просмотр отчета Allure
```bash
allure serve allure-results
```

Запуск в Docker
Собрать и запустить контейнер:

```bash
docker-compose up --build
```

После выполнения тестов отчеты будут доступны в директории allure-results

Для просмотра отчета:

```bash
allure serve allure-results
```

# Тестовые сценарии
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
