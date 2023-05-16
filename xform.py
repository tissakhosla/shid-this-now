'''handle data transformations'''

def timelength(ms):
    '''format ms into length of time'''
    print(ms)
    t = [(ms/1000)//3600, ((ms/1000)%3600)//60, (ms/1000)%60]
    for i, v in enumerate(t):
        t[i] = '0' + str(int(v)) if v < 10 else str(int(v))
    return f'{t[0]}:{t[1]}:{t[2]}'
