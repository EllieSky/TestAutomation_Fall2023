import os
from configparser import ConfigParser


TEST_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.dirname(TEST_DIR)
TEST_RESULTS = os.path.join(PROJECT_DIR, 'test_results')

TEST_ENV = os.environ.get('TEST_ENV') or 'test'

config = ConfigParser()
config.read(os.path.join(PROJECT_DIR, 'config.ini'))

BROWSER = 'chrome'
DEFAULT_WAIT = config.get(TEST_ENV, 'DEFAULT_WAIT')

DOMAIN = config.get(TEST_ENV, 'DOMAIN')
BASE_URL = f'{DOMAIN}/symfony/web/index.php'

ADMIN_USER = config.get(TEST_ENV, 'ADMIN_USERNAME')
PASSWORD = config.get(TEST_ENV, 'DEFAULT_ADMIN_PASSWORD')




