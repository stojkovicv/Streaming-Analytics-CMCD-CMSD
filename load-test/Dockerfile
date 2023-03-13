FROM python:3.9

WORKDIR /usr/src/load-test

RUN pip install locust

COPY . .

EXPOSE 8089
CMD ["locust", "-f", "locust.py", "--host=http://cmcd-server:8080"]
