import pyaudio
from config import (
	SAMPLE_RATE,
	CHANNELS,
	SAMPLE_PER_FRAME,
	FORMAT
)

import numpy as np
from audio_processor import (
	freq_from_autocorr
)

class AudioRecorder():
	def __init__(self, microphone=True):
		if microphone:
			self.frameProvider = getFrameProviderFromMicrophone()

	def getFrameProviderFromMicrophone(self):
		pyaudioInstance = pyaudio.PyAudio()

		streamMicrophone = pyaudioInstance.open(rate=SAMPLE_RATE,
												channels=CHANNELS,
												format=FORMAT,
												input=True)

		return streamMicrophone

	def getFrame(self):
		frame = self.frameProvider.read(SAMPLE_PER_FRAME)
		return frame