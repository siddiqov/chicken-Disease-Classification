import os
import urllib.request
import zipfile
from pathlib import Path
from cnnClassifier.entity.config_entity import DataIngestionConfig
from cnnClassifier import logger

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self):
        logger.info("Starting file download...")
        if not os.path.exists(self.config.local_data_file):
            filename, headers = urllib.request.urlretrieve(self.config.source_URL, self.config.local_data_file)
            logger.info(f"File {filename} downloaded successfully with headers: {headers}")
        else:
            logger.info(f"File already exists at {self.config.local_data_file}")

    def extract_zip_file(self):
        logger.info("Starting file extraction...")
        if not os.path.exists(self.config.unzip_dir):
            os.makedirs(self.config.unzip_dir)
        
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(self.config.unzip_dir)
        logger.info(f"Files extracted to {self.config.unzip_dir}")
