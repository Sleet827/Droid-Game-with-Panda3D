from ipgetter2 import IPGetter

getter = IPGetter()

def myip():
    return str(getter.get().v4)
