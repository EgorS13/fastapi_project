# Руководство по запуску

## Требования
- Python 3.7+
- pip (менеджер пакетов Python)
- Виртуальное окружение (рекомендуется)

## 1. Клонирование репозитория
git clone https://github.com/EgorS13/fastapi_project.git

## 2. Настройка виртуального окружения
### Для Windows:
python -m venv venv
venv\Scripts\activate

## 3. Установка зависимостей
pip install -r requirements.txt

## 4. Запуск сервера
uvicorn app:app --reload

Сервер будет доступен по адресу:  
http://127.0.0.1:8000
А OpenAPI спецификация:
http://127.0.0.1:8000/openapi.json

## 5. Тестирование
### Запуск тестов с генерацией отчета:
Необходимо открыть второй терминал и запустить:
pytest --maxfail=5 --disable-warnings --html=report.html -v
