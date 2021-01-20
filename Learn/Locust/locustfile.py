import random
from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    wait_time = between(5, 9)

    @task
    # 只有被 @task 定义的方法才会被调用
    def index_page(self):
        self.client.get("/")  # 这里的地址需要排除 host 部分
        # self.client.get("/ibot")

    @task(3)
    # 3为权重，表示有3倍机会执行该任务
    def view_item(self):
        item_id = random.randint(1, 10000)
        self.client.get(f"/item?id={item_id}", name="/item")

    def on_start(self):
        self.client.post("/login", {"username":"foo", "password":"bar"})