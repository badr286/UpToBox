from requests import get

class uptobox:

	def __init__(self, token):
		self.token = token
		self.prefix = 'https://uptobox.com/api/'


	def file_info(self,file_code):
		res = get(self.prefix+"link/info?fileCodes="+file_code).json()
		res = res['data']['list'][0]
		res['file_size'] = str(round(res['file_size'] /8/1000/1024, 2)) + ' mb' # 8 bits = byte , 1000 byte = kb , 1024 kb = mb

		return res

	def download_url(self,file_code):
		res = get(self.prefix+f"link?token={self.token}&file_code={file_code}").json()
		
		if 'waitingToken' in res['data'].keys():
			waitingToken = res['data']['waitingToken']
			sleep_time = res['data']['waiting']

			sleep(sleep_time)

			res = get(self.prefix+f"link?token={self.token}&file_code={file_code}&waitingToken="+waitingToken).json()

		return res['data']['dlLink']


