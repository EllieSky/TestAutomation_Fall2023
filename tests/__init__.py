import os

BROWSER = 'chrome'
DEFAULT_WAIT = 5

DOMAIN = 'http://hrm-online.portnov.com'
BASE_URL = f'{DOMAIN}/symfony/web/index.php'

ADMIN_USER = 'admin'
PASSWORD = 'password'


TEST_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.dirname(TEST_DIR)
TEST_RESULTS = os.path.join(PROJECT_DIR, 'test_results')


