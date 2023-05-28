#!/usr/bin/env python
# coding: utf-8

# In[2]:


from car import Car
#ElectricCar类需访问父类Car

class Battery():
    """模拟电动汽车电瓶"""
    
    def __init__(self,battery_size = 70):
        self.battery_size = battery_size
    
    def describe_battery(self):
        """打印电瓶容量信息"""
        print("This car has a "+ str(self.battery_size) + "-KWh battery.")
        
    def get_range(self):
        """打印电瓶续航里程"""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size ==85:
            range =270
        
        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)
        
    def upgrade_battery(self):
        """电瓶升级"""
        if self.battery_size != 85:
            self.battery_size = 85


# In[3]:


class ElectricCar(Car):
    def __init__(self,make,model,year):
        """初始化父类的属性，再初始化电动汽车特有属性"""
        super().__init__(make,model,year)
        self.battery_size = 70
        self.battery = Battery()#创建一个新的battery实例,默认值为70
    
    def describe_battery(self):
        """打印电瓶容量的信息"""
        print("This car has a " + str(self.battery_size) + "-KW/h battery.")
    
    def fill_gas_tank():
        """电动汽车没有油箱"""
        print("This car doesn't need a gas tank!")
        #当对电动汽车调用方法fill_gas_tank()时python将忽略Car类中的方法转而用上述代码


# In[ ]:





# In[ ]:




