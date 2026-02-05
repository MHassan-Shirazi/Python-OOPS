# # # Class, Attribute, Method

# # # class Factory:
# # #     a = 10 # attribute

# # #     def hello(self): # method
# # #         print("How are you")  

# # # print(Factory().a)

# # # Factory().hello()


# # ## Object
# # ## Object is a instance

# # # class Factory:
# # #     a = 10 # attribute

# # #     def hello(self): # method
# # #         print("How are you")  

# # # obj = Factory()  # Object

# # # print(obj.a)

# # # obj.hello()


# # ## self => Constructor

# # class Factory:
# #     def __init__(self,material,zips,pockets):
# #         self.material = material
# #         self.zips = zips
# #         self.pockets = pockets

# #     def show(self):
# #         print(f"your object details are {self.material} , {self.zips} , {self.pockets}")


# # nike = Factory("Leather",3,2)

# # campus = Factory("nyloan" , 3,3)

# # # print(campus.pockets)

# # # nike.show()

# ## TYPES OF ATTRIBUTES

# class Animal:
#     name = "lion" ## class attriute

#     def __init__(self, age):
#         self.age = age  ## instance attribute

#     def show(self):
#         print("how are you")

#     ## decorators

#     @classmethod  
#     def hello(cls):
#         print("how are you")

#     @staticmethod
#     def static():
#         print("How are you")

# obj = Animal(12)

