from pathlib import Path

from lib.data_extract import DataExtract

log_file_path = Path('.\\data_repo\\test_data.log')
data_extract = DataExtract()
data_extract.extract_data(log_file_path)
data_extract.output_json(Path('.\\data_repo\\test_data.json'))
