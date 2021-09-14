class Trainer:
    TRAINER_ID = 0

    def __init__(self, name):
        Trainer.TRAINER_ID += 1
        self.name = name
        self.id = Trainer.TRAINER_ID

    def __repr__(self):
        return f"Trainer <{self.id}> {self.name}"

    @staticmethod
    def get_next_id():
        return Trainer.TRAINER_ID + 1

