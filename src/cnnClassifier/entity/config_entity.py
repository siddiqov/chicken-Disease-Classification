import os
from dataclasses import dataclass
from pathlib import Path
import yaml

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path

#class DataIngestionConfig:
#    def __init__(self, root_dir: Path, source_URL: str, local_data_file: Path, unzip_dir: Path):
#        self.root_dir = root_dir
#        self.source_URL = source_URL
#        self.local_data_file = local_data_file
#        self.unzip_dir = unzip_dir
