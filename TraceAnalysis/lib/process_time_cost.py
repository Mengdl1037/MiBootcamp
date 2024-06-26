# UTF-8
# Author: Mengdi Liu
# Date: 2024-6-25
# Function: Calculate the time cost of each process

import json

class ProcessTimeCost:
    """计算每个工序的时间消耗，并提供平均耗时、99分位耗时、90分位耗时的计算"""
    def __init__(self, data_file_path=None):
        """初始化，
        ProcessA_time_cost为字典，以 帧id 为主键，保存 ProcessA 的时间消耗，
        ProcessB_time_cost为字典，以 帧id 为主键，保存 ProcessB 的时间消耗。
        """
        self.ProcessA_time_cost = {} # {frame_id: ProcessA_time_cost, ...}
        self.ProcessB_time_cost = {} # {frame_id: ProcessB_time_cost, ...}
        if data_file_path:
            self.calculate_time_cost(data_file_path)

    def calculate_time_cost(self, data_file_path):
        """计算每个工序的时间消耗，并将结果存入字典中和列表中"""
        with open(data_file_path, 'r') as f:
            data = json.load(f)
        
        # data为嵌套列表，但是仍然可以用如下方式进行遍历（为什么？？）
        for frame_id, info in data:
            self.ProcessA_time_cost[frame_id] = {}
            self.ProcessB_time_cost[frame_id] = {}

            # 计算ProcessA的时间消耗
            if info['ProcessA_start'] is None:
                self.ProcessA_time_cost[frame_id] = None
            else:
                self.ProcessA_time_cost[frame_id] = info['ProcessA_end'] - info['ProcessA_start']
                
            # 计算ProcessB的时间消耗
            if info['ProcessB_start'] is None:
                self.ProcessB_time_cost[frame_id] = None
            else:
                self.ProcessB_time_cost[frame_id] = info['ProcessB_end'] - info['ProcessB_start']
    
    def get_ProcessA_time_cost(self):
        """返回ProcessA的时间消耗字典"""
        return self.ProcessA_time_cost
    
    def get_ProcessB_time_cost(self):
        """返回ProcessB的时间消耗字典"""
        return self.ProcessB_time_cost
    
    def get_ProcessA_average_time_cost(self):
        """返回ProcessA的平均时间消耗"""
        temp = [value for value in self.ProcessA_time_cost.values() if value is not None]
        return sum(temp) / len(temp)
    
    def get_ProcessB_average_time_cost(self):
        """返回ProcessB的平均时间消耗"""
        temp = [value for value in self.ProcessB_time_cost.values() if value is not None]
        return sum(temp) / len(temp)
    
    def get_ProcessA_p99_time_cost(self):
        """返回ProcessA的99分位时间消耗"""
        temp = [value for value in self.ProcessA_time_cost.values() if value is not None]
        temp.sort()
        return temp[int(len(temp) * 0.99)]
    
    def get_ProcessB_p99_time_cost(self):
        """返回ProcessB的99分位时间消耗"""
        temp = [value for value in self.ProcessB_time_cost.values() if value is not None]
        temp.sort()
        return temp[int(len(temp) * 0.99)]
    
    def get_ProcessA_p90_time_cost(self):
        """返回ProcessA的90分位时间消耗"""
        temp = [value for value in self.ProcessA_time_cost.values() if value is not None]
        temp.sort()
        return temp[int(len(temp) * 0.9)]
    
    def get_ProcessB_p90_time_cost(self):
        """返回ProcessB的90分位时间消耗"""
        temp = [value for value in self.ProcessB_time_cost.values() if value is not None]
        temp.sort()
        return temp[int(len(temp) * 0.9)]

    def output_ProcessA_json(self, ProcessA_output_json_path):
        """将ProcessA计算的结果输出到json文件"""
        with open(ProcessA_output_json_path, 'w') as f:
            f.write(json.dumps(self.ProcessA_time_cost, indent=4))
    
    def output_ProcessB_json(self, ProcessB_output_json_path):
        """将ProcesssB计算的结果输出到json文件"""
        with open(ProcessB_output_json_path, 'w') as f:
            f.write(json.dumps(self.ProcessB_time_cost, indent=4))

