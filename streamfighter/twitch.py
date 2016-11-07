from lxml import html
import requests

class TwitchSnippet():
	def __init__(self,twitch_url):
		htmlPage = requests.get(twitch_url)

		self.htmlObject = html.fromstring(htmlPage.content)
		self.twitch_url = twitch_url


	def getBroadcasterAvatar(self):
		# broadcasterElement = self.htmlObject.xpath("//div[@class='js-broadcaster-info']")
		return ""


	def getBroadcasterName(self):
		broadcasterElement = self.htmlObject.xpath("//meta[@property='og:title']/@content")
		broadcasterName = ""
		if len(broadcasterElement) > 0:
			broadcasterName = broadcasterElement.pop().split(' ')[0]
		return broadcasterName

	def getEmbed(self):
		return 'https://clips.twitch.tv/embed?clip=' + self.twitch_url.split('https://clips.twitch.tv/').pop()

	def getGame(self):
		return ""
		# gameElement = self.htmlObject.find_class('js-broadcaster-info')[0]
		# print(gameElement)
		# return gameElement

	def getPoster(self):
		videoElement = self.htmlObject.xpath("//meta[@name='twitter:image']/@content")
		posterUrl = ""
		if len(videoElement) > 0:
			posterUrl = videoElement[0]
		return posterUrl

	def getTwitchUrl(self):
		return self.twitch_url