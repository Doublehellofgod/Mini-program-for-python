class Example:
    def __init__(self, name='Плоская',name2='Керамика',cen=10):
        self.__name=name
        self.__name2=name2
        Example.count = cen;
    
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name=name
        
    @property
    def name2(self):
        return self.__name2
    @name2.setter
    def name2(self, name2):
        self.__name2=name2
        
    @staticmethod
    def printNameProperty(_example):
        print('Тип плитки: '+ _example.name+'\nМатериал: '+_example.name2)
 
example=Example('Плоская',' Керамика',100)
Example.printNameProperty(example)
print ('Цена за штуку: '+str(example.count))
