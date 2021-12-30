from utility import divide, multiple
# from shopping.more_shopping.shopping_cart import buy
#way2
from shopping.more_shopping import shopping_cart
if __name__ == '__main__':
    print(divide(12, 2))
    print(multiple(2, 3))


    # shopping.more_shopping.shopping_cart.buy('T-Shirt')
    # shopping.more_shopping.shopping_cart.buy('Short')
    # # shopping.shopping_cart.shoppping_cart.discard('T-Shirt')
    # shopping.more_shopping.shopping_cart.discard('Short')
    # print(shopping.more_shopping.shopping_cart.cart)
    print(shopping_cart.buy('ringo, apple'))
    print(shopping_cart.buy('whore'))
    print(max([12,3,4,5]))
    print(shopping_cart.max())
    if __name__ == '__main__':
        print('This is main modules')