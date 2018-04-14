# -*- coding: utf-8 -*-
"""
She35 Editor
运行本程序之前，请确保已经成功启动visdom服务，启动方式如下：
python -m visdom.server
"""
from visdom import Visdom
import numpy as np

vis = Visdom()

svgstr = """
<svg height="300" width="300">
  <ellipse cx="80" cy="80" rx="50" ry="30"
   style="fill:red;stroke:purple;stroke-width:2" />
  抱歉，你的浏览器不支持在线显示SVG对象.
</svg>
"""
vis.svg(
    svgstr=svgstr,
    opts=dict(title='SVG图像')
)