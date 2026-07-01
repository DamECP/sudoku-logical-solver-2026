class Cell:
    def __init__(self, cell_id, value, row, col, box):
        self.id = cell_id
        self.value = value
        self.row = row
        self.col = col
        self.box = box
        self.row_peers = None
        self.col_peers = None
        self.box_peers = None
        self.peers = None

        #candidates initialisation
        if self.value is None:
            self.candidates = set(range(1,10))
        else:
            self.candidates = set()
    
    def __repr__(self):
        candidates = sorted(self.candidates) if self.candidates is not None else "None"

        data = [f"id = {str(self.id)}",
                f"value = {str(self.value)}",
                f"candidates = {candidates}",
                f"row = {str(self.row)}",
                f"column = {str(self.col)}",
                f"box = {str(self.box)}"]

        return "\n".join(i for i in data)

        

if __name__ == "__main__":
    test = set()
    print(bool(test))