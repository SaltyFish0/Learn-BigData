import pyecharts
from pyecharts.charts import Bar
from pyecharts.charts import Line

import pandas as pd
import numpy as np
from pyecharts import options as opts

path = r"C:\Users\DELL\Desktop\互联网商务系疫苗学生受种者.xlsx"

data = pd.read_excel(path)
data.dropna(axis=1, inplace=True)

data['院系班级'].replace('互联网商务系', '', regex=True, inplace=True)

currentYear = 2022
data['出生年份'] = [str(i)[0:4] for i in data['出生日期']]
data['年龄'] = [2022 - int(i) for i in data['出生年份']]

x = data['院系班级'].value_counts().index
y = data['院系班级'].value_counts().values

barX_1 = np.hsplit(x, 1)[0].values.tolist()
barY_1 = np.hsplit(y, 1)[0].tolist()
barY_2 = barY_1[::-1]

bar = {
    Bar()
    .add_xaxis(barX_1)
    .add_yaxis("数量", barY_1)
    .set_global_opts(
        xaxis_opts=opts.AxisOpts(name_rotate=60, axislabel_opts={"rotate": 90}))
    .render("1" + ".html")
}

# Line = {
#     Line(
#         init_opts=opts.InitOpts(
#
#          )
#     )
#     # set_global_opts全局参数
#     # pos_left标题距离左边的位置 item_gap主副标题间的位置 title_textstyle_opts大标题样式 subtitle_textstyle_opts小标题样式
#     .set_global_opts(
#         title_opts=opts.TitleOpts(title="正标题", subtitle='副标题', item_gap=10, pos_left='20%',
#                                   title_textstyle_opts=opts.TextStyleOpts(color='red'
#                                                                           , font_size=12
#                                                                           , font_weight='bold'),
#                                   subtitle_textstyle_opts=opts.TextStyleOpts(color='blue'
#                                                                              , font_style='normal'
#                                                                              , font_weight='normal'
#                                                                              # 粗细 'normal'，'bold'，'bolder'，'lighter'
#                                                                              , font_family='monospace'
#                                                                              , font_size=12
#                                                                              , background_color='grey'
#                                                                              , border_color='black'
#                                                                              )),
#
#         # legend_opts图例
#         # type_图例样式 pos_left水平方向位置 pos_top垂直方向位置 pos_top方式
#         legend_opts=opts.LegendOpts(type_=None
# #                                     , pos_left='right'
# #                                     , pos_top='middle'
# #                                     , orient='vertical'),
# #         tooltip_opts=opts.TooltipOpts(is_show=True),
#         # xaxis_opts X轴配置
#         # type_类型 name_rotate坐标轴名称旋转角度 axislabel_opts样式
#         xaxis_opts=opts.AxisOpts(type_="category", name_rotate=0, name="班级",
#                                  axislabel_opts=opts.LabelOpts(font_size=16
#                                                                # , rotate=45
#                                                                ),
#                                  name_location='middle'  # 坐标轴名字所在的位置
#                                  , name_gap=25  # x轴名字与坐标轴之间的距离
#                                  , offset=0  # 坐标轴X的值距离X轴的距离
#                                  ),
#         yaxis_opts=opts.AxisOpts(
#             type_="value",
#             axistick_opts=opts.AxisTickOpts(is_show=True),
#             splitline_opts=opts.SplitLineOpts(is_show=True),
#         ),
#         datazoom_opts=opts.DataZoomOpts(range_start=10, range_end=30)  # 坐标轴进行缩放
#     )
#
#     .add_xaxis(xaxis_data=barX_1)  # X轴数据
#     .add_yaxis(
#         series_name="测试线1",  # 图线名称
#         y_axis=barY_1,  # Y轴数据
#         symbol="emptyCircle",  # 标记的图形
#         is_symbol_show=True,  # 是否显示symbol(标记)
#         label_opts=opts.LabelOpts(is_show=True),  # 是否显示刻度数据
#     )
#     .add_yaxis(
#         series_name="测试线2",  # 图线名称
#         y_axis=barY_2,  # Y轴数据
#     )
#     .render("1" + ".html")
# }
# print(pyecharts.__version__)