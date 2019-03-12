#!/usr/bin/env python
# -*- coding: utf-8 -*-

from models.Exceptions 	import InterfaceInitError
from gpiozero 			import LED
from libraries 			import usb_pixel_ring_v1 	as pixel_ring
from models.Interface 	import Interface

class RespeakerMicArrayV1(Interface):

	def __init__(self, numLeds):
		super(RespeakerMicArrayV1, self).__init__(numLeds)

		self._leds = pixel_ring.find()

		if self._leds is None:
			raise InterfaceInitError('Respeaker Mic Array V1 not found')

		self._power 	= LED(5)
		self._colors 	= self._newArray()


	def setPixel(self, ledNum, red, green, blue, brightness):
		"""
		Mic array v1 is BGR!!
		"""
		if ledNum < 0 or ledNum >= self._numLeds:
			self._logger.warning('Trying to access a led index out of reach')
			return

		index = ledNum * 4
		self._colors[index] = blue
		self._colors[index + 1] = green
		self._colors[index + 2] = red
		self._colors[index + 3] = brightness


	def setPixelRgb(self, ledNum, color, brightness):
		self.setPixel(ledNum, color[0], color[1], color[2], brightness)


	def clearStrip(self):
		self._colors = self._newArray()
		self._leds.off()


	def show(self):
		self._leds.show(self._colors)


	def setVolume(self, volume):
		self._leds.set_volume(volume)


	def _newArray(self):
		return [0, 0, 0, 0] * self._numLeds