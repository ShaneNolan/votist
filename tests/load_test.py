from locust import HttpUser, TaskSet, task, between

class FraudPredictTask(TaskSet):
    @task
    def predict(self):
        request_body = {
            "amount": 111111111111111110,
            "lat": 1230,
            "long": 1230,
            "merch_lat": 1110,
            "merchant_long": 111,
            "age": 22,
            "category": "entertainment",
        }
        self.client.post('/predict', json=request_body)



class IrisLoadTest(HttpUser):
    tasks = [FraudPredictTask]
    host = 'http://127.0.0.1'
    stop_timeout = 20
    wait_time = between(1, 5)