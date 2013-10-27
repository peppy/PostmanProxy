from libmproxy import controller, proxy
from request import Request
from collection import Collection
import os

class CollectionCreatorProxy(controller.Master):
	def __init__(self, server, collection, rules):
		self.collection = collection
		self.rules = rules
		controller.Master.__init__(self, server)

	def run(self):
		try:
			return controller.Master.run(self)
		except KeyboardInterrupt:
			self.shutdown()

	def handle_request(self, msg):
		request = Request(self.collection.id)
		request.init_from_proxy(msg)

		self.collection.add_request(request)

		msg.reply()

	def handle_response(self, msg):
		msg.reply()