FROM python:3.12.4-slim-bullseye

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir -r base-requirements.txt

RUN pip install --no-cache-dir -r extra-requirements.txt

COPY . .

CMD ["fastapi", "run", "src/main.py", "--host", "0.0.0.0", "--port", "8000"]
