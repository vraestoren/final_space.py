from requests import Session

class FinalSpace:
	def __init__(self) -> None:
		self.api = "https://finalspaceapi.com/api/v0"
		self.session = Session()
		self.session.headers = {
			"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36",
			"accept": "application/json"
		}
	
	def get_endpoints(self) -> dict:
		return self.session.get(self.api).json()
	
	def get_character(self, character_id: int) -> dict:
		return self.session.get(
			f"{self.api}/character/{character_id}").json()
			
	def get_all_characters(self) -> dict:
		return self.session.get(f"{self.api}/character").json()
	
	def get_episode(self, episode_id: int) -> dict:
		return self.session.get(
			f"{self.api}/episode/{episode_id}").json()
			
	def get_all_episodes(self) -> dict:
		return self.session.get(f"{self.api}/episode").json()

	def get_location(self, location_id: int) -> dict:
		return self.session.get(
			f"{self.api}/locations/{location_id}").json()
			
	def get_all_locations(self) -> dict:
		return self.session.get(f"{self.api}/locations").json()
	
	def get_all_quotes(self) -> dict:
		return self.session.get(f"{self.api}/quote").json()
