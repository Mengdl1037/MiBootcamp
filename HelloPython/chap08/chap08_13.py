# UTF-8
# Author: Liu Mengdi
# Date: 2024-06-21
# Function:

def build_profile(first, last, **user_info):
    """创建⼀个字典，其中包含我们知道的有关⽤户的⼀切
    Args:
        first: 名字
        last: 姓
        **user_info: 其他信息
    Returns:
        包含⽤户信息的字典
    """
    user_info['first_name'] = first.lower()
    user_info['last_name'] = last.lower()
    return user_info


user_profile = build_profile('San', 'Zhang',
    location='Beijing',
    school='Tsinghua University',
    field='Mathematics')
print(user_profile)