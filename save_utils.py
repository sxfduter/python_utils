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
