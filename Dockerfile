# syntax=docker/dockerfile:1

# format: [image]:[tag]
FROM python:latest

#This instructs Docker to use this path as the default location for all subsequent commands.
WORKDIR /app

#We copy our requirements.txt into /app directory ([WORKDIR]/requirements.txt)
COPY requirements.txt requirements.txt

#We install our packages requires ([WORKDIR]/requirements.txt) in the docker images we want to build
RUN pip3 install -r requirements.txt

#add our source code into the image
COPY . .

#command to run when our image run
CMD [ "python3", "app.py"]


#BUILD
#docker build --tag [image_name]

#When installed this image, and build it, you can run it with:
#docker run --p [host_port]:8000 [docker_image]
# once run, in navigator use: "http://[ip_host]:[host_port]/[predict_one] or [predict_many]