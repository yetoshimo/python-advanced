from car import Car


class SportsCar(Car):

    def __init__(self):
        super(SportsCar, self).__init__()

    @staticmethod
    def race():
        return "racing"
