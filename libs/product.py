class Product:

    # create objecet with a single price and date
    # used when product first starts getting tracked
    def __init__(self, price, title, last_updated):
        self.price = price
        self.title = title
        self.date = last_updated
        self.price_history = [price]
        self.dates = [last_updated]

    # create object with list of prices, and dates updated
    # used when product has been tracked before

    def getPriceHistory(self):
        return self.price_history

    def getTitle(self):
        return self.title

    def getLastPrice(self):
        return self.price

    def getLastUpdated(self):
        return self.date
