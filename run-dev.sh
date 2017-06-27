gulp build
docker build -t rroslund/lilpebbles .
docker stop lilpebbles
docker rm lilpebbles
docker run -it -p 8000:8000 -v c:/code/lilpebbles/src:/app/src --name lilpebbles rroslund/lilpebbles:latest
