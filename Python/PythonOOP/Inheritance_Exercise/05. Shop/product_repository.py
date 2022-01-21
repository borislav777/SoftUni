from product import Product


class ProductRepository:
    def __init__(self):
        self.products = []

    def add(self, product: Product):
        return self.products.append(product)

    def find(self, product_name):
        for p in self.products:
            if p.name == product_name:
                return p

    def remove(self, product_name):
        for p in self.products:
            if p.name == product_name:
                return self.products.remove(p)

    def __repr__(self):
        result = ''

        result += "\n".join([f"{p.name}: {p.quantity}" for p in self.products])

        return result
