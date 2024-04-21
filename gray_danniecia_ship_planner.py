"""
Description: This code will write a program that can keep track of the composition of a container
ship and its cargo. The program will compute the speed and draught of potential container ship
configurations. 

Author: Danniecia Gray 
"""

class FullCargoShipError(Exception):
    def __init__(self, excpt= "Exception: Cargo Ship Full."):
        self.excpt = excpt
        
#container class storing container specifications
class Container:
    def __init__(self,size,type):
        self.size = size
        self.type = type

    def get_size(self):
        return self.size
    
    def get_cargo_type(self):
        return self.type
       


class Container_Ship:
    def __init__(self,max_cap,max_speed,min_draft,max_draft):
        self.max_cap = max_cap
        self.max_speed = max_speed
        self.min_draft = min_draft
        self.max_draft = max_draft
    #list of all the containers assigned to the cargo ship 
        self.containers = []

    def add_container(self,container):
            if self.max_cap > self.get_cargo:
                self.containers.append(container)
            
            else:
                raise FullCargoShipError
        
    def remove_container(self,container):
        self.containers.pop(container)

    #returns amount of cargo on ship
    def get_cargo(self):
        return len(self.containers)
    
    #returns ship draft
    def get_draft(self):
        return len(self.containers)+7
    
    #returns ship speed
    def get_speed(self):
        return self.get_draft - self.max_speed


    #print method 
    def print_ship(self):
        

        cargo = print(f'Cargo: {ship.get_cargo()} TEUs')
        draft = print(f'Draft: {ship.get_draft()} meters')
        speed = print(f'Speed: {ship.get_speed()} knots')
        list  = print(self.containers)

        return cargo,draft,speed,list



ship=Container_Ship
cargo_types=["FF","CG","PG","RM","IE"]


size = input("Enter container size: ")

if size in ["1","2"]:
        
    type = input("Enter container type: ")

    try:
        container = Container(size,type)
        if type in cargo_types:
            ship.add_container(container)
                
    except ValueError:
        print("Exception: Invalid Cargo Type")
    
else:
    print("Enter a valid number!")