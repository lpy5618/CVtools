import os#批量删除带有某名字的文件
path="I:/ictnet/data/test/results/10/shape/bellingham1/"
files=os.listdir(path)
for i ,f in enumerate(files):
    if f.find("bellingham1")>=0 :
        print(f)
        os.remove(path+f)
