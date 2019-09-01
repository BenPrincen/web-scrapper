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
    def __init__(self, price_history, title, dates):
        self.price_history = price_history
        self.dates = dates
        self.title = title
        self.date = dates[len(dates) - 1]
        self.price = price_history[len(price_history) - 1]

    def getPriceHistory():
        return price_history

    def getTitle():
        return title

    def getLastPrice():
        return price

    def getLastUpdated():
        return date
