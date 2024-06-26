# UTF-8
# Author: Mengdi Liu
# Date: 2024-6-25
# Function:

import matplotlib.pyplot as plt
import numpy as np
import json

class PlotFigure:
    def __init__(self, data_file_path=None):
        self.data = None
        if data_file_path:
            self.load_data(data_file_path)
    
    def load_data(self, data_file_path):
        """加载数据文件，同时计算帧数、最大时间、最小时间"""
        with open(data_file_path, 'r') as f:
            self.data = json.load(f)
        self.data = sorted(self.data, key=lambda x: x[0], reverse=False)

    def plot_time_sequence(self, output_path):
        """绘制ProcessA和ProcessB的调度时序图"""
        plt.figure(figsize=(40, 30))
        for frame_id, info in self.data:
            if info['ProcessA_start'] is not None:
                hline_A = np.arange(info['ProcessA_start'], info['ProcessA_end'], 1)
                frame_A = np.ones_like(hline_A) * int(frame_id)
                plt.plot(hline_A, frame_A, color='orange')
            if info['ProcessB_start'] is not None:
                hline_B = np.arange(info['ProcessB_start'], info['ProcessB_end'], 1)
                frame_B = np.ones_like(hline_B) * int(frame_id)
                plt.plot(hline_B, frame_B, color='red')
                # plt.plot(y=frame_id, xmin=info['ProcessB_start'], xmax=info['ProcessB_end'], color='red')

        plt.xlabel('Time(ms)')
        plt.ylabel('Frame ID')
        plt.xlimit = (90000, 150000)
        plt.ylimit = (5000, 7000)
        # plt.ypltis.set_major_locator(plt.MultipleLocator(500))
        plt.title('Time Sequence of ProcessA and ProcessB')
        plt.legend(['ProcessA', 'ProcessB'])
        plt.grid(True)
        plt.savefig(output_path)
        plt.show()