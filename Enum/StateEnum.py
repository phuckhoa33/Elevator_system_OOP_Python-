from enum import Enum

class ElevatorState(Enum):
    SLEEP_TIME = 'sleep'
    MOVE_TOP = 'move_top'
    MOVE_DOWN = 'move_down'