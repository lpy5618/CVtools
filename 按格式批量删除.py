import os#批量删除某格式文件

def del_files(path):
  for root , dirs, files in os.walk(path):
    for name in files:
      if name.endswith(".swf"):   #指定要删除的格式，这里是jpg 可以换成其他格式
        os.remove(os.path.join(root, name))
        print ("Delete File: " + os.path.join(root, name))
# test
if __name__ == "__main__":
  path = 'J:\\豆丁网下载\\swf'
  del_files(path)
