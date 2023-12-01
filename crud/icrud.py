from abc import ABC , abstractmethod

class Icrud(ABC):
	@abstractmethod
	def create(self, **kwargs):
		raise NotImplementedError

	@abstractmethod
	def read(self, **kwargs):
		raise NotImplementedError

	@abstractmethod
	def update(self, **kwargs):
		raise NotImplementedError
	
	@abstractmethod
	def relation(self, **kwargs):
		raise NotImplementedError

	@abstractmethod
	def delete(self, **kwargs):
		raise NotImplementedError