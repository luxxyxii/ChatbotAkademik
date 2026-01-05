FROM python:3.10-slim

WORKDIR /app

# copy semua file ke container
COPY . /app

# install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# jalankan aplikasi
CMD ["python", "app.py"]
