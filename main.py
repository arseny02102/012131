class People():
    n=0
    def __init__ (self,name=0,profession=0,age=0,weight=0,rost=0,sex=0,IQ=0):
        self.name=name
        self.profession=profession
        self.age=age
        self.weight=weight
        self.rost=rost
        self.sex=sex
        self.IQ=IQ
p1 = People('Rostislav','Преподаватель',"30",'70','190','M','200')
print(getattr(p1,'name'))
print(getattr(p1,'IQ'))
