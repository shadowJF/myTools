from stringtool.time.timestamp import timestamp

def timestamp_run(var,func):
    obj = timestamp(var,func)
    
    if func == "timestamp":
        obj.get_timestamp()
    elif func == "date":
        obj.get_date()