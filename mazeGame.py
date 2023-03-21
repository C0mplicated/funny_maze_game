##Maze Game
##maze.py
##Liaotianbao Zhang
##lzhang77
##section 2 

from graphics import*
from random import randrange

def story():#write the gamming title
    infile=open('story.txt','r')#IFL
    win=GraphWin("Maze",600,600)#GW
    win.setCoords(-8,-8,8,9)
    win.setBackground('pink')
    read=infile.readlines()
    im=Image(Point(0,-4),'albert.gif')
    im.draw(win)
    y=6
    for line in read:
        words=Text(Point(0,y),line)#OTXT
        words.setStyle('bold italic')
        words.setSize(15)
        words.setTextColor('green')
        y=y-1
        words.draw(win)
    inputbox=Entry(Point(4,1),9)#IEB
    inputbox.draw(win)
    win.getMouse()#IMS
    name=inputbox.getText()
    win.getMouse()#IMS
    win.close()
    infile.close()
    return name


def window(name):
    #build the window
    win = GraphWin("Maze",600,600)#GW
    win.setCoords(-8,-8,8,9)
    
    status=Text(Point(0,8.5),"move by using 'W,A,S,D'")#OTXT
    status.setTextColor('orange')
    status.draw(win)
    playerName=Text(Point(-7,8.5),name)#OTXT
    playerName.draw(win)
    return win,status

def functionalBlock(win):
    key=Text(Point(6.8,8.5),"Key:")#OTXT
    key.draw(win)
    num=0  
    keydisplay=Text(Point(7.5,8.5),str(num))
    keydisplay.draw(win)
    
    #draw the key
    key1=Rectangle(Point(-1,-7),Point(0,-6))
    key1.setFill('gold')
    key1.draw(win)
    key2=Rectangle(Point(2,2),Point(3,3))
    key2.setFill('gold')
    key2.draw(win)
    
    #draw the exit
    exit=Rectangle(Point(7,-6),Point(8,-5))
    exit.setFill('blue')
    exit.draw(win)
    
    #draw the obstacle
    obe1=Rectangle(Point(-3,-7),Point(-2,-6))
    obe1.setFill('red')
    obe1.draw(win)
    return num,keydisplay,key1,key2

def block(win):
    #draw the maze
    rect1=Rectangle(Point(-8,7),Point(8,8))
    rect1.setFill('black')
    rect1.draw(win)
    rect2=Rectangle(Point(-8,6),Point(-1,7))
    rect2.setFill('black')
    rect2.draw(win)
    rect3=Rectangle(Point(-8,5),Point(-5,6))
    rect3.setFill('black')
    rect3.draw(win)
    rect4=Rectangle(Point(-8,2),Point(-2,5))
    rect4.setFill('black')
    rect4.draw(win)
    rect5=Rectangle(Point(-8,-1),Point(-6,1))
    rect5.setFill('black')
    rect5.draw(win)
    rect6=Rectangle(Point(-8,-8),Point(-7,-1))
    rect6.setFill('black')
    rect6.draw(win)
    rect7=Rectangle(Point(-7,-8),Point(-5,-4))
    rect7.setFill('black')
    rect7.draw(win)
    rect8=Rectangle(Point(6,0),Point(8,7))
    rect8.setFill('black')
    rect8.draw(win)
    rect9=Rectangle(Point(2,-5),Point(8,0))
    rect9.setFill('black')
    rect9.draw(win)
    rect10=Rectangle(Point(0,-8),Point(8,-6))
    rect10.setFill('black')
    rect10.draw(win)
    rect11=Rectangle(Point(0,-6),Point(1,-1))
    rect11.setFill('black')
    rect11.draw(win)
    rect12=Rectangle(Point(-1,-1),Point(1,1))
    rect12.setFill('black')
    rect12.draw(win)
    rect13=Rectangle(Point(-5,-8),Point(0,-7))
    rect13.setFill('black')
    rect13.draw(win)
    rect14=Rectangle(Point(-2,-7),Point(-1,-2))
    rect14.setFill('black')
    rect14.draw(win)
    rect15=Rectangle(Point(-4,-6),Point(-2,-4))
    rect15.setFill('black')
    rect15.draw(win)
    rect16=Rectangle(Point(-6,-3),Point(-1,-2))
    rect16.setFill('black')
    rect16.draw(win)
    rect17=Rectangle(Point(-3,-3),Point(-2,1))
    rect17.setFill('black')
    rect17.draw(win)
    rect18=Rectangle(Point(-5,-2),Point(-3,0))
    rect18.setFill('black')
    rect18.draw(win)
    rect19=Rectangle(Point(0,4),Point(5,6))
    rect19.setFill('black')
    rect19.draw(win)
    rect20=Rectangle(Point(3,1),Point(5,4))
    rect20.setFill('black')
    rect20.draw(win)
    rect21=Rectangle(Point(0,2),Point(2,3))
    rect21.setFill('black')
    rect21.draw(win)
    rect22=Rectangle(Point(-5,1),Point(-4,2))
    rect22.setFill('black')
    rect22.draw(win)
    rect23=Rectangle(Point(0,1),Point(3,2))
    rect23.setFill('black')
    rect23.draw(win)
    rect24=Rectangle(Point(-2,2),Point(-1,3))
    rect24.setFill('black')
    rect24.draw(win)
    rect25=Rectangle(Point(-1,4),Point(0,5))
    rect25.setFill('black')
    rect25.draw(win)
    
