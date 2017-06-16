docker build -t rroslund/lilpebbles .
docker stop lilpebbles
docker rm lilpebbles
docker run -it -p 8000:8000 --name lilpebbles rroslund/lilpebbles:latest
