class Phone:
    def call(self):
        print('You can call')
    def message(self):
        print('You can message')
class iphone (Phone):
    def Photo(self):
        print('You can take photo')

pro_14 = iphone()
pro_14.call()
pro_14.message()
pro_14.Photo()