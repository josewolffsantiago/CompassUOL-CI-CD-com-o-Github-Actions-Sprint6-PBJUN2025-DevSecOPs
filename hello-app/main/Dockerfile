FROM python:3.14.0rc3-alpine3.22

WORKDIR /app

RUN apk add --no-cache gcc musl-dev python3-dev

RUN pip install "fastapi[standard]" uvicorn

COPY . .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
