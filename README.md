# Beat-Detection
Requires numpy,scipy
run the BeatD.py giving the location of song in .wav format as parameter
for ex "python BeatD.py song.wav"
the output will be shown on terminal itself
same for Frq.py 
just replace BeatD.py with Frq.py


there are two different codes submitted BeatD works on raw amplitude variation in audio file to detect beat whereas Frq.py works in Fourier 
Domain comparing amplitude of frequencies where bass lies although latter should be more precise but due to issues with amplitude of wave being
returned i was not able to add variance factors to code thus it messes up at some places.

Implementaion based on http://www.flipcode.com/misc/BeatDetectionAlgorithms.pdf 

Further Improvements :
Ratio of amplitude of local energy and current energy is fixed in these codes which can be improved by varing it with variance to get better 
detection
