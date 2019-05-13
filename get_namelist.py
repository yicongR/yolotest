import os
def ListFilesToTxt(dir,file,wildcard,recursion):
    exts = wildcard.split(" ")
    files = os.listdir(dir)
    for name in files:
        fullname=os.path.join(dir,name)
        if(os.path.isdir(fullname) & recursion):
            ListFilesToTxt(fullname,file,wildcard,recursion)
        else:
            for ext in exts:
                if(name.endswith(ext)):
                    (filename,extension) = os.path.splitext(name)
                    Name = os.path.splitext(name)[0] 
                    file.write(Name + "\n")
                    break
def Test():
  dir="/Users/renyicong/Desktop/yolov3/darknet/cat_detect/val_img"
  outfile="/Users/renyicong/Desktop/yolov3/darknet/cat_detect/val.txt"
  wildcard = ".jpg"
 
  file = open(outfile,"w")
  if not file:
    print ("cannot open the file %s for writing" % outfile)
  ListFilesToTxt(dir,file,wildcard, 1)
 
  file.close()

Test()
