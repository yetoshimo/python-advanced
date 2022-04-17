from HierarchicalInheritance.person import Person
from HierarchicalInheritance.employee import Employee


class Teacher(Person, Employee):

    @staticmethod
    def teach():
        return f"teaching..."
