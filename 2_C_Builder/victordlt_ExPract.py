# Buileder Pattern applied in Fast food chain restaurant
from abc import ABC, abstractmethod

class IBurgerBuilder(ABC):
    @abstractmethod
    def add_bread(self, bread): pass

    @abstractmethod
    def add_meat(self, body): pass

    @abstractmethod
    def add_cheese(self, legs): pass

    @abstractmethod
    def add_dressing(self, legs): pass

    @abstractmethod
    def add_lettuce(self): pass
    
    @abstractmethod
    def add_tomato(self): pass

    @abstractmethod
    def get_burger(self): pass    

class ClassicBurgerBuilder(IBurgerBuilder):    
    def __init__(self):
         self.burger = Burger()

    def add_bread(self):
        self.burger.bread = "Brioche"       

    def add_meat(self):
        self.burger.meat = "Beef"

    def add_cheese(self):
        self.burger.cheese = "cheddar"

    def add_dressing(self):
        self.burger.dressing = True
    
    def add_lettuce(self):
        self.burger.lettuce = True
    
    def add_tomato(self):
        self.burger.tomato = True

    def get_burger(self):
        return self.burger

class VeggieBurgerBuilder(IBurgerBuilder): 
    def __init__(self):
         self.burger = Burger()

    def add_bread(self):
        self.burger.bread = "Whole Wheat"       

    def add_meat(self):
        self.burger.meat = "Veggie Patty"

    def add_cheese(self):
        self.burger.cheese = "Swiss"

    def add_dressing(self):
        self.burger.dressing = False 
    
    def add_lettuce(self):
        self.burger.lettuce = True
    
    def add_tomato(self):
        self.burger.tomato = True

    def get_burger(self):
        return self.burger

class BurgerDirector:
    def __init__(self, burger_builder):
         self.burger_builder = burger_builder

    def construct_burger(self):
        self.burger_builder.add_bread()
        self.burger_builder.add_meat()
        self.burger_builder.add_cheese()
        self.burger_builder.add_dressing()
        self.burger_builder.add_lettuce()
        self.burger_builder.add_tomato()
        


class Burger:
    def display_burger_info(self):
        print("Burger Info:")
        print(f"Bread: {self.bread}")
        print(f"Meat: {self.meat}")
        print(f"Cheese: {self.cheese}")
        print(f"Dressing: {self.dressing}")
        print(f"Lettuce: {self.lettuce}")
        print(f"Tomato: {self.tomato}")

#************************************************************************************
# Client code ***********************************************************************
#************************************************************************************
#burger_builder = ClassicBurgerBuilder()
burger_builder = VeggieBurgerBuilder()
burger_director = BurgerDirector(burger_builder)

burger_director.construct_burger()
burger = burger_builder.get_burger()

burger.display_burger_info() 