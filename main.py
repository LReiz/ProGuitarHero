import sys
import audio_recorder
from audio_processor import process_audio_forever

from config import INPUT_DEVICE

def main():
	if len(sys.argv) > 1 and (sys.argv[1]).lower() == "debug":
		audio_recorder.AudioRecorder().showDevices()
	else:
		microphone = audio_recorder.AudioRecorder(INPUT_DEVICE)
		process_audio_forever(microphone)


if __name__ == '__main__':
	main()