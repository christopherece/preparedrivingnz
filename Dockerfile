FROM python:3.9

# Install PostgreSQL client libraries
RUN apt-get update && apt-get install -y libpq-dev

WORKDIR /home/meztroinhinyero/django/trafficquizapp

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV DATABASE_HOST=192.168.10.225

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
