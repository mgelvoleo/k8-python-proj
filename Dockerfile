FROM python:3.10.6-alpine

WORKDIR /app
COPY . .

RUN pip install -r requirements.txt

# Expose port 5000 for your Flask application
EXPOSE 5000

ENTRYPOINT ["python"]
CMD ["app.py"]
