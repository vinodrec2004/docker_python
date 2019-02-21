FROM python:3.4-alpine
WORKDIR /code
ADD . /code
RUN pip install -r requirements.txt
EXPOSE 80
CMD ["python", "myapp.py"]
