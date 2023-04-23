from Elevator import Elevator
from FloorManagement import FloorManagement
from Enum.StateEnum import ElevatorState
import threading

class ElevatorManagement():
    def __init__(self, elevators: list):
        self._elevators = elevators

    @property
    def __floor_threads(self) -> None:
        threads = []
        for i in range(len(self._elevators)):
            elevator: Elevator = self._elevators[i]
            t = threading.Thread(elevator.run, args=())
            threads.append(t)
            t.start()
        return threads
    
    def __shutDownAllOperation(self):
        for i in self.__floor_threads:
            i.join()
    
    def approveRequestFromUser(self, floor, current_floor, elevator_index):
        elevator: Elevator = self._elevators[elevator_index]
        if elevator._state==ElevatorState.SLEEP_TIME:
            if current_floor<floor:
                elevator.setState(ElevatorState.MOVE_TOP)
            else:
                elevator.setState(ElevatorState.MOVE_DOWN)


        elevator._floor_manager.appendWaitedFloor(floor, current_floor)

        
    

            
