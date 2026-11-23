import os
from WinequalityMachineLearningProject import logger
from WinequalityMachineLearningProject.entity.config_entity import DataValidationConfig
import pandas as pd                                            

from WinequalityMachineLearningProject.entity.config_entity import (
    DataValidationConfig,
)


class DataValiadtion:
    def __init__(self, config: DataValidationConfig):
        self.config = config

    def validate_all_columns(self) -> bool:
        actual_columns = pd.read_csv(
            self.config.unzip_data_dir,
            sep=";",
            nrows=0,
        ).columns.tolist()
        expected_columns = list(self.config.all_schema)
        validation_status = actual_columns == expected_columns

        with open(self.config.STATUS_FILE, "w", encoding="utf-8") as status_file:
            status_file.write(f"Validation status: {validation_status}")

        if not validation_status:
            raise ValueError(
                f"Wine CSV columns do not match the schema. "
                f"Expected {expected_columns}, got {actual_columns}."
            )

        return validation_status