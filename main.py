from logistic_classes import Shop, Storage, Request, Store


if __name__ == '__main__':
    shop = Shop()
    print(shop.get_limit)
    shop.limit = 8
    print(shop.limit)