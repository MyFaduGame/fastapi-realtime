FROM python:3.10-slim-buster
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY ./requirement.txt .
COPY . /app/
RUN apt-get update
RUN pip install --no-cache-dir -r ./requirement.txt
EXPOSE 8000
CMD ["uvicorn","--host","0.0.0.0","--port","8000","src.main:app"]