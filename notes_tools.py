from config import (
	MIN_NOTE_FREQUENCY,
	MIN_NOTE_ID,
	BASE_NOTES_ARRAY,
	PYAUDIO_FORMATS
)

from math import (
	log,
)

def find_note_id(frequency):
	return round(log( frequency/MIN_NOTE_FREQUENCY , 2**(1/12) ) + MIN_NOTE_ID)


def find_note_string(id):
	baseNote = BASE_NOTES_ARRAY[id % 12]
	noteFamily = int(id/12)

	return (str(baseNote) + str(noteFamily))


def volume_too_low(sig, min_volume):
	if abs(max(sig)) < min_volume or abs(min(sig)) < min_volume:
		return True

	return False


# For plugged guitar only (not mic)

def convert_to_32bit_array(byteArray, pyaudio_format):
	array32Bits = b''
	bytesPerNumber = PYAUDIO_FORMATS[pyaudio_format]

	for index in range(0, len(byteArray), bytesPerNumber):
		intNumber = int.from_bytes(byteArray[index:index + bytesPerNumber], byteorder='big', signed=False)
		num32Bits = intNumber.to_bytes(4, byteorder='big')
		array32Bits += num32Bits

	return array32Bits