import os
import cv2

dir = "/Users/sunxiaofei/PycharmProjects/remote-server-projects/unlabeled_dataset/data"

for i, eachVid in enumerate(os.listdir(dir)):
  vPath = os.path.join(dir, eachVid)
  vname = vPath.split("/")[-1][:-4]
  print(vname)
  print(vPath)
  vidcap = cv2.VideoCapture(vPath)
  success,image = vidcap.read()
  count = 0
  valid_count = 0
  save_path = "./pic_data/"+vname
  if not os.path.exists(save_path):
     os.makedirs(save_path)
  while success:
    if count%40==0:
      valid_count += 1
      cv2.imwrite("./pic_data/"+vname+"/"+str(valid_count)+".jpg", image)     # save frame as JPEG file
    success,image = vidcap.read()
    print('Read a new frame: ', success)
    count += 1
