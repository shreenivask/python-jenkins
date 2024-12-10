FROM python:3.12-slim
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir --break-system-packages -r requirements.txt
EXPOSE 8000
ENV PORT=8000
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "app:app"]
