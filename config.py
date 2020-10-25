import pyaudio

# AUDIO CONFIGURATION

SAMPLE_RATE = 22050
SAMPLE_PER_FRAME = 1024

CHANNELS = 1
FORMAT = pyaudio.paInt16

# NOTES IDs

# Considering C0 = 0
MIN_NOTE_ID = 28		# E2
MAX_NOTE_ID = 62		# D5

# NOTES

MIN_NOTE_FREQUENCY = 82.406876		# E2 (Hz)

# MUSICS MAP

BASE_NOTES_ARRAY = ['C','C#','D','D#','E','F','F#','G','G#','A','A#','B']

E2 = 