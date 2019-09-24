import time
#Scheduler_nonStopper.py 
#f = open("NonStopper.log","w+")

howMuchTime = 3
i=0
while 1:
  try:
    i = i + 1;
    if i == howMuchTime:
      break
    
    print("Saved Stability {} time(s).".format(str(i)))
    p = open("NonStopper.log","a+")
    #for i in range(10):
    #  f.write("This is line %d\r\n" % (i+1))
    p.write("Saved Stability Execution.\n")
    p.close()
    time.sleep(5)
  
#f.close()
  except Exception as e:
    print(e.args)
    pass