def setPlayer(win):
    #set up the player
    player=Circle(Point(-7.5,1.5),0.5)
    player.setFill('lawngreen')
    player.draw(win)
    return player
        
class killerX:#CLOD
    
    def __init__ (self,color,center,dir=1):#moving obstacle
        self.circle=Circle(center,0.5)
        self.direction=dir
        self.circle.setFill(color)
    
    def draw(self,win):
        self.circle.draw(win)

    def move(self,win):
        if self.direction==1:
            self.circle.move(1,0)
      
        elif self.direction== -1:
            self.circle.move(-1,0)
        if self.circle.getCenter().getX()==-0.5:
            self.direction=-1
        elif self.circle.getCenter().getX()==-4.5:
            self.direction=1
            
    def getCenter(self,win):
        center=self.circle.getCenter()
        return center
    
    def changeColor(self,win):
        colors=['maroon','orange','yellow','mediumspringgreen','hotpink','magenta','navy']
        color=colors[randrange(0,7)] #RND
        self.circle.setFill(color)


    #the location where the player cannot go through
def locations():#LOOD
    walls=[(-8.5,1.5),(-7.5,2.5),(-6.5,2.5),(-5.5,2.5),(-4.5,2.5),(-3.5,2.5),(-2.5,2.5),(-1.5,2.5),
           (-4.5,1.5),(-7.5,0.5),(-6.5,0.5),(-2.5,0.5),(-0.5,0.5),(0.5,0.5),
           (-6.5,-0.5),(-4.5,-0.5),(-3.5,-0.5),(-2.5,-0.5),(-0.5,-0.5),(0.5,-0.5)
           ,(2.5,-0.5),(2.5,-0.5),(3.5,-0.5),(4.5,-0.5),(5.5,-0.5),(-7.5,-1.5)
           ,(-4.5,-1.5),(-2.5,-1.5),(0.5,-1.5),(2.5,-1.5),(-7.5,-2.5),(-5.5,-2.5)
           ,(-4.5,-2.5),(-3.5,-2.5),(-2.5,-2.5),(-1.5,-2.5),(0.5,-2.5),(2.5,-2.5)
           ,(-7.5,-3.5),(-1.5,-3.5),(0.5,-3.5),(2.5,-3.5),(-6.5,-4.5),(-5.5,-4.5)
           ,(-3.5,-4.5),(-2.5,-4.5),(-1.5,-4.5),(0.5,-4.5),(2.5,-4.5),(-6.5,-5.5)
           ,(-5.5,-5.5),(-3.5,-5.5),(-2.5,-5.5),(-1.5,-5.5),(0.5,-5.5),(3.5,-4.5)
           ,(4.5,-4.5),(5.5,-4.5),(6.5,-4.5),(7.5,-4.5),(-6.5,-6.5),(-5.5,-6.5)
           ,(-1.5,-6.5),(0.5,-6.5),(1.5,-6.5),(2.5,-6.5),(3.5,-6.5),(4.5,-6.5)
           ,(5.5,-6.5),(6.5,-6.5),(7.5,-6.5),(-4.5,-7.5),(-3.5,-7.5),(-2.5,-7.5)
           ,(-0.5,-7.5),(6.5,0.5),(0.5,1.5),(1.5,1.5),(2.5,1.5),(3.5,1.5),(4.5,1.5)
           ,(6.5,1.5),(0.5,2.5),(1.5,2.5),(3.5,2.5),(4.5,2.5),(6.5,2.5),(-2.5,3.5)
           ,(3.5,3.5),(4.5,3.5),(6.5,3.5),(-2.5,4.5),(-3.5,4.5),(-4.5,4.5),(-0.5,4.5)
           ,(0.5,4.5),(1.5,4.5),(2.5,4.5),(4.5,4.5),(6.5,4.5),(-5.5,5.5),(0.5,5.5)
           ,(1.5,5.5),(2.5,5.5),(3.5,5.5),(4.5,5.5),(6.5,5.5),(-4.5,6.5),(-3.5,6.5)
           ,(-2.5,6.5),(-1.5,6.5),(6.5,6.5),(-0.5,7.5),(0.5,7.5),(1.5,7.5),(2.5,7.5)
           ,(3.5,7.5),(4.5,7.5),(5.5,7.5),(8.5,-5.5)]
    
    keys1=[(-0.5,-6.5)]
    keys2=[(2.5,2.5)]
    exitPoint=[(7.5,-5.5)]
    obstacle=[(-2.5,-6.5)]
    return walls,keys1,keys2,exitPoint,obstacle
    

