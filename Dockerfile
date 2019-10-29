FROM python:3.6

# set work directory
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DEBUG 0

# upgrade pip
RUN pip install --upgrade pip

# install others needed libraries
RUN pip install urllib3==1.10.4 && \
  pip install requests==2.7.0 && \
  pip install pysolr==3.3.2 && \
  pip install elasticsearch==1.6.0 && \
  pip install pymongo==2.8.1 && \
  pip install mongo-connector==2.0.3

# copy requirements
COPY requirements.txt ./
# install requirements
RUN pip install -r requirements.txt

# copy everything to app dir
COPY . /app

RUN chmod 755 run_web.sh
ENTRYPOINT ["/app/run_web.sh"]
CMD ["run"]