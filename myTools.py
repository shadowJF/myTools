from optparse import OptionParser
import sys
'''
author:liangjfc@yonyou.com
date:2015-12-01
'''

if __name__=="__main__":
    parser = OptionParser(usage="usage: myTools.py -f arg1 arg2 ...",version="%prog 1.0") 
    
    help_message = '''Specify the function you want to use.\n Functions available for now are as follows:
    ====================================================
    encoding: encoding a string in specified encoding. You can specify an encoding type,default in utf-8.
                use like: -f encoding fanfan gbk or -f encoding fanfan
    ====================================================
    decoding: decoding a bytes in specified encoding. You can specify an encoding type,default in utf-8.
                use like: -f decoding \\xEA\\xA3 gbk or -f decoding \\x13\\xB2 
    ====================================================
    date_to_timestamp: transform date to timestamp.
                use like -f date_to_timestamp 20151003200300 or -f date_to_timestamp now
    ====================================================
    timestamp_to_date: transform timestamp to date.
                use like -f timestamp_to_date 1447854652 or -f timestamp_to_date now'''
    
    
    parser.add_option("-f", "--function", action="store", dest="function",
                            help=help_message)
    
    
    (option,args) = parser.parse_args()

    if option.function is None:
        print("usage: " + parser.usage)
        print("to find functions you can use: use -h for help")
        sys.exit(1)
    
    try:
        function_module = __import__("function.%s" % option.function, fromlist=["function"])
        function = function_module.function()
        function.func_run(args)
    except Exception as err:
        print(err)
   
        