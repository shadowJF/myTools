from optparse import OptionParser
from stringtool.characterencode import character_run
from stringtool.time import timestamp_run
'''
author:liangjfc@yonyou.com
date:2015-12-01
'''

if __name__=="__main__":
    parser = OptionParser() 
    parser.add_option("-e", "--encode", action="store", dest="encode_string",
                            help="encode the string in specific character encoding (default in utf-8)")
    parser.add_option("-c", "--character", action="store", dest="encoding",
                            help="the character encoding used by encode or decode function")
    parser.add_option("-d", "--decode",action="store", dest="decode_string",
                            help="decode the string in specific character encoding (default in utf-8)")
    parser.add_option("-t","--timestamp", action="store", dest="date_str",
                            help="transform date(20151223081022) to timestamp, use 'now' to represent current time")
    parser.add_option("-a","--date", action="store", dest="timestamp_str",
                            help="transform timestamp to date, use 'now' to represent current time")
    
    (option,args) = parser.parse_args()
    
    used = False
    
    if option.encode_string is not None:
        if option.encoding is not None:
            encoding = option.encoding
        else:
            encoding = "utf-8"
        character_run(option.encode_string,"encode",encoding)
        used = True
    
    if option.decode_string is not None:
        if option.encoding is not None:
            encoding = option.encoding
        else:
            encoding = "utf-8"
        character_run(option.decode_string,"decode",encoding)
        used = True
        
    if option.date_str is not None:
        timestamp_run(option.date_str, "timestamp")
        used = True
    
    if option.timestamp_str is not None:
        timestamp_run(option.timestamp_str, "date")
        used = True
    
    if used is False:
        print("no arguments found, please use myTools.py -h for help!\n")
        