FROM python:3.6
WORKDIR /app
RUN pip install kafka
COPY consumer.py ./
CMD ["python", "consumer.py"]
