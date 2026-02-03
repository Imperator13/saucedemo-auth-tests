FROM python:3.10-slim

WORKDIR /app

# Установка системных зависимостей
RUN apt-get update && apt-get install -y \
    wget \
    gnupg \
    unzip \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Установка Chrome
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list \
    && apt-get update && apt-get install -y google-chrome-stable

# Копирование файлов проекта
COPY requirements.txt .
COPY pytest.ini .
COPY conftest.py .
COPY src ./src

# Установка Python зависимостей
RUN pip install --no-cache-dir -r requirements.txt

# Создание директории для отчетов
RUN mkdir -p /app/allure-results /app/screenshots

# Команда запуска тестов
CMD ["pytest", "--headless", "--alluredir=./allure-results"]