import soundfile as sf
from ttsmms import TTS

tts = TTS("../data/hin")
wav = tts.synthesis("मेरे कंधे पर अपना सिर मत रखो")
from IPython.display import Audio

# Audio(wav["x"], rate=wav["sampling_rate"])
# Save the audio to a WAV file
sf.write('output.wav', wav["x"], wav["sampling_rate"])