# Используйте официальный образ Python в качестве базового образа
FROM python:3.11

# Установите переменную окружения PYTHONUNBUFFERED для предотвращения буферизации вывода
ENV PYTHONUNBUFFERED 1

# Установите рабочий каталог внутри контейнера
WORKDIR /app

# Скопируйте файл зависимостей и установите их
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Скопируйте весь текущий каталог внутрь контейнера
COPY . /app/

# Выполните миграции и соберите статические файлы Django
RUN python manage.py migrate
RUN python manage.py collectstatic --noinput

# Укажите порт, который будет слушаться контейнером
EXPOSE 8000

# Запустите Django приложение при запуске контейнера
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]