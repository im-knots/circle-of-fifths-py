FROM python:3.9

WORKDIR /usr/src/reprocess
COPY requirements.txt ./
# RUN pip install uwsgi
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python3", "-u", "./app.py"]
