from requests import Session

class FinalSpace:
	def __init__(self) -> None:
		self.api = "https://finalspaceapi.com/api/v0"
		self.session = Session()
		self.session.headers = {
			"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36",
			"accept": "application/json"
		}
	
	def _get(self, endpoint: str) -> dict:
		return self.session.get(endpoint).json()

	def get_endpoints(self) -> dict:
		return self._get(self.api)

	def get_character(self, character_id: int) -> dict:
		return self._get(f"{self.api}/character/{character_id}")
			
	def get_all_characters(self) -> dict:
		return self._get(f"{self.api}/character")
	
	def get_episode(self, episode_id: int) -> dict:
		return self._get(f"{self.api}/episode/{episode_id}")
			
	def get_all_episodes(self) -> dict:
		return self._get(f"{self.api}/episode")

	def get_location(self, location_id: int) -> dict:
		return self._get(f"{self.api}/locations/{location_id}")
			
	def get_all_locations(self) -> dict:
		return self._get(f"{self.api}/locations")
	
	def get_all_quotes(self) -> dict:
		return self._get(f"{self.api}/quote")
