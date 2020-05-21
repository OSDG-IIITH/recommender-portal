FROM python:3.7-alpine
LABEL author=pk13055 version=1.0

RUN pip3 install pip-tools \
    && apk add --update build-base \ 
    libxml2-dev libxslt-dev \
    && rm -rf /var/cache/apk/*

WORKDIR /app
COPY requirements.in  .
RUN pip-compile requirements.in > requirements.txt \
    && pip3 install -r requirements.txt


COPY . /app
EXPOSE 5000
ENTRYPOINT ["uvicorn", "--host", "0.0.0.0", "--port", "5000", "--reload", "main:app"]

