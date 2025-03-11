docker buildx create --name flask_demo --driver docker-container --use
docker buildx build –t flask_demo/1.0 –f Dockerfile --load .
docker run -it --name flask_demo --gpus all --restart always –v /backup/msyang/flask_demo:/workspace –p 5000:5000 flask_demo/1.0