from base.base_function import function_base
import abc

class function(function_base):
    
    def __init__(self):
        pass
    
    
    @abc.abstractmethod
    def func_run(self,params):
        try:
            str_data = params[0]
            if len(params) == 2:
                encoding = params[1]
            else:
                encoding = "utf-8"
            bytes_data = str_data.encode(encoding)
            print(bytes_data)
        except Exception as err:
            print(err)
            print("may be encoding error, try use -c to specify an encoding")
            
        