import requests
import json
import logging
import time
from .constants import API_URL, DEFAULT_RETRY_COUNT, DEFAULT_RETRY_DELAY, REQUEST_TIMEOUT

class ExchangeRateProvider:
       def __init__(self, retry_count=DEFAULT_RETRY_COUNT, retry_delay=DEFAULT_RETRY_DELAY):
        self.retry_count = retry_count
        self.retry_delay = retry_delay
        self._logger = self._setup_logger()
        self._rates_cache = None
    
    def _setup_logger(self):
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.INFO)
        if not logger.handlers:
            handler = logging.StreamHandler()
            formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
            handler.setFormatter(formatter)
            logger.addHandler(handler)
        return logger
    
    def get_rates(self):
        if self._rates_cache:
            return self._rates_cache
            
        for attempt in range(self.retry_count):
            try:
                response = requests.get(API_URL, timeout=REQUEST_TIMEOUT)
                response.raise_for_status()
                data = response.json()
                self._rates_cache = data['rates']
                return self._rates_cache
            except (requests.exceptions.RequestException, json.JSONDecodeError, KeyError) as e:
                self._logger.warning(f"Attempt {attempt + 1}/{self.retry_count} failed: {e}")
                if attempt < self.retry_count - 1:
                    time.sleep(self.retry_delay)
                else:
                    self._logger.error("All retries exhausted")
                    raise
        return None