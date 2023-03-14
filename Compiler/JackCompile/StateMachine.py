#FSM状态机的结构
from transitions import Machine
# 定义一个自己的类
class Matter(object):
    pass
model = Matter()
# 状态定义
states=['solid', 'liquid', 'gas', 'plasma']
# 定义状态转移
# The trigger argument defines the name of the new triggering method
transitions = [
    {'trigger': 'melt', 'source': 'solid', 'dest': 'liquid' },
    {'trigger': 'evaporate', 'source': 'liquid', 'dest': 'gas'},
    {'trigger': 'sublimate', 'source': 'solid', 'dest': 'gas'},
    {'trigger': 'ionize', 'source': 'gas', 'dest': 'plasma'}]
# 初始化
machine = Machine(model=model, states=states, transitions=transitions, initial='solid')
# Test 
print(model.state)   # solid
# 状体转变
model.melt()
print(model.state)   # liquid
