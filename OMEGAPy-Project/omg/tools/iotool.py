from sys import stdout,stdin

def nak_print(*args,flush=False,end='\n'):
    for i in args:
        stdout.write(i,flush=flush)
    
    stdout.write(end)

