FROM python:3.9-slim
ENV PYTHONUNBUFFERED=1

# --- ДОБАВЛЯЕМ ЭТУ СТРОКУ: ---
RUN pip install redis
# -----------------------------

WORKDIR /app
COPY main.py .
EXPOSE 8000
CMD ["python", "main.py"]
