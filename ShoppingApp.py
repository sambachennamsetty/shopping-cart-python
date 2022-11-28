from MyStore import MyStore
from ShoppingCart import ShoppingCart
import pickle


def read_pickle():
    try:
        fileObj = open('data.obj', 'rb')
        pickleObj = pickle.load(fileObj)
        fileObj.close()
        return pickleObj
    except Exception as e:
        print()
        return None


def save_to_pickle(store, scart):
    dataObj = {'store': store, 'scart': scart}
    fileObj = open('data.obj', 'wb')
    pickle.dump(dataObj, fileObj)
    fileObj.close()


def main():
    fname = 'ProductData.txt'
    store = MyStore()
    scart = ShoppingCart()  # empty shopping cart

    pickle_data = read_pickle()
    if pickle_data:
        store = pickle_data.get("store")
        scart = pickle_data.get("scart")
    else:
        store.read_products_from_file(fname)

    main_menu = '1: View Products' + '\n' + '2: Shop' + '\n' + \
                '3: Checkout' + '\n' + '4: Add Product' + '\n' + '5: Remove Product' + '\n' + '0: Exit'
    shopping_menu = '\t1: Add Product to Cart' + '\n\t' + '2: Remove Product From Cart ' + '\n\t ' + \
                    '3: Show Cart' + '\n\t' + '4: Clear Cart ' + '\n\t ' + '0: back to main'

    menu_option = 1
    while menu_option > 0:
        print('\n' + main_menu)
        menu_option = input('please enter an option: ')
        menu_option = int(menu_option)
        if menu_option == 0:
            print('quitting application..')
            if len(scart.items) > 0 or len(store.plist) > 0:
                save_to_pickle(store, scart)
            break  # exit main loop
        if menu_option == 1:
            store.show_products()
        if menu_option == 2:
            shopping_menu_option = 1
            while shopping_menu_option > 0:
                print('\n' + shopping_menu)
                soption = input('\tplease enter a shopping option: ')
                shopping_menu_option = int(soption)
                if shopping_menu_option == 1:  # add to cart
                    pid_qty = input('\tplease enter productid,qty to buy(ex: 1001, 3): ')
                    if (pid_qty.index(',') < 0):
                        print('invalid productid,qty specified..')
                    else:
                        parts = pid_qty.split(',')
                        pid = int(parts[0])
                        qty = int(parts[1])
                        pr = store.get_product(pid)
                        if pr != None:
                            scart.add_item(pr, qty)
                if shopping_menu_option == 2:  # remove from cart
                    pid = input('\tplease enter productid to remove from cart: ')
                    scart.remove_item(int(pid))
                if shopping_menu_option == 3:  # view cart
                    scart.show_cart()
                if shopping_menu_option == 4:  # clear cart
                    scart.clear_cart()
        if menu_option == 3:  # checkout
            total = scart.compute_total()
            print(total)
            total_after_discount = scart.apply_discount(total)
            print('\n------check out info---------')
            print('Total Amount = ', total, ' Total Amount after discount = ', total_after_discount)
        if menu_option == 4:
            print("")
            pid = int(input("Please enter product id: (ex: 1001): "))
            pname = input("Please enter product name: (ex: 12 inch laptop): ")
            price = float(input("Please enter product price: (ex:124.34): "))
            cat = input("Please enter product category: (ex:electronics): ")
            store.add_product(pid, pname, price, cat)

        if menu_option == 5:
            print("")
            pid = int(input("Please enter product id to remove: (ex: 1001): "))
            store.remove_product(pid)


main()