def movement(win,name,walls,keys1,keys2,exitPoint,obstacle,status,player,num,keydisplay,key1,key2,killer):
    #how to move the character
    fail=0
    while 0<1:
        keyString=win.getKey()
        status.setText('Yellow Keys, Red Trap, and Colorful Monster')
        
        if keyString=='w':
            killer.move(win)
            killer.changeColor(win)
            if (player.getCenter().getX(),player.getCenter().getY()+1) not in walls:#what happen if player move into the walls
                player.move(0,1)
                
                if str(player.getCenter()) ==str(killer.getCenter(win)):#what happen if player meet the killer
                    status.setText('You Lose! (click to play again)')
                    win.getMouse()
                    player.undraw()
                    player=Circle(Point(-7.5,1.5),0.5)
                    player.setFill('green')
                    player.draw(win)
                    num=0
                    keydisplay.setText(str(num))
                    fail=fail+1

        
        elif keyString=='a':
            killer.move(win)
            killer.changeColor(win)
            if (player.getCenter().getX()-1,player.getCenter().getY()) not in walls:#what happen if player move into the walls
                player.move(-1,0)
            
                if str(player.getCenter()) ==str(killer.getCenter(win)):#what happen if player meet the killer
                    status.setText('You Lose! (click to play again)')
                    win.getMouse()
                    player.undraw()
                    player=Circle(Point(-7.5,1.5),0.5)
                    player.setFill('green')
                    player.draw(win)
                    num=0
                    keydisplay.setText(str(num))
                    fail=fail+1
            
        elif keyString=="s":
            killer.move(win)
            killer.changeColor(win)
            if (player.getCenter().getX(),player.getCenter().getY()-1) not in walls:#what happen if player move into the walls
                player.move(0,-1)
                player.getCenter()
                if (player.getCenter().getX(),player.getCenter().getY()) in keys1:#what happen if player gets the keys
                    num=num+1
                    if num >2:
                        num=2
                    keydisplay.setText(str(num))
                    key1.undraw()
                elif (player.getCenter().getX(),player.getCenter().getY()) in keys2:#what happen if player gets the keys
                    num=num+1
                    if num >2:
                        num=2
                    keydisplay.setText(str(num))
                    key2.undraw()
            
        elif keyString=='d':
            killer.move(win)
            killer.changeColor(win)
            if (player.getCenter().getX()+1,player.getCenter().getY()) not in walls:#what happen if player move into the walls
                player.move(1,0)
                
                if (player.getCenter().getX(),player.getCenter().getY()) in obstacle:#what happen if player move into the trap
                    status.setText('You Lose! (click to play again)')
                    win.getMouse()
                    player.undraw()
                    player=Circle(Point(-7.5,1.5),0.5)
                    player.setFill('green')
                    player.draw(win)
                    num=0
                    keydisplay.setText(str(num))
                    fail=fail+1
                    
                elif str(player.getCenter()) ==str(killer.getCenter(win)):#what happen if player meet the killer
                    status.setText('You Lose! (click to play again)')
                    win.getMouse()#IMS
                    player.undraw()
                    player=Circle(Point(-7.5,1.5),0.5)
                    player.setFill('green')
                    player.draw(win)
                    num=0
                    keydisplay.setText(str(num))
                    fail=fail+1

                
                elif (player.getCenter().getX(),player.getCenter().getY()) in exitPoint:#what happen if player go through the exit point
                    break
            
    status.setText('You Win! (click to quit)')
    win.getMouse()#IMS
    win.close()
    outfile = open('scoreBoard.txt','a')#OFL
    print(name,'   ',num,'keys   ',fail,'fail',file=outfile)
    outfile.close()
    
def scoreBoard():#print the score
    infile=open('scoreBoard.txt','r')
    win=GraphWin("score",600,600)#GW
    win.setCoords(-8,-8,8,8)
    win.setBackground('pink')
    read=infile.readlines()
    t1=Text(Point(0,-7.5),'(click to quit)')#OTXT
    t1.setSize(16)
    t1.draw(win)
    y=6
    for line in read:
        words=Text(Point(0,y),line)#OTXT
        words.setStyle('bold italic')
        words.setSize(15)
        words.setTextColor('green')
        y=y-1
        words.draw(win)
    win.getMouse()#IMS
    win.close()
    infile.close()

def main():
    name=story()
    win,status=window(name)
    num,keydisplay,key1,key2=functionalBlock(win)#FNC
    killer=killerX('tan',Point(-2.5,5.5),1)
    killer.draw(win)
    block(win)
    player=setPlayer(win)
    walls,keys1,keys2,exitPoint,obstacle=locations()#FNC
    movement(win,name,walls,keys1,keys2,exitPoint,obstacle,status,player,num,keydisplay,key1,key2,killer)#FNC
    scoreBoard()
main()




    
            

    

