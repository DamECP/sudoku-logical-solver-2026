from collections.abc import Iterable

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

    @property
    def is_solved(self):
        return self.value is not None
    
    def solve(self, value:int) -> None:
        if self.is_solved:
            raise ValueError(f"Cell : {self.id} ({self.coord}) already solved (current value = {self.value})")
        
        self.value = value
        self.candidates.clear()

    def reduce_candidates(self) -> None:
        peers_values = {peer.value for peer in self.peers if peer.is_solved}
        self.candidates -= peers_values

    def remove_candidates(self, candidates:int |Iterable[int]) -> bool:
        before = self.candidates.copy()
        if isinstance(candidates, int):
            candidates = {candidates}
        else:
            candidates = set(candidates)

        self.candidates -= candidates
        return before != self.candidates


    def __repr__(self):
        candidates = sorted(self.candidates) if self.candidates is not None else "None"

        data = [f"id = {str(self.id)}",
                f"value = {str(self.value)}",
                f"candidates = {candidates}",
                f"row = {str(self.row)}",
                f"column = {str(self.col)}",
                f"box = {str(self.box)}",
                "\n"]

        return "\n".join(i for i in data)