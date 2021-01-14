FROM python:3
WORKDIR /app
COPY . ./
EXPOSE 3333
ENTRYPOINT [ "python", "./test_suite.py"]