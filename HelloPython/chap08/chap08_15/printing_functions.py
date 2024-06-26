def print_models(unprinted_designs, completed_models):
    """
    模拟打印每个设计，直到没有未打印的设计为⽌
    打印每个设计后，都将其移到列表 completed_models 中
    Args:
        unprinted_designs: 未打印的设计
        completed_models: 已打印的设计
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
    print(f"Printing model: {current_design}")
    completed_models.append(current_design)


def show_completed_models(completed_models):
    """显⽰打印好的所有模型
    Args:
        completed_models: 已打印的模型"""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

