"""Contains functionality related to Weather"""
import logging


logger = logging.getLogger(__name__)


class Weather:
    """Defines the Weather model"""

    def __init__(self):
        """Creates the weather model"""
        self.temperature = 70.0
        self.status = "sunny"

    def process_message(self, message):
        """Handles incoming weather data"""
        
        # Process incoming weather messages. Set the temperature and status.
        weather_json_data = json.loads(message.value())
        try:
            self.temperature = weather_json['temperature']
            self.status = weather_json['status']
        except:
            logger.info("weather process_message is incomplete - skipping")