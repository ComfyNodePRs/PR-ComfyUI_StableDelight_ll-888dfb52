import os
import sys

# 获取当前目录的父目录
parent_dir = os.path.dirname(os.path.abspath(__file__))

# 添加父目录到系统路径
sys.path.insert(0, parent_dir)

from .nodes import BaseNode

NODE_CLASS_MAPPINGS = {**BaseNode.NODE_CLASS_MAPPINGS}
NODE_DISPLAY_NAME_MAPPINGS = {**BaseNode.NODE_DISPLAY_NAME_MAPPINGS}
