class Snake():
    
    def __init__(self, n: int) -> None:
        self.maze = self.createMatrixNxN(n)
        self.createDirEnum()
        self.pos = [0, -1]
        self.dir = self.right
        self.turnCount = 0
        self.laidEgg = 0
        self.border = n

    def createMatrixNxN(self, n: int) -> list:
        return [[0]*n for _ in range(n)]
    
    def goStraight(self) -> None:
        if self.dir == self.left: self.pos[1] -= 1
        elif self.dir == self.right: self.pos[1] += 1
        elif self.dir == self.up: self.pos[0] -= 1
        elif self.dir == self.down: self.pos[0] += 1
            
    def goBack(self) -> None:
        if self.dir == self.left: self.pos[1] += 1
        elif self.dir == self.right: self.pos[1] -= 1
        elif self.dir == self.up: self.pos[0] += 1
        elif self.dir == self.down: self.pos[0] -= 1
            
    def turnRight(self) -> None:
        self.turnCount += 1
        if self.dir == self.left: self.dir = self.up
        elif self.dir == self.right: self.dir = self.down
        elif self.dir == self.up: self.dir = self.right
        elif self.dir == self.down: self.dir = self.left
        
    def createDirEnum(self) -> None:
        self.left, self.right, self.up, self.down = range(4)
        
    def layEgg(self) -W Nonne:
        self.turnCount = 0
        self.laidEgg += 1
        self.maze[self.pos[0]][self.pos[1]] = self.laidEgg
    
    def meetDeadEnd(self) -> bool:
        return self.turnCount >= 2
    
    def meetWall(self) -> bool:
        if self.pos[0] == self.border or self.pos[1] == self.border:
            return True
        if self.maze[self.pos[0]][self.pos[1]] != 0:
            return True
        return False
        
        
def spiralNumbers(n: int) -> list:
    snake = Snake(n)
    b = True
    while b:
        snake.goStraight()
        if snake.meetWall():
            snake.goBack()
            snake.turnRight()
        else:
            snake.layEgg()
        if snake.meetDeadEnd():
            b = False
    return snake.maze