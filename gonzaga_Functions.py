def display_menu(menu):
    print("\nAvailable Menu:")
    for index, (item, price) in enumerate(menu.items(), start=1):
        print(f"{index}. {item} - ₱{price:.2f}")

def select_item(menu):
    while True:
        choice = input("\nEnter your order number: ")
        if choice.isdigit():
            choice = int(choice)
            if 1 <= choice <= len(menu):
                item = list(menu.keys())[choice - 1]
                price = menu[item]
                print(f"You selected: {item} costing ₱{price:.2f}")
                return item, price
            else:
                print("Invalid choice. Please select a valid item number.")
        else:
            print("Invalid input. Please enter a number.")

def calculate_total(price):
    print(f"\nYour total cost is: ₱{price:.2f}")
    return price

def process_payment(total_cost):
    while True:
        cash = input("\nEnter the cash amount : ")
        if cash.replace('.', '', 1).isdigit():
            cash = float(cash)
            if cash >= total_cost:
                change = cash - total_cost                                                                                           
                print(f"Payment successful. Your change is ₱{change:.2f}.")
                return
            else:
                print(f"Insufficient Balanced. ₱{total_cost:.2f}.")
        else:
            print("Invalid input. Please enter a valid amount.")

def main():
    
    menu = {
        "Classic Roasted Chicken (Quarter)": 205.00,
        "Classic Roasted Chicken (Half)": 375.00,
        "Classic Roasted Chicken (Whole)": 715.00,
        "OMG Unfried Fried Chicken (2 pcs)": 205.00,
        "Honey Bourbon Ribs (Half)": 440.00,
        "Honey Bourbon Ribs (Whole)": 850.00,
        "Spaghetti with Meatballs Platter": 550.00,
        "Tex Mex Platter": 550.00,
        "Grilled Fish Solo A": 300.00,
        "Grilled Sausage (with 1 side dish)": 265.00,
        "Premium Steak (with 2 side dishes)": 600.00,
        "Mac and Cheese (Regular)": 55.00,
        "Roasted Carrots (Large)": 90.00,
        "Corn Muffin (1 pc)": 20.00,
        "Chicken Quesadilla": 215.00,
        "Caesar Salad": 165.00,
        "Bottled Water": 55.00,
        "Coke In Can": 70.00,
        "Minute Maid 295 ml": 33.00
    }
    print("Welcome to the Kenny Rogers Premium Dining Experience!\n")

    
    display_menu(menu)

    
    item, price = select_item(menu)

    total_cost = calculate_total(price)

    
    process_payment(total_cost)

    print("\nThank you for your order! Have a great day!")

if __name__ == "__main__":
    main()
