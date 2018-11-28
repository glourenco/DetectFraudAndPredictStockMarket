class GameCharacter:
    name = ""
    maxHP = 0
    currHP = 0
    xPos = 0

    def __init__(self,name,maxHP,xPos):
        self.name = name
        self.maxHP = maxHP
        self.currHP = maxHP
        self.xPos = xPos

    def changeHP(self,changInHP):
        self.currHP += changInHP
        if self.currHP > self.maxHP:
            self.currHP = self.maxHP
        elif self.currHP < 0:
            self.currHP = 0
    def changeXPos(self,changeXPos):
        self.xPos += changeXPos
     

newGameCharacter = GameCharacter("Lourenco",100,1)
print(newGameCharacter.name)
print(newGameCharacter.currHP)
print(newGameCharacter.xPos)
newGameCharacter.changeHP(-50)
print(newGameCharacter.currHP)


class PlayerChar(GameCharacter):
    lives = 0 
    inventory = [] 

    def __init__(self,name,maxHP,xPos): 
        super(PlayerChar,self).__init__(name,maxHP,xPos)
        self.lives = 3
        self.inventory = ["shirt","pants"]
    def addItem(self,item):
        self.inventory.append(item)
    
    def changeHP(self,changeInHP):
        super(PlayerChar,self).changeHP(changeInHP)
        if self.currHP <=0:
            self.lives -= 1
            if self.lives < 0:
                self.lives = 0

newPlayer = PlayerChar("Goncalo",150,10)
print(newPlayer.currHP)
print(newPlayer.lives)
print(newPlayer.inventory)
newPlayer.addItem("knife")
print(newPlayer.inventory)
newPlayer.changeHP(-200)
print(newPlayer.lives)
newPlayer.changeHP(-200)
print(newPlayer.lives)
newPlayer.changeHP(-200)
print(newPlayer.lives)
newPlayer.changeHP(-200)
print(newPlayer.lives)
