FROM python:3.8-slim-buster
ENV PYTHONUNBUFFERED 1

# App setup
ADD . /corta_urls
WORKDIR /corta_urls

# Requirements installation
RUN pip install -r requirements.txt

#COPY ./entrypoint.sh /
#ENTRYPOINT ["entrypoint.sh"]
#CMD ["python manage.py runserver"]
