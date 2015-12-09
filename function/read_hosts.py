import abc
from base.base_hosts_function import base_hosts_function

class function(base_hosts_function):
    
    def __init__(self):
        pass
    
    def check_params(self, params):
        pass
    
    @abc.abstractmethod
    def func_run(self,params):
        try:
            os = self.get_os()
            
            path = self.get_host_path(os)

            self.read_hosts_content(path)
        except Exception as err:
            print(err)
            
        