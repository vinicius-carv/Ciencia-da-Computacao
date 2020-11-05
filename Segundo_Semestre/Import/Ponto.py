import math
class Ponto(object):
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
    def __str__(self):
        s=str(self.x)+str(self.y)
        return s
    def getx(self):
        return self.x
    def gety(self):
        return self.y
    def setx(self,x):
        self.x=x
    def sety(self,y):
        self.y=y
    def distancia(self,p2):
        dist=math.sqrt(((self.x-p2.x)**2)+((self.y-p2.y)**2))
if __name__ == '__main__':
    p1=Ponto()
    print(Ponto.getx(p1)," ",Ponto.gety(p1))
    p2=Ponto(2,3)
    p3=Ponto(4)
    p4=Ponto(y=8)
