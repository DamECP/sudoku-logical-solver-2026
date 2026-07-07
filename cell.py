from typing import List

class Cell:
    def __init__(self, cell_id, value, row, col, box):
        self.id = cell_id
        self.value = value
        self.row = row
        self.col = col
        self.box = box
        self.coord = (row, col)
        self.row_peers: list[Cell] = None
        self.col_peers: list[Cell] = None
        self.box_peers: list[Cell] = None
        self.peers: list[Cell] = None

        #candidates initialisation
        if self.value is None:
            self.candidates = set(range(1,10))
        else:
            self.candidates = set()
    
    @ property
    def is_solved(self):
        return self.value is not None
    
    
    def __repr__(self):
        candidates = sorted(self.candidates) if self.candidates is not None else "None"

        data = [f"id = {str(self.id)}",
                f"value = {str(self.value)}",
                f"candidates = {candidates}",
                f"row = {str(self.row)}",
                f"column = {str(self.col)}",
                f"coord = {str(self.coord)}",
                f"box = {str(self.box)}"]

        return "\n".join(i for i in data)

        

if __name__ == "__main__":
    pass