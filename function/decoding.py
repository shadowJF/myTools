from base.base_function import function_base
import abc

class function(function_base):
    
    def __init__(self):
        pass
    
    
    @abc.abstractmethod
    def func_run(self,params):
        try:
            bytesstr = params[0]
            if len(params) == 2:
                encoding = params[1]
            else:
                encoding = "utf-8"
            tmp = bytesstr.replace("\\x","")
            bytes_data = bytes.fromhex(tmp)
            str_data = bytes_data.decode(encoding)
            print(str_data)
        except Exception as err:
            print(err)
            print("may be encoding error, try use -c to specify an encoding")
            
        