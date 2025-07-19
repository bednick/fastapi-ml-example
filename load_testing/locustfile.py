import locust

BATCH = 1

with open(f"request_{BATCH}.json", "r", encoding="utf-8") as fp:
    data = fp.read()


class FastapiMlExampleUser(locust.HttpUser):
    wait_time = locust.constant(1)

    @locust.task
    def predict(self):
        self.client.post(
            "/predict",
            data=data,
            headers={"Content-Type": "application/json; charset=utf-8"},
        )
