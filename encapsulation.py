class Myclass:
    __name = '' #private attribute
    __roll = '' #private attribute
    _address = '' #protected
    
    def set_name(self,name):    #set method
        self.__name = name

    def display_name(self):     #get method
        return self.__name
    
    def set_roll(self,roll):    #set method
        self.__roll = roll
    
    def display_roll(self):     #get method
        return self.__roll
    
    def __say_hello(self):
        print('hello')
    
    def public_function(self):
        self.__say_hello()
        #or return self.__say_hello()
    
m1 = Myclass()
m1.set_name('shanta')
print(m1.display_name())
m1.set_roll(1183)
print(m1.display_roll())
m1.public_function()
#m1._Myclass__say_hello() #this is one way to access private function