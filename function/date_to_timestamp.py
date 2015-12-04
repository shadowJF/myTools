from base.base_function import function_base
import abc
import time

class function(function_base):
    
    def __init__(self):
        pass
    
    
    @abc.abstractmethod
    def func_run(self,params):
        try:
            self.check_params(params)
            date = params[0]
            ts = None
            if date == "now":
                ts = int(time.time())
            else:
                time_array = time.strptime(date,"%Y%m%d%H%M%S")
                ts = int(time.mktime(time_array))
            print(ts)
        except Exception as err:
            print(err)
            
        