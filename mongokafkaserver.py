from rattlepy import rattlepy
import aiohttp


class MyServerApplication(rattlepy.RattlePyApplication):

	def prepare_routes(self):
		"""
		Register custom routes.
		:return:
		"""
		self.Routes.append(aiohttp.web.get("/v", self.version))

	async def version(self, request):
		"""
		A simple endpoint that returns JSON response.
		:param request: request
		:return: response
		"""
		return aiohttp.web.json_response({"v": 1})


if __name__ == '__main__':
	app = MyServerApplication()
	app.serve()
