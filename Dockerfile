# see https://devcenter.heroku.com/articles/container-registry-and-runtime
#Grab the latest alpine image
FROM python:3.9

# Install python and pip
ADD ./requirements.txt /tmp/requirements.txt

# Install dependencies
RUN pip install --no-cache-dir -r /tmp/requirements.txt

# Add our code
ADD ./app /opt/app/
WORKDIR /opt/app

# Expose is NOT supported by Heroku
# EXPOSE 5000
#
## Run the image as a non-root user
#RUN adduser -D myuser
#USER myuser

# Run the app.  CMD is required to run on Heroku
# $PORT is set by Heroku
CMD gunicorn --bind 0.0.0.0:$PORT wsgi
#
#CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]