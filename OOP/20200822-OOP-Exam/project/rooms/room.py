class Room:
    room_cost = 0
    appliances = []

    def __init__(self, family_name, budget, members_count):
        self.members_count = members_count
        self.budget = budget
        self.family_name = family_name
        self.children = []
        self.expenses = 0

    @property
    def expenses(self):
        return self.__expenses

    @property
    def total_expenses(self):
        return self.expenses + self.room_cost

    @expenses.setter
    def expenses(self, value):
        self.__validate_expenses(value)
        # if value < 0:
        #     raise ValueError("Expenses cannot be negative")
        self.__expenses = value

    def calculate_expenses(self, *args):
        """Each element of args will be a list (with children or appliances).
                Calculate the total cost of all elements in the lists and set the expenses attribute to the result"""
        result = 0
        for items in args:
            result += sum(x.get_monthly_expense() for x in items)

        self.expenses = result

    @staticmethod
    def __validate_expenses(value):
        if value and value < 0:
            raise ValueError("Expenses cannot be negative")

    def __repr__(self):
        consumer_results = self.__get_consumer_total_cost()
        result = [
            f"{self.family_name} with {self.members_count} members. Budget: {self.budget:.2f}$, Expenses: {self.expenses:.2f}$",
            *consumer_results
        ]
        return '\n'.join(result)

    def __get_consumer_total_cost(self):
        result = []
        appliances_cost = sum([a.get_monthly_expense() for a in self.appliances])
        if self.children:
            counter = 1
            for i in self.children:
                line = f"--- Child {counter} monthly cost: {i.get_monthly_expense():.2f}$"
                result.append(line)
                counter += 1
            result.append(f"--- Appliances monthly cost: {appliances_cost:.2f}$")
        else:
            result.append(f"--- Appliances monthly cost: {appliances_cost:.2f}$")
        return result
