import logging
import os
import sys

log_dir = 'logs'
log_str = "[%(asctime)s : %(levelname)s : %(module)s : %(message)s]"
log_filename = os.path.join(log_dir, 'looping.log')
os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format=log_str,
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler(log_filename)
    ]
)

logger = logging.getLogger('Toxic-comment-analyser')
