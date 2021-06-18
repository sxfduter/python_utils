def write_list_to_json(list, name, save_path):
     """
     将list写入到json文件
     :param list:
     :param json_file_name: 写入的json文件名字
     :param json_file_save_path: json文件存储路径
     :return:
     """
     os.chdir(save_path)
     with open(name, 'w', encoding='utf-8') as f:
         json.dump(list, f, ensure_ascii=False)

def write_to_txt(data, name="a"):
    """
     将list写入到txt文件
     :param list:
     :param name: 写入的txt文件名字
     :return:
     """
     with open(name+'.txt', 'w') as f:
         for i in range(len(data)):
             f.write(data[i]+"\r")
               
def read_to_list(file_txt):
    """
    将txt读到list
    :param file_txt: txt文件
    :return: list
    """
    data_list = []
    for line in open(file_txt, 'r'):
        data_list.append(line[:-1])
    return data_list
