# Votist

An API using FastAPI to screen transactions for fraud.

# Install

```
docker build -t votist . && docker run -p 80:80 --name=votist_container votist
```

# Performance Testing

# Docker Commands

`docker network create --driver bridge locustnw`
`docker build -t votist . && docker run -p 80:80 --network=locustnw --name=votist_container votist`
`docker rm votist_container -f && docker build -t votist . && docker run -p 80:80 --network=locustnw --name=votist_container votist`
`docker rm votist_locust -f && docker run -p 8089:8089 --network=locustnw --name=votist_locust -v C:\Users\Shane\votist:/mnt/locust locustio/locust -f /mnt/locust/tests/load_test.py`
`docker network inspect locustnw`
