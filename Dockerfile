FROM python:3.4-alpine
WORKDIR /code
ADD . /code
RUN pip install -r requirements.txt
CMD ["python", "myapp.py"]
