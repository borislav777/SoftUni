class ExercisePlan:
    EXERCISE_ID = 0

    def __init__(self, trainer_id, equipment_id, duration):
        ExercisePlan.EXERCISE_ID += 1
        self.trainer_id = trainer_id
        self.equipment_id = equipment_id
        self.duration = duration
        self.id = ExercisePlan.EXERCISE_ID

    @classmethod
    def from_hours(cls, trainer_id, equipment_id, hours):
        return cls(trainer_id, equipment_id, hours * 60)

    @staticmethod
    def get_next_id():
        return ExercisePlan.EXERCISE_ID + 1

    def __repr__(self):
        return f"Plan <{self.id}> with duration {self.duration} minutes"
