import sys
from pathlib import Path

# Adds the root project directory to the python path
root_dir = Path(__file__).resolve().parent.parent
sys.path.append(str(root_dir))

from src.load.db import get_engine

engine = get_engine()

with engine.connect() as conn:
    print("Connected successfully!")