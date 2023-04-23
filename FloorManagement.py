
class FloorManagement():
    def __init__(self, elevator_id: str) -> None:
        self._elevator_id = elevator_id
        self._waitedFloors = []

    def popWaitedFloor(self, oldFloor: int):
        if oldFloor in self._waitedFloors:
            index_of_floor = self._waitedFloors.index(oldFloor)
            self._waitedFloors.remove(index_of_floor)
            print(f"{oldFloor} is {self.state}")

    def appendWaitedFloor(self, newFloor: int, currentFloor: int) -> None:
        if newFloor not in self._waitedFloors:
            self._waitedFloors.append(newFloor)
            self._waitedFloors.append(currentFloor)
            self._waitedFloors = sorted(self._waitedFloors)
