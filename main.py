import audio_recorder
from audio_processor import process_audio_forever


def main():
	microphone = audio_recorder.AudioRecorder()
	process_audio_forever(microphone)


if __name__ == '__main__':
	main()