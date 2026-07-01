class Cell:
    def __init__(self, value, row, col):
        self.value = value
        self.row = row
        self.col = col
        self.box = self.calculate_box(row, col)
        self.row_peers = None
        self.col_peers = None

        #candidates initialisation
        if self.value is None:
            self.candidates = set(range(1,10))
        else:
            self.candidates = None

    def calculate_box(row, col):
        return 3 * (row // 3) + (col // 3)
        
