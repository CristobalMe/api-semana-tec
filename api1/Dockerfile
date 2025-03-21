FROM python:3.9-slim-buster

WORKDIR /app

COPY api1/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY api1 .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "3750"]