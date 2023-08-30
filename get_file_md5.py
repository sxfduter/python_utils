import hashlib

def get_file_md5(file_path):
    with open(file_path, 'rb') as f:
        md5_obj = hashlib.md5()
        while True:
            data = f.read(4096)
            if not data:
                break
            md5_obj.update(data)
    return md5_obj.hexdigest()

file_path = 'marker_quad_det_with_preprocess.onnx'
md5_value = get_file_md5(file_path)
print(f'The MD5 value of {file_path} is {md5_value}')
