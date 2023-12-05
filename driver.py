import FoodItemMP as fi

def createItemListMP():
    foodList = []
    numItems = int(input("How many items will you order today? "))
    if numItems < 1:
        print("You need to order at least 1 item.")
        return createItemListMP()
    for i in range(1, numItems + 1):
        foodName = input(f"Item #{i}-\nEnter food: ")
        amount = float(input(f"Enter amount of pounds: "))
        if amount <= 0:
            print("The pounds must be greater than 0.")
            continue
        foodItem = fi.FoodItemMP(foodName, amount)
        foodItem.priceListMP()
        foodItem.calculateCostMP()
        foodList.append(foodItem)
    return foodList

def displayListMP(foodList):
    for foodItem in foodList:
        print(foodItem)

def calculateTotalCostMP(foodList):
    totalCost = 0
    for foodItem in foodList:
        totalCost += foodItem.calculatedPrice
    return totalCost

def main():
    foodList = createItemListMP()
    displayListMP(foodList)
    totalCost = calculateTotalCostMP(foodList)
    print(f"Total cost: ${totalCost:.2f}")

main()
