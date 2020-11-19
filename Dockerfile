FROM python:3.8-alpine
RUN mkdir -p /var/app
WORKDIR /var/app/
RUN pip install Flask==1.1.1

EXPOSE 5000
CMD ["python", "server.py"]