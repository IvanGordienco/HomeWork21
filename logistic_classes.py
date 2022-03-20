from abc import abstractmethod


# Склад
class Storage:

    @abstractmethod
    def add(self, name, count):
        ...

    @abstractmethod
    def remove(self, name, count):
        ...

    @abstractmethod
    def get_free_space(self):
        ...

    @abstractmethod
    def get_items(self):
        ...

    @abstractmethod
    def get_unique_items_count(self):
        ...


#  Склад
class Store(Storage):
    def __init__(self):
        self.items = {}
        self.capacity = 100

    def add(self, name, count):
        is_found = False
        if self.get_free_space() > count:
            for key in self.items.keys():
                if name == key:
                    self.items[key] = self.items[key] + count
                    is_found = True
            if not is_found:
                self.items[key] = count
            print("Товар добавлен")
        else:
            print(f"Товар не может быть добавлен, так как есть место только на {self.get_free_space()}")

    def remove(self, name, count):
        for key in self.items.keys():
            if name == key:
                if self.items[key] - count >= 0:
                    self.items[key] = self.items[key] - count
                else:
                    print(f"Слишком мало {name}")
            else:
                print(f" {name.title()} - нет на складе ")

    def get_free_space(self):
        return self.capacity - sum(self.items.values())

    def get_items(self):
        return self.items

    def get_unique_items_count(self):
        return len(self.items.keys())


# Магазин
class Shop(Store):
    def __init__(self, limit=5):
        super().__init__()
        self.limit = limit
        self.capacity = 20

    @property
    def get_limit(self):
        return self.limit

    def add(self, name, count):
        if self.get_unique_items_count() < self.limit:
            super.add(name, count)
        else:
            print("Товар не может быть добавлен")


class Request:
    def __init__(self):
        lst = self.get_info(str)
        self.from_ = lst[4]
        self.to = lst[6]
        self.amount = int(lst[1])
        self.product = lst[2]

    def get_info(self, str):
        return str.split(" ")

    def __repr__(self):
        return f'Доставить {self.amount} {self.product} из {self.from_} в {self.to}'
