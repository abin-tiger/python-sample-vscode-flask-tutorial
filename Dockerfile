# Pull a pre-built alpine docker image with nginx and python3 installed
FROM python:3.8

COPY --from=pyroscope/pyroscope:latest /usr/bin/pyroscope /usr/bin/pyroscope

# Set the port on which the app runs; make both values the same.
#
# IMPORTANT: When deploying to Azure App Service, go to the App Service on the Azure 
# portal, navigate to the Applications Settings blade, and create a setting named
# WEBSITES_PORT with a value that matches the port here (the Azure default is 80).
# You can also create a setting through the App Service Extension in VS Code.
ENV LISTEN_PORT=5000
EXPOSE 5000

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

# Set the folder where uwsgi looks for the app
WORKDIR /hello_app

# Copy the app contents to the image
COPY . /hello_app

# If you have additional requirements beyond Flask (which is included in the
# base image), generate a requirements.txt file with pip freeze and uncomment
# the next three lines.
#COPY requirements.txt /
#RUN pip install --no-cache-dir -U pip
#RUN pip install --no-cache-dir -r /requirements.txt
ENTRYPOINT ["sh", "./entrypoint.sh"]