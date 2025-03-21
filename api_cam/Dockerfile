FROM python:3.9-slim-buster

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY api_cam.py .

CMD ["uvicorn", "api_cam:app", "--host", "0.0.0.0", "--port", "3751"]