# Backend Dockerfile for Flask
FROM python:3.10-slim
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir flask psycopg2-binary python-dotenv
EXPOSE 5000
CMD ["python", "app.py"]
