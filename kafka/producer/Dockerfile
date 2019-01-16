FROM python:3.6
WORKDIR /app
RUN pip install kafka
COPY producer.py ./
COPY urls.json ./
CMD ["python", "producer.py"]
