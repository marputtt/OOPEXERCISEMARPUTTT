import FoodItemMP as fi

def createItemList():
    foodList = []
    numItems = int(input("How many items will you order today? "))
    if numItems < 1:
        print("Number of items must be at least 1.")
        return createItemList()
    for i in range(1, numItems + 1):
        foodName = input(f"Item #{i}-\nEnter food: ")
        amount = float(input(f"Enter amount of pounds: "))
        if amount <= 0:
            print("Amount of pounds must be greater than 0.")
            continue
        foodItem = fi.FoodItem(foodName, amount)
        foodItem.priceList()
        foodItem.calculateCost()
        foodList.append(foodItem)
    return foodList

def displayList(foodList):
    for foodItem in foodList:
        print(foodItem)

def calculateTotalCost(foodList):
    totalCost = 0
    for foodItem in foodList:
        totalCost += foodItem.calculatedPrice
    return totalCost

def main():
    foodList = createItemList()
    displayList(foodList)
    totalCost = calculateTotalCost(foodList)
    print(f"Total cost: ${totalCost:.2f}")

main()
