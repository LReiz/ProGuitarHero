from config import (
	MIN_NOTE_FREQUENCY,
	MIN_NOTE_ID,
	BASE_NOTES_ARRAY,
	MIN_VOLUME
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


def volume_too_low(sig):
	if max(sig) < abs(MIN_VOLUME):
		return True

	return False