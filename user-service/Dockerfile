FROM python:3.9-slim-bullseye
  
WORKDIR /app

COPY ./api/requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r /app/requirements.txt

COPY ./api /app/api

ENV PYTHONPATH=/app

EXPOSE 8010

VOLUME /app/api/products.db

#CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8010"]
CMD ["python", "api/main.py"]
