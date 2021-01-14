FROM python:3
COPY . .
RUN ls
EXPOSE 3333
ENTRYPOINT [ "python", "./test_suite.py"]