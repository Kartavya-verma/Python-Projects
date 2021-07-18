class lap:
    def __init__(self,brand,series,price):
        self.brand=brand
        self.series = series
        self.price = price
    def discount(self,pri):
        dis=(pri/100)*self.price
        dis=self.price-dis
        print(dis)

l=lap("Asus","TUF series",70000)
l.discount(10)