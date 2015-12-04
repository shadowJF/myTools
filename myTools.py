from optparse import OptionParser
import sys
'''
author:liangjfc@yonyou.com
date:2015-12-01
'''

if __name__=="__main__":
    parser = OptionParser(usage="usage: %prog -f arg1 arg2 ...",version="%prog 1.0") 
    
    help_message = '''Specify the function you want to use.\n Functions available for now are as follows:
    ====================================================
    encoding: encoding a string in specified encoding. You can specify an encoding type,default in utf-8.
                use like: -f encoding fanfan gbk or -f encoding fanfan
    ====================================================
    decoding: decoding a bytes in specified encoding. You can specify an encoding type,default in utf-8.
                use like: -f decoding \\xEA\\xA3 gbk or -f decoding \\x13\\xB2 
    ====================================================
    date_to_timestamp: transform date to timestamp.
                use like: -f date_to_timestamp 20151003200300 or -f date_to_timestamp now
    ====================================================
    timestamp_to_date: transform timestamp to date.
                use like: -f timestamp_to_date 1447854652 or -f timestamp_to_date now
    ====================================================
    read_hosts: read contents of file "hosts". You can specify the os,default in windows.            
                use like: -f read_hosts or -f read_hosts linux 
    ====================================================
    add_hosts: add host (ip hostname) into file hosts.
                use like: -f add hosts ip hostname
    ====================================================
    delete_hosts: delete host from hosts file. You can specify an ip or a hostname to delete all hosts related to that or delete
                the specific host by specify ip and hostname
                use like: -f delete_hosts 10.2.3.5 or -f delete_hosts 10.3.4.5 jingfan.com '''
    
    
    
    parser.add_option("-f", "--function", action="store", dest="function",
                            help=help_message)
    
    
    (option,args) = parser.parse_args()

    if option.function is None:
        parser.print_usage()
        print("to find functions you can use: use -h for help")
        sys.exit(1)
    
    try:
        function_module = __import__("function.%s" % option.function, fromlist=["function"])
        function = function_module.function()
        function.run(args)
    except Exception as err:
        print(err)
   
        