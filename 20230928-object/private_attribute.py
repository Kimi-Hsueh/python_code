class Person:
    def __init__(self,name:str,wight:int,height:int):
        self.__name = name #將name改為private_attribute(read only狀態)
        self.__weight = wight
        self.height = height

    @property #property ->將設定值設定為read only，不可以更改
    def weight(self) ->int:
        return self.__weight
    @property
    def getBMI(self) ->float:  
        return self.bmi() #此行去執行method的bmi運算並回傳
    #method
    def bmi(self) ->float:
        return f'BMI={round(self.__weight/(self.height/100)**2,ndigits=2)}'

    def __str__(self) -> str:
        return f"name={self.__name}\nweight={self.__weight}\nheight={self.height}"
    

if __name__ == '__main__':
    p1 = Person("kimi",74,172)
    p1.__name="vivian" #此行未動態更改是因為name這個attribute被設定為read only了
    #p1.weight=99  #此行會出現錯誤狀態"AttributeError: can't set attribute"，代表在這個class裡面，是不可以被更改的
    print(p1)
    print(p1.getBMI) #getBMI是單項的指令，利用property的getBMI變數去method進行計算