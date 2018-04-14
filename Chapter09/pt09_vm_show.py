# -*- coding: utf-8 -*-
"""
She35 Editor
运行本程序之前，请确保已经成功启动visdom服务，启动方式如下：
python -m visdom.server
"""
from visdom import Visdom
import numpy as np
import math
import os.path
import getpass
from sys import platform as _platform
from six.moves import urllib
import traceback

viz = Visdom()

viz.text('Hello, Visdom!')


# contour
x = np.tile(np.arange(1, 101), (100, 1))
y = x.transpose()
X = np.exp((((x - 50) ** 2) + ((y - 50) ** 2)) / -(20.0 ** 2))

# image demo
viz.image(
    np.random.rand(3, 512, 256),
    opts=dict(title='Random!', caption='How random.'),
)

# grid of images
viz.images(
    np.random.randn(20, 3, 64, 64),
    opts=dict(title='Random images', caption='How random.')
)