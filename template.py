import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

# List of files to create (now a variable)
list_of_files = [
    "src/__init__.py",
    "src/helper.py",
    "src/prompt.py",
    ".env",
    "setup.py",
    "research/trials.ipynb",
    "static/style.css",
    "app.py",
    "store_index.py",
    "templates/chat.html"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    # Create directories if needed
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)  # exist_ok prevents errors if they already exist
        logging.info(f"Creating directory: {filedir}")

    # Create or check files
    try:
        if not os.path.exists(filepath) or os.path.getsize(filepath) == 0:
            with open(filepath, "w") as f:
                pass  # Create an empty file
            logging.info(f"Creating empty file: {filepath}")
        else:
            logging.info(f"File already exists: {filepath}")
    except Exception as e:
        logging.error(f"Error creating file {filepath}: {e}")
