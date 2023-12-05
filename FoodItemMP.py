class FoodItemMP:
    def __init__(self, foodName, amount):
        self.foodName = foodName
        self.amount = amount
        self.standardPrice = 0.0
        self.calculatedPrice = 0.0

    def priceListMP(self):
        foodPrices = {
            "Dry Cured Iberian Ham": 177.80,
            "Wagyu Steaks": 450.00,
            "Matsutake Mushrooms": 272.00,
            "Kopi Luwak Coffee": 306.50,
            "Moose Cheese": 487.20,
            "White Truffles": 3600.00,
            "Blue Fin Tuna": 3603.00,
            "Le Bonnotte Potatoes": 270.81
        }
        self.standardPrice = foodPrices.get(self.foodName, 0.0)

    def calculateCostMP(self):
        self.calculatedPrice = self.standardPrice * self.amount
        return self.calculatedPrice

    def __str__(self):
        return f"Item: {self.foodName}\nAmount ordered: {self.amount} pounds\nPrice per pound: ${self.standardPrice:.2f}\nPrice of order: ${self.calculatedPrice:.2f}\n"
