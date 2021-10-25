from project.baked_food.bread import Bread
from project.baked_food.cake import Cake
from project.drink.tea import Tea
from project.drink.water import Water
from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable


class Bakery:

    def __init__(self, name):
        self.name = name
        self.food_menu = []
        self.drinks_menu = []
        self.tables_repository = []
        self.total_income = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == "" or value == " ":
            raise ValueError("Name cannot be empty string or white space!")
        self.__name = value

    def add_food(self, food_type: str, name: str, price: float):
        find_food = [f for f in self.food_menu if f.name == name]
        if find_food:
            raise Exception(f"{food_type} {name} is already in the menu!")
        if food_type == "Bread":
            self.food_menu.append(Bread(name, price))
        elif food_type == "Cake":
            self.food_menu.append(Cake(name, price))
        return f"Added {name} ({food_type}) to the food menu"

    def add_drink(self, drink_type: str, name: str, portion: int, brand: str):
        find_drink = [d for d in self.drinks_menu if d.name == name]
        if find_drink:
            raise Exception(f"{drink_type} {name} is already in the menu!")
        if drink_type == "Tea":
            self.drinks_menu.append(Tea(name, portion, brand))
        elif drink_type == "Water":
            self.drinks_menu.append(Water(name, portion, brand))
        return f"Added {name} ({brand}) to the drink menu"

    def add_table(self, table_type: str, table_number: int, capacity: int):
        find_table = [t for t in self.tables_repository if t.table_number == table_number]
        if find_table:
            raise Exception(f"Table {table_number} is already in the bakery!")
        if table_type == "InsideTable":
            self.tables_repository.append(InsideTable(table_number, capacity))
        elif table_type == "OutsideTable":
            self.tables_repository.append(OutsideTable(table_number, capacity))

        return f"Added table number {table_number} in the bakery"

    def reserve_table(self, number_of_people: int):
        for table in self.tables_repository:
            if not table.is_reserved and table.capacity >= number_of_people:
                table.reserve(number_of_people)
                return f"Table {table.table_number} has been reserved for {number_of_people} people"

        return f"No available table for {number_of_people} people"

    def order_food(self, table_number: int, *args):
        find_table = [t for t in self.tables_repository if t.table_number == table_number]
        if not find_table:
            return f"Could not find table {table_number}"
        not_in_menu = []
        table = find_table[0]
        for food_name in args:
            is_found = False
            for food in self.food_menu:
                if food.name == food_name:
                    table.order_food(food)
                    is_found = True
                    break
            if not is_found:
                not_in_menu.append(food_name)
        result = f"Table {table_number} ordered:\n"
        for order in table.food_orders:
            result += f"{repr(order)}\n"
        result += f"{self.name} does not have in the menu:\n"
        for order in not_in_menu:
            result += f"{order}\n"
        return result

    def order_drink(self, table_number: int, *args):
        find_table = [t for t in self.tables_repository if t.table_number == table_number]
        if not find_table:
            return f"Could not find table {table_number}"
        not_in_menu = []
        table = find_table[0]
        for drink_name in args:
            is_found = False
            for drink in self.drinks_menu:
                if drink.name == drink_name:
                    table.order_drink(drink)
                    is_found = True
                    break
            if not is_found:
                not_in_menu.append(drink_name)
        result = f"Table {table_number} ordered:\n"
        for order in table.drink_orders:
            result += f"{repr(order)}\n"
        result += f"{self.name} does not have in the menu:\n"
        for order in not_in_menu:
            result += f"{order}\n"
        return result

    def leave_table(self, table_number: int):
        find_table = [t for t in self.tables_repository if t.table_number == table_number]
        table = find_table[0]
        bill = table.get_bill()
        table.clear()
        self.total_income += bill
        result = f"Table: {table_number}\n"
        result += f"Bill: {bill:.2f}"
        return result

    def get_free_tables_info(self):
        result = ""
        for table in self.tables_repository:
            result += f"{table.free_table_info()}\n"
        return result

    def get_total_income(self):
        return f"Total income: {self.total_income:.2f}lv"


# bakery = Bakery("Sweet")
# print(bakery.add_food("Cake", "selska", 25.00))
# print(bakery.add_food("Cake", "nedelq", 29.00))
# print(bakery.add_food("Bread", "rajen", 1.00))
# print(bakery.food_menu)
# print(bakery.add_drink("Water", "devin", 1, "devin"))
# print(bakery.add_drink("Water", "trapezna", 1, "baldaran"))
# print(bakery.add_drink("Tea", "limone", 1, "Lipton"))
# print(bakery.drinks_menu)
# bakery.tables_repository.append(InsideTable(1, 5))
# print(bakery.reserve_table(6))
# print(bakery.order_food(1,'selska','nedelq','rajen','bql','tipov'))
# print(bakery.order_drink(1,'devin','trapezna','limone','cola','fanta'))
