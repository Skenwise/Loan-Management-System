# project_root/config/__init__.py
from dotenv import load_dotenv
import os
import sys

# Load .env file
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '..', '.env'))

# Add project root to sys.path for absolute imports
PROJECT_ROOT = os.environ.get('PROJECT_ROOT')
if PROJECT_ROOT:
    sys.path.insert(0, PROJECT_ROOT)