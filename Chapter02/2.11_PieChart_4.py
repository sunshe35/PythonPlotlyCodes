# 2.11-4 应用案例
import plotly as py
import plotly.graph_objs as go

# Donut Chart
pyplt = py.offline.plot
fig = {
  "data": [
    {
      "values": [9884, 9510, 9363, 7961, 6755],
      "labels": [
          '金瑞期货',
          '海通期货', 
          '国泰君安',
          '银河期货',
          '五矿经易'
      ],
      'domain': {'x': [0, .6],
                'y': [0, .5]},
      "name": "AU.SHF多头持仓",
      "hoverinfo":"label + percent + name",
      "hole": .4,
      "type": "pie"
    },     
    {
      "values": [8847, 6229, 2764, 2406, 2022],
      "labels": [
          '中信期货',
          '招金期货', 
          '国贸期货',
          '铜冠金源',
          '中银国际'
      ],
      'domain': {'x': [.2, 1],
                'y': [0, .5]},
      "name": "AU.SHF空头持仓",
      "hoverinfo":"label + percent + name",
      "hole": .4,
      "type": "pie"
    },
    {
      "values": [14393, 12220, 11824, 11233, 10072],
      "labels": [
          '中信期货',
          '东证期货', 
          '海通期货',
          '方正中期',
          '国泰君安'
      ],
      'domain': {'x': [0, .9],
                'y': [.5, 1]},
      "name": "AG.SHF多头持仓",
      "hoverinfo":"label + percent + name",
      "hole": .4,
      "type": "pie"
    },
    {
      "values": [30983, 20699, 16781, 15686, 14198],
      "labels": [
          '中信期货',
          '国泰君安', 
          '海通期货',
          '国贸期货',
          '永安期货'
      ],
      'domain': {'x': [0.5, 1],
                'y': [.5, 1]},
      "name": "AG.SHF空头持仓",
      "hoverinfo":"label + percent + name",
      "hole": .4,
      "type": "pie"
    }],
    
  "layout": {
        "title":"有色金属板块主力合约多空持仓分布图",
        "annotations": [
            {
                "font": {
                    "size": 18
                },
                "showarrow": False,
                "text": "AU.SHF多头持仓",
                "x": 0.45,
                "y": 0.754
            },
            {
                "font": {
                    "size": 18
                },
                "showarrow": False,
                "text": "AU.SHF空头持仓",
                "x": 0.794,
                "y": 0.754
            },
            {
                "font": {
                    "size": 18
                },
                "showarrow": False,
                "text": "AG.SHF多头持仓",
                "x": 0.255,
                "y": 0.23
            },
            {
                "font": {
                    "size": 18
                },
                "showarrow": False,
                "text": "AG.SHF空头持仓",
                "x": 0.6,
                "y": 0.23
            }
        ]
    }
}
pyplt(fig, filename='tmp/donut.html')
