import scipy.io.wavfile
import numpy
import sys


def sumsquared(arr):
    sum = 0.0
    krr = (arr[:, 0] + 1j * arr[:, 1])
    ff = numpy.fft.fft(krr)
    brr = []
    for i in range(0,6):
        sum += abs(ff[i])
    return sum


def local(queue):
    ret = 0.0
    for i in queue:
        ret += i
    return ret/len(queue)


def var(queue):
    var = 0.0
    avg = local(queue)
    j = 0
    for i in queue:
        j += 1
        var += (i-avg)*(i-avg)
    var /= j
    return var


if sys.argv.__len__() < 2:
    print('USAGE: wavdsp <wavfile>')
    sys.exit(1)

numpy.set_printoptions(threshold=sys.maxsize)
rate, data = scipy.io.wavfile.read(sys.argv[1])
data_len = data.__len__()
idx = 0
hist_last = 44032
queue = []
instant_energy = 0

count = 0.0
while idx < data_len - 48000:
    if idx > 44032:
        dat = data[idx:idx+1024]
        foo = sumsquared(dat)
        queue.append(foo)
        queue.pop(0)
        local_energy = local(queue)
   	c = 2.5
        flag = False
        if (c*local_energy < foo):
            flag = True
        if flag:
            print((1.0*idx)/44100)
            count += 0
        idx = idx + 1024
    else:
        dat = data[idx:idx+1024]
        instant_energy = sumsquared(dat)
        queue.append(instant_energy)
        idx = idx + 1024
