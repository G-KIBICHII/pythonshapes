#!/usr/bin/env python
# coding: utf-8

# In[8]:


import turtle
class polygon:
    def __init__(self, sides,name, size):
        self.sides = sides
        self.name = name
        self.size =size
        self.interion_angles = (self.sides-2)*180
        self.angles = self.interion_angles/ self.sides
    def draw(self):
        for i in range(self.sides):
            turtle.forward(100)
            turtle.left(180-self.angles)
        turtle.done()
        
square= polygon(4,"square",100)
pentagon =polygon(5,"pentagon",100)
triangle = polygon(3,"triangle",100)
unknown = polygon(50,"unkown",10)
hexagon = polygon(5, "hexagon",20)
print(square.interion_angles)
print(square.angles)
square.draw()
#triangle.draw()




# In[ ]:





# In[ ]:




