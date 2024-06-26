# UTF-8
# Author: Mengdi Liu
# Date: 2024-6-25
# Function: Extract data from the log file
import re
import json

# from pathlib import Path

class DataExtract:
    """提取log文件中的数据，并将数据存入字典中，并提供输出json文件的功能"""
    def __init__(self, log_file_path=None):
        self.data = {}
        if log_file_path:
            self.extract_data(log_file_path)

    def extract_lines(self, log_file_path):
        """读取log文件的每一行"""
        with open(log_file_path, 'r') as f:
            lines = f.readlines()
        return lines
    
    def extract_data(self, log_file_path):
        """提取log文件中的数据"""
        lines = self.extract_lines(log_file_path)

        # 正则表达式提取数据
        pattern = re.compile(r'static_multistream\|frame_id:(\d+)\|timestamp:-1\|cpu:\d+\|(\w+):(\w+):(\d+)')
        for line in lines:
            try:
                data = pattern.search(line)
                # 如果匹配到数据，将数据存入字典
                # 字典结构：{frame_id: {ProcessA_start: xxx, ProcessA_end: xxx, ProcessB_start: xxx, ProcessB_end: xxx}, ...}
                if data:
                    frame_id = data.group(1)
                    elaspe_name = data.group(2)
                    elaspe_label = data.group(3)
                    elaspe_time = data.group(4)
                    if frame_id not in self.data:
                        self.data[frame_id] = {}
                        self.data[frame_id]['ProcessA_start'] = None
                        self.data[frame_id]['ProcessA_end'] = None
                        self.data[frame_id]['ProcessB_start'] = None
                        self.data[frame_id]['ProcessB_end'] = None
                    if elaspe_name == 'ProcessA':
                        if elaspe_label == 'start':
                            self.data[frame_id]['ProcessA_start'] = int(elaspe_time)
                        else:
                            self.data[frame_id]['ProcessA_end'] = int(elaspe_time)
                    elif elaspe_name == 'ProcessB':
                        if elaspe_label == 'start':
                            self.data[frame_id]['ProcessB_start'] = int(elaspe_time)
                        else:
                            self.data[frame_id]['ProcessB_end'] = int(elaspe_time)
            except:
                print('There are something wrong when extracting data from the log file.')
                # pass
        self.data = sorted(self.data.items(), key=lambda x: x[0], reverse=False)
        return self.data
    
    def output_json(self, output_json_path):
        """将提取的数据输出到json文件"""
        with open(output_json_path, 'w') as f:
            f.write(json.dumps(self.data, indent=4))
