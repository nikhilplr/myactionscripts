FROM python:3.11-slim

WORKDIR /app

COPY entrypoint.py .
COPY requirements.txt .

#RUN pip install --no-cache-dir -r requirements.txt
RUN pip3 install openai==0.28

ENTRYPOINT ["python", "/app/entrypoint.py"]
