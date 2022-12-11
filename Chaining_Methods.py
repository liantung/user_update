class User:

    def __init__(self, first_name, last_name, email, age):

        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0

    # Methods:

    def display_info(self):
        print(f"First name: {self.first_name}")
        print(f"Last name: {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Age: {self.age}")
        print(f"Member: {self.is_rewards_member}")
        print(f"Current Points: {self.gold_card_points}")

    def enroll(self):

        # NINJA BONUS
        if(self.is_rewards_member):
            print("User already a member.")
            return self
        
        self.is_rewards_member = True


        self.gold_card_points = 200

        return self

    
    
    def spend_points(self, amount):

        # Add logic in the spend points method
        # to be sure they have enough points to 
        # spend that amount and handle appropriately
        if self.gold_card_points < amount:
            print("Insufficient points.")
            return False

        # decrease the user's points by the amount specified.
        self.gold_card_points -= amount



my_user = User("Lian", "Tung", "ltung@codingdojo.com", 28)
my_user.display_info()

user2 = User("Rob", "John", "cbrown@codingdojo.com", 35)
user3 = User("Justin", "Hart", "srollins@codingdojo.com", 39)

my_user.spend_points(40)
user2.enroll().spend_points(80)

my_user.display_info()
user2.display_info()
user3.display_info()