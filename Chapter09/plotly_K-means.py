import plotly as py
import plotly.graph_objs as go
from plotly import tools

import time
import numpy as np

from sklearn.cluster import MiniBatchKMeans, KMeans
from sklearn.metrics.pairwise import pairwise_distances_argmin
from sklearn.datasets.samples_generator import make_blobs

# 产生随机数据
np.random.seed(0)

batch_size = 45
centers = [[1, 1], [-1, -1], [1, -1]]
n_clusters = len(centers)
X, labels_true = make_blobs(n_samples = 3000, centers = centers, cluster_std = 0.7)

# n_samples是待生成的样本的总数
# centers表示类别数
# cluster_std表示每个类别的方差，例如我们希望生成2类数据，其中一类比另一类具有更大的方差，可以将cluster_std设置为[1.0,3.0]。

# 使用K-means算法
k_means = KMeans(init = 'k-means++', n_clusters = 3, n_init = 10)
t0 = time.time()
k_means.fit(X)
t_batch = time.time() - t0

# 使用MiniBatchKMeans算法
mbk = MiniBatchKMeans(init = 'k-means++', n_clusters = 3, batch_size = batch_size,
                      n_init = 10, max_no_improvement = 10, verbose = 0)
t0 = time.time()
mbk.fit(X)
t_mini_batch = time.time() - t0

pyplt = py.offline.plot
colors = ['#4EACC5', '#FF9C34', '#4E9A06']

# We want to have the same colors for the same cluster from the
# MiniBatchKMeans and the KMeans algorithm. Let's pair the cluster centers per
# closest one.
k_means_cluster_centers = np.sort(k_means.cluster_centers_, axis=0)
mbk_means_cluster_centers = np.sort(mbk.cluster_centers_, axis=0)
# Compute minimum distances between one point and a set of points
k_means_labels = pairwise_distances_argmin(X, k_means_cluster_centers)
mbk_means_labels = pairwise_distances_argmin(X, mbk_means_cluster_centers)
order = pairwise_distances_argmin(k_means_cluster_centers,
                                  mbk_means_cluster_centers)

fig = tools.make_subplots(rows=1, cols=3,
                          print_grid=False,
                          subplot_titles=('KMeans<br>train time: %.2fs\ninertia: %f' %
                                          (t_mini_batch, mbk.inertia_),
                                          'MiniBatchKmeans<br>train time: %.2fs\ninertia: %f' %
                                          (t_mini_batch, mbk.inertia_), 
                                          'Difference'))
# k-means
for k, col in zip(range(n_clusters), colors):
    my_members = k_means_labels == k
    cluster_center = k_means_cluster_centers[k]
    kmeans1 = go.Scatter(x=X[my_members, 0], y=X[my_members, 1],
                         showlegend=False,
                         mode='markers', marker=dict(color=col, size=4))
    kmeans2 = go.Scatter(x=[cluster_center[0]], y=[cluster_center[1]],
                         showlegend=False,
                         mode='markers', marker=dict(color=col, size=14,
                                                    line=dict(color='black',
                                                              width=1)))
    fig.append_trace(kmeans1, 1, 1)
    fig.append_trace(kmeans2, 1, 1)
    
fig['layout']['xaxis1'].update(showticklabels=False, ticks='',
                               zeroline=False, showgrid=False)
fig['layout']['yaxis1'].update(showticklabels=False, ticks='',
                               zeroline=False, showgrid=False)
# minibatchkmeans
for k, col in zip(range(n_clusters), colors):
    my_members = mbk_means_labels == order[k]
    cluster_center = mbk_means_cluster_centers[order[k]]
    minibatchkmeans1 = go.Scatter(x=X[my_members, 0], y=X[my_members, 1],
                                 showlegend=False,
                                 mode='markers', marker=dict(color=col, size=4))
    minibatchkmeans2 = go.Scatter(x=[cluster_center[0]], y=[cluster_center[1]],
                                 showlegend=False,
                                 mode='markers', marker=dict(color=col, size=14,
                                                            line=dict(color='black',
                                                                      width=1)))
    fig.append_trace(minibatchkmeans1, 1, 2)
    fig.append_trace(minibatchkmeans2, 1, 2)

fig['layout']['xaxis2'].update(showticklabels=False, ticks='',
                               zeroline=False, showgrid=False)
fig['layout']['yaxis2'].update(showticklabels=False, ticks='',
                               zeroline=False, showgrid=False)

# Initialise the different array to all False
different = (mbk_means_labels == 4)

for k in range(n_clusters):
    different += ((k_means_labels == k) != (mbk_means_labels == order[k]))

identic = np.logical_not(different)
difference1 = go.Scatter(x=X[identic, 0], y=X[identic, 1],
                         showlegend=False,
                         mode='markers', marker=dict(color='#bbbbbb', size=4))
        
difference2 = go.Scatter(x=X[different, 0], y=X[different, 1], 
                         showlegend=False,
                         mode='markers', marker=dict(color='magenta', size=4))

fig.append_trace(difference1, 1, 3)
fig.append_trace(difference2, 1, 3)

fig['layout']['xaxis3'].update(showticklabels=False, ticks='',
                               zeroline=False, showgrid=False)
fig['layout']['yaxis3'].update(showticklabels=False, ticks='',
                               zeroline=False, showgrid=False)
pyplt(fig, filename = r'tmp\K-means.html')