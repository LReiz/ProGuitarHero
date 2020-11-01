import pyaudio



# DEVICES CONFIGURATION --------------------------------------------------------

INPUT_DEVICE = 2             # 1 for Microphone / 2 for Guitar
MICROPHONE = 1
GUITAR = 2

# PC MICROPHONE

INPUT_SAMPLE_RATE_MIC = 22050
INPUT_CHANNELS_MIC = 1
INPUT_SAMPLE_PER_FRAME_MIC = 1024
INPUT_FORMAT_MIC = pyaudio.paInt16
INPUT_DEVICE_INDEX_MIC = None

# MY GUITAR

INPUT_SAMPLE_RATE_GUITAR = 44100
INPUT_CHANNELS_GUITAR = 1
INPUT_SAMPLE_PER_FRAME_GUITAR = 1024
INPUT_FORMAT_GUITAR = pyaudio.paInt24
INPUT_DEVICE_INDEX_GUITAR = 10

# SPEAKERS

OUTPUT_SAMPLE_RATE = 44100
OUTPUT_CHANNELS = 1                     # 1 MONO / 2 STEREO
OUTPUT_SAMPLE_PER_FRAME = 1024
OUTPUT_FORMAT = pyaudio.paInt16

MIN_VOLUME_MIC = 15000
MIN_VOLUME_GUITAR = 10000000

# NOTES -----------------------------------------------------------------------

# NOTES IDs
# Considering C0 = 0
MIN_NOTE_ID = 28		# E2
MAX_NOTE_ID = 62		# D5

# NOTES

MIN_NOTE_FREQUENCY = 82.406876		# E2 (Hz)

# MUSICS MAP

BASE_NOTES_ARRAY = ['C','C#','D','D#','E','F','F#','G','G#','A','A#','B']


# GENERAL ---------------------------------------------------------------------

PYAUDIO_FORMATS = {
    16  :   1,          # paInt8    (1byte)
    8   :   2,          # paInt16   (2bytes)
    4   :   3,          # paInt24   (3bytes)
    2   :   4,          # paInt32   (4bytes)
}