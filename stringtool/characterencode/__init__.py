from stringtool.characterencode.character import character

def character_run(var,func,encoding):
    ch = character(var,func,encoding)
    
    if func == "encode":
        ch.encode()
    elif func == "decode":
        ch.decode()