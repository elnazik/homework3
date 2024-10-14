class Stock:
    def stock(self):
        pass

class Security(Stock):
    def security(self):
        return "security"

class Asset(Security):
    def asset(self):
        return "assets"

class InterestBearingItem(Security):
    def InterestBearingItem(self):
        return "InterestBearingItem"

stock = Stock()
print(stock.stock())
asset = Asset()
print(asset.asset())
interest_bearing_item = InterestBearingItem()
print(interest_bearing_item.InterestBearingItem())

