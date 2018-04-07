from visdom import Visdom
import numpy as np

vis = Visdom()

# image demo
vis.image(
    np.random.rand(3, 256, 256),
    opts=dict(title='单图片', caption='图片标题1'),
)

# grid of images
vis.images(
    np.random.randn(20, 3, 64, 64),
    opts=dict(title='网格图像', caption='图片标题2')
)