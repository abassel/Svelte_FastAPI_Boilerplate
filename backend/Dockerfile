#   TO EXECUTE THIS DOCKERFILE:

#   container_name=backend
#   img_name=backend_img
#   docker build -t ${img_name} .
#   docker run  --name ${container_name} -p 8000:8000 -d --rm ${img_name}               # To run this container

#   docker logs ${container_name}                                                       # Get output logs
#   docker run -it ${container_name} bash                                               # To inspect before running
#   docker exec -it ${container_name} bash                                              # To inspect while running

#   docker system prune --all --force                                                   # Docker clearup

FROM python:3.11.7-bookworm

# copy project requirement files here to ensure they will be cached.
WORKDIR /opt/app
COPY requirements.lock.txt ./

RUN pip install -r requirements.lock.txt

COPY ./  ./

EXPOSE 8000

ENTRYPOINT ["uvicorn", "--host", "0.0.0.0", "--port", "8000", "src.main:app"]
