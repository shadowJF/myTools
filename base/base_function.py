import abc

class function_base(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def func_run(self,params):
        pass
