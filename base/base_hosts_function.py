from base.base_function import function_base
import re,platform


class base_hosts_function(function_base):
    
    def get_host_path(self,os):
        path = "";
        os = os.lower()
        if os == "windows":
            path = "C:\\Windows\\System32\\drivers\\etc\\hosts"
        elif os == "linux":
            path = "/etc/hosts"
        else:
            raise ValueError("os specified error, try windows or linux.")
        return path
    
    def read_hosts_content(self,path):
        with open(path) as file_handler:
                for line in file_handler:
                    if line.startswith("#"):
                        pass
                    else:
                        line = line.strip()
                        if line != "":
                            print(line)
    
    def get_os(self):
        if "Windows" in platform.system():
            return "windows"
        elif "Linux" in platform.system():
            return "linux"
        else:
            raise ValueError("the os is not supported please email ljingfan159@163.com to report.")
    
    def is_os(self,string):
        pattern = re.compile("windows|linux",re.IGNORECASE)
        match = pattern.match(string)
        if match:
            return True
        else:
            return False
      
    def is_ip(self,string):
        pattern = re.compile("^(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[0-9]{1,2})(\.(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[0-9]{1,2})){3}$")  
        match = pattern.match(string)
        if match:
            return True
        else:
            return False  

    def match_ip_hostname(self,string,ip,hostname):
        if ip and hostname:
            p_str = ip + "\s*" + hostname
        elif ip:
            p_str = ip + "\s*.*"
        elif hostname:
            p_str = ".*\s*" + hostname
        
        pattern = re.compile("^" + p_str + "$")
        match = pattern.match(string)
        if match:
            return True
        else:
            return False
