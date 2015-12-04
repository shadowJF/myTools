import abc

class function_base(object):
    __metaclass__ = abc.ABCMeta

    
    def run(self,params):
        self.check_params(params)
        self.func_run(params)

    def check_params(self,params):
        if len(params) == 0:
            raise ValueError("Arguments error, no arguments added after function.")
    
    @abc.abstractmethod    
    def func_run(self,params):
        pass