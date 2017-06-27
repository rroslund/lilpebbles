aws ecr get-login --no-include-email --region us-east-1 --profile rich >> login-ecr.sh
login-ecr.sh
rm login-ecr.sh
docker build -t lilpebbles .
docker tag lilpebbles:latest 017510324046.dkr.ecr.us-east-1.amazonaws.com/lilpebbles:latest
docker push 017510324046.dkr.ecr.us-east-1.amazonaws.com/lilpebbles:latest
