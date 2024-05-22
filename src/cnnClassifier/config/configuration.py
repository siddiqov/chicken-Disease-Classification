from pathlib import Path
from cnnClassifier.constants import *
from cnnClassifier.utils.common import read_yaml, create_directories
from cnnClassifier.entity.config_entity import DataIngestionConfig

CONFIG_FILE_PATH = Path("config/config.yaml")
PARAMS_FILE_PATH = Path("params.yaml")

class ConfigurationManager:
    def __init__(self, config_filepath=CONFIG_FILE_PATH, params_filepath=PARAMS_FILE_PATH):
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        create_directories([Path(self.config['artifacts_root'])])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config['data_ingestion']
        create_directories([Path(config['root_dir'])])
        return DataIngestionConfig(
            root_dir=Path(config['root_dir']),
            source_URL=config['source_URL'],
            local_data_file=Path(config['local_data_file']),
            unzip_dir=Path(config['unzip_dir'])
        )
