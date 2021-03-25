class Catalogue:

    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def get_by_letter(self, first_letter):
        res = [prod for prod in self.products if prod[0] == first_letter]
        return res

    def __repr__(self):
        self.products = sorted(self.products)
        result = f"Items in the {self.name} catalogue:\n"

        result += '\n'.join(self.products)
        return result


catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)
