class Test():
    def __init__(self, v: int=0, i: int=1) -> None:
        self.v = v
        self.i = i
    
    def increase(self) -> None:
        self.v += self.i

    def __repr__(self) -> str:
        return str(self.v)
