import abc,os
from base.base_hosts_function import base_hosts_function

class function(base_hosts_function):
    
    def __init__(self):
        pass
    
    def check_params(self, params):
        if len(params) < 1 or len(params) > 2:
            raise ValueError("at least one ip or one hostname should be specified and no more arguments.")
    
    @abc.abstractmethod
    def func_run(self,params):
        try:
            opsys = self.get_os()
            ip = None
            hostname = None
            if len(params) == 2:
                ip = params[0]
                hostname = params[1]
            elif len(params) == 1:
                if self.is_ip(params[0]):
                    ip = params[0]
                else:
                    hostname = params[0]
               
            path = self.get_host_path(opsys)

            with open(path,"r") as reader,open(path+".tmp","w") as writer:
                for line in reader:
                    if not line.startswith("#"):
                        line_strip = line.strip()
                        if self.match_ip_hostname(line_strip,ip,hostname):
                            continue
                    writer.write(line) 
            
            os.remove(path)
            os.rename(path+".tmp",path)
            
            print("host deleted succeed.\n")
            print("now the hosts file is:")
            self.read_hosts_content(path)
        except Exception as err:
            print(err)
            
        