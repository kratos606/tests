import sys,os
import threading
import json
from temp.program import *
def test_fib(a):
    x,y=0,1
    for i in range(a):
        x,y=y,x+y
    return x
def test(i):
    return [fib(i)==test_fib(i),"not equal"]
def run():
    for i in range(100):
        try:
            x,y=test(i)
            if x:
                print(json.dumps({'passed':True}))
            else:
                print(json.dumps({'passed':False,'message':y}))
        except Exception as e:
            print(json.dumps({'passed':False,'message':str(e)}))
    t2.cancel()
def runtime():
    if t.is_alive():
        print(json.dumps({'passed':False,'message':"This solution takes too long"}))
        os._exit(0)
if __name__ == '__main__':
    t = threading.Thread(target=run)
    t2 = threading.Timer(5, runtime) 
    t.daemon = True
    t.start()
    t2.start()
