aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 574284216851.dkr.ecr.us-east-1.amazonaws.com
docker build -t foodieflow .
docker tag foodieflow:latest 574284216851.dkr.ecr.us-east-1.amazonaws.com/foodieflow:latest
docker push 574284216851.dkr.ecr.us-east-1.amazonaws.com/foodieflow:latest