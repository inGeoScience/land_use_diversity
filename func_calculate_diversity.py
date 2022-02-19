import numpy
import pandas
from tkinter import filedialog
import time


class calculateDiversity:

    def calculate_normalized_entropy(self, param_rows_list: list):
        entropy_list = []
        for one_list in param_rows_list:
            molecule_sum = 0
            species_count = 0
            for item in one_list:
                if item > 0:
                    species_count += 1
            for item in one_list:
                if item > 0:
                    molecule_sum += (item / sum(one_list)) * numpy.log(item / sum(one_list))
            molecule_sum = -molecule_sum
            entropy = molecule_sum / numpy.log(species_count)
            entropy_list.append(entropy)
        return entropy_list

    def calculate_shannon_entropy(self, param_rows_list: list):
        entropy_list = []
        for one_list in param_rows_list:
            molecule_sum = 0
            species_count = 0
            for item in one_list:
                if item > 0:
                    species_count += 1
            for item in one_list:
                if item > 0:
                    molecule_sum += (item/sum(one_list)) * numpy.log(item / sum(one_list))
            entropy = -molecule_sum
            entropy_list.append(entropy)
        return entropy_list

class baseFunction:

    def get_data(self):
        rows_list = []
        properties_list = []
        data_file = filedialog.askopenfile()
        print('请在弹出的窗口中选择操作的Excel文件')
        sheet_name = input('请输入Sheet名称：')
        # 直接复制吧：餐饮,公共设施,公园广场,公司,购物中心,超级市场,银行,学校,住宅,医院,政府单位,酒店旅社,运动场所
        usecols_str = input('请输入各类POI的字段名，使用英文逗号隔开：')
        usecols_list = []
        for str in usecols_str.split(','):
            usecols_list.append(str)
        if data_file:
            df = pandas.read_excel(io=data_file.name,
                                   sheet_name=sheet_name,
                                   usecols=usecols_list)
            for row in df.itertuples():
                properties_list = []
                for item in usecols_list:
                    properties_list.append(row.__getattribute__(item))
                rows_list.append(properties_list)
        return rows_list

    def save_excel(self, param_entropy_list: list, field_name: str):
        df = pandas.DataFrame({
            field_name: param_entropy_list
        })
        current_time = str(time.time())
        df.to_excel('./Data/%s_result.xlsx' % field_name, index=False)
        print('输出Excel完成')