class Appliance:
    MONTH_DAYS = 30

    def __init__(self, cost):
        self.cost = cost

    def get_monthly_expense(self):
        return Appliance.MONTH_DAYS * self.cost
