import xml.etree.ElementTree as ET
import pickle
import os
from os import listdir, getcwd
from os.path import join
from pathlib import Path
import pdb

cat_class_id=0


def convert(size, box):
    dw = 1./(size[0])
    dh = 1./(size[1])
    x = (box[0] + box[1])/2.0 - 1
    y = (box[2] + box[3])/2.0 - 1
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh
    return (x,y,w,h)



def convert_annotation(xml_path):
    #text=open(xml_path).read()
    #text=re.sub(u"[\x00-\x08\x0b-\x0c\x0e-\x1f]+",u"",text)
    #root=ET.fromstring(text) # xml非法字符时使用
    #print(xml_path) #如果有报xml损坏用这个查看损坏文件 不多直接删了
    tree = ET.parse(xml_path)
   # parser = ET.XMLParser(recover=True)
   # tree = ET.fromstring(xml_path, parser=parser)
    root = tree.getroot()
    #pdb.set_trace()()
    wd=Path.cwd()
    if not Path(wd / "annotation").exists():
        Path.mkdir(wd / "annotation")
    img_id=Path(xml_path).stem
    #pdb.set_trace()()
    file_name="annotation/%s.txt"%img_id
    #print(file_name)
    if not Path(wd / file_name).exists():
        #os.mknod(wd / file_name)
        open(wd / file_name, 'w').close()

    width=float(root[4][0].text)
    height=float(root[4][1].text)    
    out_file=open(wd/file_name,'w')    
    for item in root.findall('object'):
        xmin=float(item[4][0].text)
        ymin=float(item[4][1].text)
        xmax=float(item[4][2].text)
        ymax=float(item[4][3].text)
        sz=(width,height)
        b=(xmin,xmax,ymin,ymax)
        bb=convert(sz,b)
        out_file.write(str(cat_class_id)+" "+" ".join([str(a) for a in bb])+'\n')

    

#get current path, set img_path  and label path  
wd=Path.cwd()
img_path= wd /"pack_2"
label_path= wd / "label"
i,j=0,0
for item in label_path.iterdir():
    #print(Path(img_path/item.stem/".jpg"))
    #if Path(img_path/str(item.stem+".jpg")).exists():
        #i=i+1
    convert_annotation(item)
