FROM python:3.8-slim-buster
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
# Expose port 8000 to the outside world
EXPOSE 8000
# Define environment variable
ENV PORT=8000
CMD ["python", "app.py", "--host", "0.0.0.0:5000"]
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "wsgi:app"]
