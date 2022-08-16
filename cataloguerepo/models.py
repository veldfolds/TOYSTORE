import json
#represents a specific toy on the shelf
class Toy():
   
        # if(name or manufacturer or price or image_url or year_manufactured or stock or category == None):
        #     raise Exception("Ensure all toy attributes have been set")
        # else:
    toy_id = "",
    name = "",
    manufacturer = "",
    price = 0,
    image_url = "",
    year_manufactured = "",
    stock = 0,
    category = ""

    def __init__(self, name, manufacturer, price, image_url, year_manufactured, stock, category, toy_id = "") -> None:
        self.name = name
        self.manufacturer = manufacturer
        self.price = price
        self.image_url = image_url
        self.year_manufactured = year_manufactured
        self.stock = stock
        self.category = category
        self.toy_id = toy_id

    def to_json(self):
        toy_json = json.dumps(self.__dict__)
        return toy_json


toy1 = Toy("Fly581", "ToyMaker", 35, "https://ToyMaker.com", "2018", 5, "flight", "1")
toy2 = Toy("Train", "ToyMaker", 35, "https://ToyMaker.com", "2018", 5, "flight", "2")
toy3 = Toy("Bear", "ToyMaker", 35, "https://ToyMaker.com", "2018", 5, "flight", "3")
toy4 = Toy("Zebra", "ToyMaker", 35, "https://ToyMaker.com", "2018", 5, "flight", "4")
toy5 = Toy("Russian doll", "ToyMaker", 35, "https://ToyMaker.com", "2018", 5, "flight", "5")
toy6 = Toy("Drone", "ToyMaker", 35, "https://ToyMaker.com", "2018", 5, "flight", "6")
toy7 = Toy("Kite", "ToyMaker", 35, "https://ToyMaker.com", "2018", 5, "flight", "7")
toy8 = Toy("Boat", "ToyMaker", 35, "https://ToyMaker.com", "2018", 5, "flight", "8")
toy9 = Toy("Board game", "ToyMaker", 35, "https://ToyMaker.com", "2018", 5, "flight", "9")
toy10 = Toy("Card", "ToyMaker", 35, "https://ToyMaker.com", "2018", 5, "flight", "10")

toys_list = [toy1, toy2, toy3, toy4, toy5, toy6, toy7, toy8, toy9, toy10]

