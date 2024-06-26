# UTF-8
# Author: Mengdi Liu
# Date: 2024-6-25
# Function: Calculate the time cost of each process

import json

class FrameTimeCost:
    """计算平均吞吐量"""
    def __init__(self, data_file_path=None):
        self.data = None
        self.frame_num = 0
        self.frame_time_cost = []
        self.max_time = None
        self.min_time = None
        if data_file_path:
            self.load_data(data_file_path)
            self.frame_num = len(self.data)
            self.max_time = self.__get_max_time()
            self.min_time = self.__get_min_time()
            self.__get_frame_time_cost()


    def load_data(self, data_file_path):
        """加载数据文件，同时计算帧数、最大时间、最小时间"""
        with open(data_file_path, 'r') as f:
            self.data = json.load(f)
        self.data = sorted(self.data, key=lambda x: x[0], reverse=False)
        self.frame_num = len(self.data)
        self.max_time = self.__get_max_time()
        self.min_time = self.__get_min_time()
    
    def __get_max_time(self):
        """获取最大时间，即最后一帧的结束时间"""
        temp_data = self.data[:]
        last_frame = temp_data.pop()
        if last_frame[1]['ProcessA_end'] is None:
            max_time = last_frame[1]['ProcessB_end']
        else:
            max_time = last_frame[1]['ProcessA_end']
        return max_time

    def __get_min_time(self):
        """获取最小时间，即第一帧的开始时间"""
        temp_data = self.data[:]
        first_frame = temp_data.pop(0)
        if first_frame[1]['ProcessA_start'] is None:
            min_time = first_frame[1]['ProcessB_start']
        else:
            min_time = first_frame[1]['ProcessA_start']
        return min_time
    
    def __get_frame_time_cost(self):
        """获取每一帧的时间消耗"""
        for frame_info in self.data:
            if frame_info[1]['ProcessB_start'] is None:
                frame_time_cost = frame_info[1]['ProcessA_end'] - frame_info[1]['ProcessA_start']
            else:
                frame_time_cost = frame_info[1]['ProcessB_end'] - frame_info[1]['ProcessA_start']
            self.frame_time_cost.append(frame_time_cost)
    
    def get_average_throughput(self):
        """返回平均吞吐量"""
        return (self.frame_num / (self.max_time - self.min_time)) * 1000
    
    def get_acverage_frame_time_cost(self):
        """返回平均帧时间消耗"""
        return (sum(self.frame_time_cost)) / self.frame_num