# Create a class BINARY TREE that contains background information of product prices (product code, price of 1 product). 
# The tree is sorted by product codes. From the keyboard enter data on the number of products in the format: product code, number of products. 
# Using a tree, find the cost of products (cost = quantity * price of one product).


class Product:
    __product_code : int
    __price: int
    
    def __init__(self, product_code, price):
        self.product_code = product_code
        self.price = price

    @property
    def product_code(self):
        return self.__product_code
    

    @product_code.setter
    def product_code(self, value):
        if not isinstance(value, int):
            raise TypeError("Product code must be an integer")
        self.__product_code = value


    @property
    def price(self):
        return self.__price
    

    @price.setter
    def price(self, value):
        if not isinstance(value, int):
            raise TypeError("Product code must be an integer")
        self.__price = value


class Node:
    product: Product
    def __init__(self, product):
        self.product = product
        self.left = None
        self.right = None


    def __lt__(self, other):
        return self.product.product_code < other.product.product_code


    def __gt__(self, other):
        return self.product.product_code > other.product.product_code




class BinaryTree:
    root: Node
    def __init__(self):
        self.root = None


    def addNode(self, node):
        if self.root is None:
            self.root = node
        else:
            self.add(node, self.root)


    def add(self, node, current_root: Node):
        if node > current_root:
            if current_root.right is None:
                current_root.right = node
            else:
                self.add(node, current_root.right)
        if node < current_root:
            if current_root.right is None:
                current_root.right = node
            else:
                self.add(node, current_root.left)


    def search(self, code, current_root: Node) -> int:
        if not current_root:
            return 

        if current_root.product.product_code == code:
            return current_root.product.price
        elif current_root.product.product_code > code:
            return self.search(code, current_root.left)
        else:
            return self.search(code, current_root.right)


    def count (self, code, quantity):
        return self.search(code, self.root)*quantity

        


def main():

    x = BinaryTree()
    number_of_products = input("Enter the number of products")
    for i in range(number_of_products):
        print("Product " + str(i))
        code = int(input("Enter the product code: "))
        price = int(input("Enter the product price: "))
        x.addNode(Node(Product(code, price)))

    print(x.count(19, 200))




if __name__ == "__main__":
    main()