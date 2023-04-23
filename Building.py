from ElevatorManagement import ElevatorManagement
from FloorManagement import FloorManagement
from Elevator import Elevator
import json


class Building():
    def __init__(self, top_floor: int, bottom_floor) -> None:
        self.top_floor = top_floor
        self.bottom_floor = bottom_floor
        self.__managementSystem = ElevatorManagement(self.__elevators)
    
    @property
    def __elevators(self) -> list:
        with open("elevators.json", "r") as f:
            data = json.loads(f.read())
        return [self.__create_elevator(**elevator) for elevator in data['elevators']]
    
    def __create_elevator(self, elevator_id: str, restricted_amount: int, permission_level: int):
        floor_manager = FloorManagement(elevator_id)
        return Elevator(elevator_id, restricted_amount, permission_level, floor_manager, self.top_floor, self.bottom_floor)

    @property
    def floors(self):
        return [Floor(floor, self.__managementSystem, self.__elevators) for floor in range(self.bottom_floor, self.top_floor+1)]

    def set_question(self):
        while True:
            floor = int(input("What floor do you stay now: "))
            for i in range(len(self.floors)):
                if self.floors[i]._floor_number==floor:
                    floor = self.floors[i]
                    break 
            floor.dashboard()

class Floor():
    def __init__(self, floor_number: int, manager: ElevatorManagement, elevators: list) -> None:
        self._floor_number = floor_number
        self.__manager = manager
        self.__elevators = elevators
        
    def dashboard(self): 
        print("-------------------------")
        print("---------1 2 3-----------")
        print("---------4 5 7-----------")
        print("---------| 8 9---------")
        print("-------------------------")
        choose = int(input("Please enter your elevator: "))
        elevator_id = int(input("Please enter you choosen elevator: "))
        elevator: Elevator = self.__elevators[elevator_id]
        self.__manager.approveRequestFromUser(choose, elevator_id, elevator_id)
    