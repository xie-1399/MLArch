#计算图基类

class Graph(object):
    def __init__(self):
        self.nodes = []
        self.name_scope = None

    def add_node(self,node):
        self.nodes.append(node)

    def reset_value(self):
        """
        重置图中全部节点的值
        """
        for node in self.nodes:
            node.reset_value(False)  # 每个节点不递归清除自己的子节点的值

    def node_count(self):
        return len(self.nodes)

default_graph = Graph()