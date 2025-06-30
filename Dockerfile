# ✅ Используем минимальный образ Python 3.11
FROM python:3.11-slim

# 🛠 Устанавливаем ffmpeg и его зависимости
RUN apt-get update && apt-get install -y ffmpeg && apt-get clean

# 🗂 Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# 📥 Копируем весь код проекта в контейнер
COPY . .

# 📦 Устанавливаем Python-зависимости
RUN pip install --no-cache-dir -r requirements.txt

# ▶️ Указываем команду запуска
CMD ["python", "main.py"]

