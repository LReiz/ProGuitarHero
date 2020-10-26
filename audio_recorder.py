import pyaudio
from config import (
	INPUT_SAMPLE_RATE,
	INPUT_CHANNELS,
	INPUT_SAMPLE_PER_FRAME,
	INPUT_FORMAT
)

import numpy as np
from audio_processor import (
	freq_from_autocorr
)

class AudioRecorder():
	def __init__(self, microphone=True):
		if microphone:
			self.frameProvider = self.getFrameProviderFromMicrophone()

	def getFrameProviderFromMicrophone(self):
		pyaudioInstance = pyaudio.PyAudio()

		streamMicrophone = pyaudioInstance.open(rate=INPUT_SAMPLE_RATE,
												channels=INPUT_CHANNELS,
												format=INPUT_FORMAT,
												input=True)

		print('recording...')
		return streamMicrophone

	def getFrame(self):
		frame = self.frameProvider.read(INPUT_SAMPLE_PER_FRAME)
		return frame