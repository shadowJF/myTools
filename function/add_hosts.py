import abc
from base.base_hosts_function import base_hosts_function

class function(base_hosts_function):
    
    def __init__(self):
        pass
    
    def check_params(self, params):
        if len(params) < 2:
            raise ValueError("ip and hostname should be specified.")
    
    @abc.abstractmethod
    def func_run(self,params):
        try:
            os = "windows"
            if params is not None and len(params) == 3 :
                os = params[0]
                ip = params[1]
                hostname = params[2]
            else:
                ip = params[0]
                hostname = params[1]
            
            path = self.get_host_path(os)

            with open(path,"a") as file_handler:
                file_handler.write(ip + "\t" + hostname + "\n")
            print("host added succeed: " + ip + "\t" + hostname + "\n")
            print("now the hosts file is:")
            
            self.read_hosts_content(path)
        except Exception as err:
            print(err)
            
        