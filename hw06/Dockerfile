FROM python:3.8-slim-buster

WORKDIR /hw06

COPY requirements.txt requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 5000

# Default command (optional, change as needed) 
CMD ["python3", "routes.py"]
