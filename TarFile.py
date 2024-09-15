import tarfile, sys
from io import BytesIO
from functools import reduce


tar = bytes.fromhex(sys.stdin.read())
fileobj = BytesIO(tar)

with tarfile.open(fileobj=fileobj) as f:
    #Следующая строчка взята из StackOverFlow
    #https://stackoverflow.com/questions/10028435/python-tarfile-size
    size = reduce(lambda x,y: getattr(x, 'size', x)+getattr(y, 'size', y), f.getmembers())
    file_cnt = sum(obj.isfile() for obj in f.getmembers())
    print(size, file_cnt)
