docker build -t slack-report .
docker run --env-file .env slack-report
