from Zoo.reptile import Reptile


class Lizard(Reptile):

    def __init__(self, name: str):
        Reptile.__init__(self, name)
