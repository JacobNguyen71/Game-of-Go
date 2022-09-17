from board_base import GO_POINT, NO_POINT
from board import GoBoard

DEFAULT_KOMI = 6.5

class GoEngine:
    def __init__(self, name: str, version: float) -> None:
        """
        name : name of the player used by the GTP interface
        version : version number used by the GTP interface
        """
        self.name: str = name
        self.version: float = version
        self.komi: float = DEFAULT_KOMI

    def get_move(self, board: GoBoard, color: int) -> GO_POINT:
        """
        name : name of the player used by the GTP interface
        version : version number used by the GTP interface
        """
        #get the empty points of this board
        emptyPoints = board.get_empty_points()

        #if there are empty points...
        if len(emptyPoints > 0):
            #return the first point in that list
            return emptyPoints[0]
        else:
            return NO_POINT
        