from optparse import OptionParser
import sys
'''
author:liangjfc@yonyou.com
date:2015-12-01
'''

if __name__=="__main__":
    parser = OptionParser(usage="usage: %prog -f arg1 arg2 ...",version="%prog 1.0") 
    
    help_message = '''Specify the function you want to use.\n Functions available for now are as follows:
    =+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+
    Function: encoding
    ----------------------------------------------------
    Describe: encoding a string in specified encoding. You can specify an encoding type,default in utf-8.
    ----------------------------------------------------
    use like: -f encoding fanfan gbk or -f encoding fanfan
    =+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+
    Function: decoding
    ----------------------------------------------------
    Describe: decoding a bytes in specified encoding. You can specify an encoding type,default in utf-8.
    ----------------------------------------------------
    use like: -f decoding \\xEA\\xA3 gbk or -f decoding \\x13\\xB2 
    =+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+
    Function: date_to_timestamp
    ----------------------------------------------------
    Describe: transform date to timestamp.
    ----------------------------------------------------
    use like: -f date_to_timestamp 20151003200300 or -f date_to_timestamp now
    =+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+
    Function: timestamp_to_date
    ----------------------------------------------------
    Describe: transform timestamp to date.
    ----------------------------------------------------
    use like: -f timestamp_to_date 1447854652 or -f timestamp_to_date now
    =+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+
    Function: read_hosts
    ----------------------------------------------------
    Describe: read contents of file "hosts". 
    ----------------------------------------------------            
    use like: -f read_hosts 
    =+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+
    Function: add_hosts
    ----------------------------------------------------
    Describe: add host (ip hostname) into file hosts.
    ----------------------------------------------------
    use like: -f add_hosts ip hostname 
    =+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+
    Function: delete_hosts
    ----------------------------------------------------
    Describe: delete host from hosts file. You can specify ip or hostname or both to delete hosts related to it 
    ----------------------------------------------------
    use like: -f delete_hosts 10.2.3.5 or -f delete_hosts 10.3.4.5 jingfan.com or -f delete_hosts jingfan.com'''
    
    
    
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
   
        