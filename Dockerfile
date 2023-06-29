# Используем базовый образ Python
FROM python:3.11

# Устанавливаем переменные окружения
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /usr/src/app

# Копируем файлы зависимостей в контейнер
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install -r requirements.txt

# Копируем остальные файлы проекта в контейнер
COPY . .


RUN python manage.py migrate


# Открываем порт, на котором будет работать Django приложение
EXPOSE 8000

# Запускаем команду для запуска Django сервера
CMD ["python", "manage.py", "runserver"]