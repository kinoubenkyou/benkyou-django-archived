from main.producers import Producer


class UserCreateProducer(Producer):
    TOPIC = "user-create"

    def send(self, user_id):
        self.produce(None, {"user_id": user_id})
