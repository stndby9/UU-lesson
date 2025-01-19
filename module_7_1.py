import pprint


class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    __file_name = 'products.txt'

    def get_products(self):
        file = open(self.__file_name, 'r')
        c_prod = file.read().strip()
        file.close()
        return c_prod

    def add(self, *products):
        l_prod = set()
        file = open(self.__file_name, 'r')
        for line in file:
            l_prod = line.split(', ')[0]
        file.close()
        file = open(self.__file_name, 'a')
        for product in products:
            if product.name not in l_prod:
                file.write(f'{product}\n')
            else:
                print(f'Продукт {product.name} уже есть в магазине.')


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')
print(p2)
s1.add(p1, p2, p3)
print(s1.get_products())
