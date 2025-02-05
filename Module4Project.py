# Encapsulation - Data (menu, prices) and methods are bundled into the class
# Abstraction - Complex delivery logic is hidden behind simple method calls

class DunnDelivery:
    def __init__(self):
        # encapsulation by keeping data together

        # set up menu, prices, and delivery locations
        self.menu = {
            "Energy Drinks": ["Monster", "Rockstar"],
            "Coffee Drinks": ["Latte", "Cappuccino"],
            "Seasonal Drinks": ["Pumpkin Spice Latte", "Hot Coco", "Lemonade slush"],
            "Breakfast": ["Bagel", "Muffin", "Scone"],
            "Lunch": ["Falafel Wrap", "Hummus & Pita", "Chicken Wrap"]
        }

        self.prices = {
            "Monster": 3.99, "Rockstar": 3.99,
            "Latte": 4.99, "Cappuccino": 4.99,
            "Pumpkin Spice Latte": 4.99, "Hot Coco": 3.99, "Lemonade slush": 4.99,
            "Bagel": 2.99, "Muffin": 2.99, "Scone": 2.99,
            "Falafel Wrap": 8.99, "Hummus & Pita": 7.99, "Chicken Wrap": 8.99
        }

        self.delivery_locations = {
            "Library": 10, # minutes
            "Academic Success Center": 8,
            "ITEC Computer Lab": 5
        }

    def show_menu(self, category=None):
        # prints out the menu of the requested category
        if category:
            print(f"\n==={category} ===")
            for item in self.menu[category]:
                print(f"{item}: ${self.prices[item]:.2f}")
        else:
            for category in self.menu:
                print(f"\n=== {category} ===")
                for item in self.menu[category]:
                    print(f"{item}: ${self.prices[item]:.2f}")
            
    def calculate_total(self, items, has_student_id=False, priority=False):
        # calculate the sum of the items ordered
        total = sum(self.prices[item] for item in items)
        # 10% discount for students
        if has_student_id and total > 10:
            total *= 0.9
        # 2$ extra dollars for priority
        if priority:
            total += 2
        return total

    def estimate_delivery(self, location, current_hour, priority):
        # gets the time for delivery
        base_time = self.delivery_locations[location]
        # depending on the hour the delivery may take longer
        if (9 <= current_hour <= 10) or (11 <= current_hour <= 13):
            base_time += 5
        # subtracts 3 when using priority
        if priority:
            base_time -= 3
        return base_time

    def print_order(self, location, items, current_hour, has_student_id, priority):
        # prints the order
        print("\n=== Order Summary ===")
        print(f"Delivery to: {location}")
        print("\nItems Ordered:")
        for item in items:
            print(f"- {item}: ${self.prices[item]:.2f}")
        
        # calculates the total, delivery time
        total = self.calculate_total(items, has_student_id, priority)
        delivery_time = self.estimate_delivery(location, current_hour, priority)

        # prints if priority is true
        if priority:
            print("\nPriority Order $2.00 [cannot be discounted]")
        
        # prints the subtotal, after discount, and delivery time
        print(f"\nSubtotal: ${sum(self.prices[item] for item in items):.2f}")
        if has_student_id and total < sum(self.prices[item] for item in items):
            print("Student Discount Applied!")
        print(f"Total after discount: ${total:.2f}")
        print(f"Estimate delivery time: {delivery_time} minutes")

    def price_search(self):
            try:
                # gets search
                search = float(input("\nWhat is your budget?: "))
                while True:
                    # checks if search is above zero
                    if search > 0:
                        # gets prices under the users budget
                        for item in self.prices:
                            if self.prices[item] <= search:
                                print(f"{item}  {self.prices[item]}")
                        break
                    else:
                        search = float(input("Please enter a positive number?: "))
            except ValueError:
                ("Please enter a float number.")

def ask_rating():
    # asks if user would rate delivery
    inquiry = input("\nwould you like to rate your delivery?(y\\n): ")
    while True:
        try:
            if inquiry == "y" or inquiry == "Y":
                # checks if user rating is a integer and between 1-5
                userRating = int(input("What would you rate us out of 5?: "))
                while not 1 <= userRating <= 5:
                    userRating = int(input("Enter a number between 1-5: "))
                # writes the answer into a file
                with open("star_rating.txt", "a") as file:
                   file.write(f"{userRating} Stars\n")
                break
            # breaks if user didn't want to rate delivery
            elif inquiry == "n" or inquiry == "N":
                break
            else:
                # makes user type 'y' or 'n'
                inquiry = input("please enter(y\\n): ")
        except ValueError:
            # prints if error occurs
            print("Please enter a valid number - ", end= '')

def main():
    delivery = DunnDelivery()
    delivery.show_menu("Coffee Drinks")

    order = ["Latte", "Bagel", "Bagel", "Muffin", "Hot Coco"]

    delivery.print_order("ITEC Computer Lab", order, 9, has_student_id=True, priority=True)

    #ask_rating()
    #delivery.price_search()

if __name__ == "__main__":
    main()