from locust import HttpUser, constant , task, SequentialTaskSet
import json
import random

class LoadResTest(SequentialTaskSet):
    @task
    def list_breeds(self):
        response = self.client.get("/breeds/list/all")
        print("List Breeds - Get Method status is", response.status_code)
        assert response.status_code == 200, "Unexpected response code" + response.status_code

        random_bread = response.json()['message']
        random_breeds_list = (random.choice(list(random_bread)))
        print(random_breeds_list)
        response_random = self.client.get("/breed/{}/images/random".format(random_breeds_list))
        print("Random image - Get Method status is", response_random.status_code)
        assert response_random.status_code == 200, "Unexpected response code" + response_random.status_code


    @task
    def random_image(self):
        response = self.client.get("/breeds/image/random")
        print("Random image - Get Method status is", response.status_code)
        assert response.status_code == 200, "Unexpected response code" + response.status_code


class LoadSeqTest(HttpUser):
    wait_time = constant(1)
    host = "https://dog.ceo/api"
    tasks = [LoadResTest]




#locust -f locust_load_test.py -u 1 -r 1 -t 10s --headless --print-stats --host=https://dog.ceo/api -L DEBUG --logfile demo_report.log --html dilip.html