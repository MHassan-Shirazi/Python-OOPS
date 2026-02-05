class Factory:   ## grand parent
    def __init__(self, material,zips):
        self.material = material
        self.zips = zips

class KarachiFactory(Factory):  
    def __init__(self,material,zips,color):
        super().__init__(material,zips)
        self.color = color

class LahoreFactory(KarachiFactory): 
    def __init__(self, material, zips, color,pockets):
        super().__init__(material, zips, color)
        self.pockets = pockets
        

obj = LahoreFactory("Pents",2,"black",2)
obj2 = LahoreFactory("Tshirt",3,"white",1)

print(obj.material)    
print(obj2.pockets)   