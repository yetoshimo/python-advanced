from project.medicine.medicine import Medicine


class Salve(Medicine):
    default_health_increase = 50

    def __init__(self):
        super().__init__(self.default_health_increase)
