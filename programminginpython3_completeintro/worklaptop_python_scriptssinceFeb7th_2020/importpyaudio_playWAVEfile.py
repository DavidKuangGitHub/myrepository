"""importpyaudio_playWAVEfile.py => _pydub.py
py importpyaudio_playWAVEfile.py file_example_WAV_10MG.wav
"""
import urllib.request
from pydub import AudioSegment
from pydub.playback import play
# Download an audio file
#urllib.request.urlretrieve("https://tinyurl.com/wx9amev", "metallic-drums.wav")
# Load into PyDub
#loop = AudioSegment.from_wav("metallic-drums.wav")
loop = AudioSegment.from_wav("file_example_WAV_10MG.wav")
# Play the result
play(loop)


"""import pyaudio
import wave
import sys

CHUNK = 1024

if len(sys.argv) < 2:
    print("Plays a wave file.\n\nUsage: %s filename.wav" % sys.argv[0])
    sys.exit(-1)

wf = wave.open(sys.argv[1], 'rb')

p = pyaudio.PyAudio()

stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                channels=wf.getnchannels(),
                rate=wf.getframerate(),
                output=True)

data = wf.readframes(CHUNK)

while data != '':
    stream.write(data)
    data = wf.readframes(CHUNK)

stream.stop_stream()
stream.close()

p.terminate()"""