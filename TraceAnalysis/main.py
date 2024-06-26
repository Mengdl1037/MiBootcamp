# UTF-8
# Author: Mengdi Liu
# Date: 2024-6-25
# Function: Main function


from pathlib import Path

from lib.data_extract import DataExtract
from lib.process_time_cost import ProcessTimeCost
from lib.frame_time_cost import FrameTimeCost
from lib.plot_figure import PlotFigure

# 文件路径
LOG_FILE_PATH = Path('./data_repo/trace_analysis.log')
DATA_FILE_PATH = Path('./my_repo/data.json')
PROCESSA_TIME_COST_FILE_PATH = Path('./my_repo/ProcessA_time_cost.json')
PROCESSB_TIME_COST_FILE_PATH = Path('./my_repo/ProcessB_time_cost.json')
FIGURE_OUTPUT_PATH = Path('./my_repo/time_sequence.png')

# 提取数据
data_extract = DataExtract()
data_extract.extract_data(LOG_FILE_PATH)
data_extract.output_json(Path(DATA_FILE_PATH))

# 各工序耗时统计
process_time_cost = ProcessTimeCost()
process_time_cost.calculate_time_cost(DATA_FILE_PATH)
process_time_cost.output_ProcessA_json(PROCESSA_TIME_COST_FILE_PATH)
process_time_cost.output_ProcessB_json(PROCESSB_TIME_COST_FILE_PATH)
print(f"ProcessA的平均耗时：{process_time_cost.get_ProcessA_average_time_cost()} ms")
print(f"ProcessA的99分位耗时：{process_time_cost.get_ProcessA_p99_time_cost()} ms")
print(f"ProcessA的90分位耗时：{process_time_cost.get_ProcessA_p90_time_cost()} ms")
print(f"ProcessB的平均耗时：{process_time_cost.get_ProcessB_average_time_cost()} ms")
print(f"ProcessB的99分位耗时：{process_time_cost.get_ProcessB_p99_time_cost()} ms")
print(f"ProcessB的90分位耗时：{process_time_cost.get_ProcessB_p90_time_cost()} ms")

# 平均吞吐量和平均帧时间消耗
frame_time_cost = FrameTimeCost(DATA_FILE_PATH)
print(f"平均吞吐量：{frame_time_cost.get_average_throughput()} 帧/秒")
print(f"平均帧时间消耗：{frame_time_cost.get_acverage_frame_time_cost()} ms")

# ProcessA和ProcessB的调度时序图
plot_figure = PlotFigure(DATA_FILE_PATH)
plot_figure.plot_time_sequence(FIGURE_OUTPUT_PATH)




