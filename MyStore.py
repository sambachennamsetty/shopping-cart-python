from Product import Product


class MyStore(object):
    def __init__(self):
        self.plist = []  # store contains list of products

    def read_products_from_file(self, file_name):
        lines = open(file_name)
        plist = []  # product list
        for line in lines:
            parts = line.split(',')  # split line into parts
            pr = Product(int(parts[0]), parts[1], float(parts[2]), parts[3])
            self.plist.append(pr)
        return self.plist

    def add_product(self, pid, pname, price, cat):
        pr = Product(int(pid), pname, price, cat)
        self.plist.append(pr)
        return self.plist

    def remove_product(self, pid):  # remove product from products

        product_to_remove = None
        for product in self.plist:
            if product.product_id == pid:
                product_to_remove = product
        if product_to_remove != None:
            self.plist.remove(product_to_remove)

    def show_products(self):
        for pr in self.plist:
            print(pr, end='')  # end='' suppresses newline after each

    def get_product(self, pid):
        for pr in self.plist:
            if pr.product_id == pid:
                return pr
        return None
