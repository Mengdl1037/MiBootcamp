# UTF-8
# Author: Liu Mengdi
# Date: 2024-06-21
# Function:

class Car:
    """⼀次模拟汽⻋的简单尝试"""
    def __init__(self, make, model, year):
        """初始化描述汽⻋的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """返回格式规范的描述性名称"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        """打印⼀个句⼦，指出汽⻋的⾏驶⾥程"""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """将⾥程表读数设置为给定的值"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """让⾥程表读数增加给定的量"""
        self.odometer_reading += miles

class Battery:
    """⼀次模拟电动汽⻋电池的简单尝试"""
    def __init__(self, battery_size=40):
        """初始化电池的属性"""
        self.battery_size = battery_size

    def describe_battery(self):
        """打印⼀条描述电池容量的消息"""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """打印⼀条消息，指出电池的续航⾥程"""
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225
        return range
    
    def upgrade_battery(self):
        """升级电池容量"""
        if self.battery_size == 40:
            self.battery_size = 65
            print("Upgraded the battery to 65 kWh.")
        else:
            print("The battery is already upgraded.")


class ElectricCar(Car):
    """电动汽⻋的独特之处"""
    def __init__(self, make, model, year):
        """
        先初始化⽗类的属性，再初始化电动汽⻋特有的属性
        """
        super().__init__(make, model, year)
        self.battery = Battery()

    def fill_gas_tank(self):
        """电动汽⻋没有油箱"""
        print("This car doesn't have a gas tank!")


my_car = ElectricCar('wuling', 'hongguang', 2021)
print("车的续航里程是 %d 公里。" % my_car.battery.get_range())
# 升级电池容量:
my_car.battery.upgrade_battery()
print("车的续航里程是 %d 公里。" % my_car.battery.get_range())