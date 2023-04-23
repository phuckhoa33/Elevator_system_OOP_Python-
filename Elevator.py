from FloorManagement import FloorManagement
from Enum.StateEnum import ElevatorState
import time

class Elevator():
    def __init__(self, elevator_id: str, restricted_amount: int, permission_level: int, floor_manager: FloorManagement, top_floor: int, bottom_floor: int) -> None:
        self.top_floor = top_floor
        self.bottom_floor = bottom_floor
        self._elevator_id = elevator_id
        self._state = ElevatorState.SLEEP_TIME
        self._floor_manager = floor_manager
        self._current_floor = 0
        self._restricted_amount = restricted_amount
        self._amount_people = 0 
        self._permission_level = permission_level
        self._stopped = True

    def stop(self, stoppedFloor: int):
        self._stopped = True
        self._floor_manager.popWaitedFloor(stoppedFloor)
        self._current_floor = stoppedFloor
        time.sleep(5)

    def setState(self, state: ElevatorState):
        self._state = state

    def run(self):
        manager = self._floor_manager
        i: int = 0
        while len(manager._waitedFloors)>0:
            if self._current_floor==self.top_floor:
                self.setState(ElevatorState.MOVE_DOWN)
            elif self._current_floor==self.bottom_floor:
                self.setState(ElevatorState.MOVE_TOP)

            if self._state==ElevatorState.MOVE_DOWN:
                i -= 1 
            elif self._state==ElevatorState.MOVE_TOP:
                i += 1
            manager.popWaitedFloor(i)
            self.stop(i)
            

    
    