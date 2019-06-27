
FROM python:3.6.8-alpine3.8
COPY requirements.txt /src/requirements.txt
RUN pip install -r /src/requirements.txt
COPY app.py /src
COPY meaning.py /src
COPY test_meaning.py /src
CMD python /src/app.py
