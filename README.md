# diabete_ml
repository for diabetes prediction in machine learning

# Docker

# BUILD
docker build --tag [image_name]:[tag]
    # example
    build: `sudo docker build --tag flask-diabete-predict:1.0`
# Dockerfile
- When installed this image, and build it, you can run it with:
- docker run -p [host_port]:8000 [docker_image]
- once run, in navigator use: "http://[ip_host]:[host_port]/[predict_one] or [predict_many]


