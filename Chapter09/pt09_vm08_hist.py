# -*- coding: utf-8 -*-
"""
She35 Editor
运行本程序之前，请确保已经成功启动visdom服务，启动方式如下：
python -m visdom.server
"""
from visdom import Visdom
import numpy as np

vis = Visdom()

vis.histogram(X=np.random.rand(10000), opts=dict(numbins=20))