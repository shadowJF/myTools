from optparse import OptionParser
from stringtool.characterencode import run

if __name__=="__main__":
    parser = OptionParser() 
    parser.add_option("-e", "--encode", action="store", dest="encode_string",
                            help="encode the string in specific character encoding (default in utf-8)")
    parser.add_option("-c", "--character", action="store", dest="encoding",
                            help="the character encoding used by encode or decode function")
    parser.add_option("-d", "--decode",action="store", dest="decode_string",
                            help="decode the string in specific character encoding (default in utf-8)")
    
    (option,args) = parser.parse_args()
    
    used = False
    
    if option.encode_string is not None:
        if option.encoding is not None:
            encoding = option.encoding
        else:
            encoding = "utf-8"
        run(option.encode_string,"encode",encoding)
        used = True
    
    if option.decode_string is not None:
        if option.encoding is not None:
            encoding = option.encoding
        else:
            encoding = "utf-8"
        run(option.decode_string,"decode",encoding)
        used = True
    
    if used is False:
        print("no arguments found, please use myTools.py -h for help!\n")
        