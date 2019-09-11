from DKClasses.MySingleton import MySingleton

x = MySingleton()
print("Here x.y equals to %d" %x.y)
x.y = 20
z = MySingleton()
print("Here z.y equals to %d" %z.y)