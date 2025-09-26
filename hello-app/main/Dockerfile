FROM python:3.14.0rc3-alpine3.22
WORKDIR /app
COPY requirements.txt .
RUN  apk install --no-cache-dir -r requirements.txt
COPY . .

EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
