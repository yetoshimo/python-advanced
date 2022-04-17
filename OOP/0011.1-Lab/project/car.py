from vehicle import Vehicle


class Car(Vehicle):

    def __init__(self):
        super(Car, self).__init__()

    @staticmethod
    def drive():
        return "driving"
