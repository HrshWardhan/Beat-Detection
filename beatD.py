import scipy.io.wavfile, numpy, sys, subprocess
import time
le_multi = 0.023219955 # Local energy multiplier ~ 1024/44100
def sumsquared(arr):
    sum = 0.0
    for k in arr:
            i=k/10000
            sum += ((i[0] * i[0]) + (i[1] * i[1]))
    return sum

def var(queue):
    var = 0.0
    avg = le_multi*local(queue)
    j=0
    for i in queue:
        j+=1
        var += (i-avg)*(i-avg)
    var/=j
    return var    
    
def local(queue):
    sum = 0.0
    j=0
    for i in queue:
        sum += i
        j+=1    
    return sum

if sys.argv.__len__() < 2:
    print ('USAGE: wavdsp <wavfile>')
    sys.exit(1)

numpy.set_printoptions(threshold=sys.maxsize)
rate, data = scipy.io.wavfile.read(sys.argv[1])

data_len = data.__len__()
idx = 0
hist_last = 44032
queue = []
instant_energy = 0
local_energy = 0

foo = []
i=0
while idx < data_len - 48000:
    if idx>44032:
        dat = data[idx:idx+1024]
        instant_energy = sumsquared(dat)
        queue.pop(0)
        queue.append(instant_energy)
        local_energy = le_multi * local(queue)
        #print(var(queue))
        c = (-0.0025714*var(queue))+1.5142857
        #print str(c*local_energy) + " " + str(instant_energy) 
        if (instant_energy > (local_energy*3.5)):
            i+=1
            #print str(c*local_energy) + " " + str(instant_energy) 
            foo.append((1.0*idx)/44100)
            print ((1.0*idx)/44100)
        idx = idx + 1024
    else:
        dat = data[idx:idx+1024]
        instant_energy = sumsquared(dat)
        queue.append(instant_energy)
        idx = idx + 1024
#p.terminate()

sum = 0.0
j=1
prev=0
for i in foo: 
    #print int(i) 
    if(int(i) is prev):
        j+=1
        sum+=i
    else:
        #print sum/j
        sum=i        
        j=1
        prev=int(i)
