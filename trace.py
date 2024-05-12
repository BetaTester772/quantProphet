from sparklestock import Stock
from time import sleep


def init_stock_system() -> Stock:
    system = Stock("http://3.34.181.14")
    system.login("id", "pw")

    print("Init Complete")
    print(system.check_my_asset())

    return system


if __name__ == '__main__':
    stock_system = init_stock_system()
    while True:
        temp = stock_system.check_my_asset()
        if stock_system.check_my_asset() != temp:
            temp = stock_system.check_my_asset()
            print(temp)
        sleep(2)
