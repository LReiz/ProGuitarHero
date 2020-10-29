import pyaudio
from config import (
	INPUT_SAMPLE_RATE_MIC,
	INPUT_CHANNELS_MIC,
	INPUT_SAMPLE_PER_FRAME_MIC,
	INPUT_FORMAT_MIC,
	INPUT_DEVICE_INDEX_MIC,

	INPUT_SAMPLE_RATE_GUITAR,
	INPUT_CHANNELS_GUITAR,
	INPUT_SAMPLE_PER_FRAME_GUITAR,
	INPUT_FORMAT_GUITAR,
	INPUT_DEVICE_INDEX_GUITAR
)

import numpy as np
from audio_processor import (
	freq_from_autocorr
)

class AudioRecorder():
	def __init__(self, microphone=True):
		if microphone:
			self.frameProvider = self.getFrameProviderFromMicrophone()
			self.input_sample_rate = INPUT_SAMPLE_RATE_MIC
			self.input_channels = INPUT_CHANNELS_MIC
			self.input_sample_per_frame = INPUT_SAMPLE_PER_FRAME_MIC
			self.input_format = INPUT_FORMAT_MIC
		else:
			self.frameProvider = self.getFrameProviderFromGuitar()
			self.input_sample_rate = INPUT_SAMPLE_RATE_GUITAR
			self.input_channels = INPUT_CHANNELS_GUITAR
			self.input_sample_per_frame = INPUT_SAMPLE_PER_FRAME_GUITAR
			self.input_format = INPUT_FORMAT_GUITAR


	def getFrameProviderFromMicrophone(self):
		pyaudioInstance = pyaudio.PyAudio()

		streamMicrophone = pyaudioInstance.open(rate=INPUT_SAMPLE_RATE_MIC,
												channels=INPUT_CHANNELS_MIC,
												format=INPUT_FORMAT_MIC,
												input_device_index=INPUT_DEVICE_INDEX_MIC,
												input=True)

		print('Mic recording...')
		return streamMicrophone


	def getFrameProviderFromGuitar(self):
		pyaudioInstance = pyaudio.PyAudio()

		streamGuitar = pyaudioInstance.open(rate=INPUT_SAMPLE_RATE_GUITAR,
												channels=INPUT_CHANNELS_GUITAR,
												format=INPUT_FORMAT_GUITAR,
												input_device_index=INPUT_DEVICE_INDEX_GUITAR,
												input=True)

		print('Guitar recording...')
		return streamGuitar


	def getFrame(self):
		frame = self.frameProvider.read(self.input_sample_per_frame, exception_on_overflow=False)
		return frame