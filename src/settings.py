import os
from pathlib import Path  # Python 3.6+ only

from dotenv import load_dotenv

project_dir = os.path.join(os.path.dirname(__file__), os.pardir)
dotenv_path = os.path.join(project_dir, '.env')
load_dotenv(dotenv_path)

DB_ADDRESS = os.getenv("DB_ADDRESS")
