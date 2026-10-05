import json
from pyecharts import options as opts
from pyecharts.charts import Bar
class dataclass:
    def __init__(self,date,order_id,sale_amount,province):
        self.date = date
        self.order_id = order_id
        self.sale_amount = sale_amount
        self.province = province
    # 重写__repr__方法，实现对象的打印输出
    def __repr__(self):
        return f'{self.date},{self.order_id},{self.sale_amount},{self.province}'

class FileReader():
    def __init__(self,file_path,encoding = 'utf-8'):
        self.fr = open(file_path,'r',encoding=encoding)

    def read_csv(self) -> list:
        data_list = []
        for line in self.fr.readlines()[1:]:
            line = line.strip()
            arr = line.split(',')
            dc = dataclass(arr[0],arr[1],arr[2],arr[3])
            data_list.append(dc)
        return data_list

    def read_json(self) -> list:
        data_list = []
        for line in self.fr.readlines()[1:]:
            line = line.strip()
            data_dict = json.loads(line)
            dc = dataclass(data_dict['date'],data_dict['order_id'],data_dict['sale_amount'],data_dict['province'])
            data_list.append(dc)
        return data_list
fr_csv = FileReader(r"F:\新建文件夹\data (2).csv")
fr_json = FileReader(r"F:\新建文件夹\data.json")
lst1 = fr_csv.read_csv()
lst2 = fr_json.read_json()
all_data = lst1 + lst2

def data_process(data):
    data_dict = {}
    for dc in data:
        if dc.date in data_dict:
            data_dict[dc.date] += float(dc.sale_amount)
        else:
            data_dict[dc.date] = float(dc.sale_amount)
    # 字典转换为列表，按日期排序
    data = [(key,value) for key,value in data_dict.items()]
    data.sort()
    d_list = [t[0] for t in data]
    s_list = [t[1] for t in data]
    return d_list,s_list
date_list,amount_list = data_process(all_data)



def draw_bar(date_list, amount_list):
    bar = (
        Bar()
        .add_xaxis(date_list)
        .add_yaxis("销售额", amount_list, color="blue", label_opts=opts.LabelOpts(is_show=False))
        .set_global_opts(
            title_opts=opts.TitleOpts(title="黑马程序员数据分析案例"),
            xaxis_opts=opts.AxisOpts(
                axislabel_opts=opts.LabelOpts(rotate=-45, interval=5),
            ),
            # Y轴增加单位【元】
            yaxis_opts=opts.AxisOpts(name="元"),
            # 图例放到右上角
            legend_opts=opts.LegendOpts(pos_right="5%", pos_top="5%"),
            datazoom_opts=[opts.DataZoomOpts(range_start=0, range_end=100)],
        )
    )
    bar.render("sales_bar.html")

draw_bar(date_list, amount_list)

















