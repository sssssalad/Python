#!/usr/bin/env python
# coding: utf-8

# ### 作为一个模块使用

# In[2]:


"""一个可用于表示汽车的类"""

class Car():
    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 25
    
    def get_descriptive_name(self):
        """返回简洁描述性信息"""
        long_name = str(self.year) + " " +self.make + " " + self.model
        return long_name.title()
    
    def read_odometer(self):
        """打印汽车里程信息"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")
        
    def update_odometer(self, mileage):
        """
        将里程表读数设置为指定的值
        禁止将里程表往回调
        """
        if mileage>=self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
        
    def increment_odometer(self,miles):
        """将里程表读书增加指定的量"""
        if miles>=0:
            self.odometer_reading += miles
        else:
            print("You can't roll back an odometer!")


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



class ElectricCar(Car):
    def __init__(self,make,model,year):
        """初始化父类的属性，再初始化电动汽车特有属性"""
        super().__init__(make,model,year)
        self.battery = Battery()#创建一个新的battery实例




