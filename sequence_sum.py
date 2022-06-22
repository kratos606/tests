import sys,os
import threading
import json
from temp.program import *
def test_som(a):
    return a*((a+1)/2)
def test(i):
    return [som(i)==test_som(i),"not equal"]
def run():
    a = list(range(100))+[1000000000]
    for i in a:
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
