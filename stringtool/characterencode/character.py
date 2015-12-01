import binascii

class character:
    
    def __init__(self,var,func,characterencoding):
        if func == "encode":
            self.str = var
            self.byte = None
        else:
            var = var.replace("\\x","")
            self.byte = bytes.fromhex(var)
            self.str = None
        self.encoding = characterencoding
            
    
    def encode(self):
        try:
            if not self.byte:
                self.byte = self.str.encode(self.encoding)
            print(self.byte)
        except Exception as err:
            print(err)
            print("may be encoding error, try use -c to specify an encoding")
            
    def decode(self):
        try:
            if not self.str:
                self.str = self.byte.decode(self.encoding)
            print(self.str)
        except Exception as err:
            print(err)
            print("may be encoding error, try use -c to specify an encoding")