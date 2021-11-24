# save pic from tensor
from torchvision import utils as vutils
vutils.save_image(x[0], './visual9/test.jpg'.replace('test', str(np.random.randint(1, 100))), normalize=True)        

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
             f.write(data[i]+"\n")
               
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

def get_pic_by_url(folder_path, lists):
    """
    将lists中url下载到folder_path本地目录中
    :param folder_path: 本地目录
    :return: lists: url list
    """
    if not os.path.exists(folder_path):
        print("Selected folder not exist, try to create it.")
        os.makedirs(folder_path)
    for url in lists:
        print("Try downloading file: {}".format(url))
        filename = url.split('/')[-1].split('?')[0]
        filepath = folder_path + '/' + filename
        if os.path.exists(filepath):
            print("File have already exist. skip")
        else:
            try:
                urllib.request.urlretrieve(url, filename=filepath)
            except Exception as e:
                print("Error occurred when downloading file, error message:")
                print(e)
