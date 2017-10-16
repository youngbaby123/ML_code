#-*-coding:utf-8-*- 
import os
import random
import shutil


def GetimgList(dir, dir_rel='', fileList=[], dir_rel_list=[]):
    newDir = dir
    newdir_rel = dir_rel
    if os.path.isfile(dir):
        try:
            fileList.append(dir)
            # dir_rel_list.append(dir_rel.decode('gbk'))
        except Exception,e:
            print e.message
            print 'IO error: ', dir
    elif os.path.isdir(dir):
        for s in os.listdir(dir):
            newDir = os.path.join(dir, s)
            if os.path.isdir(newDir):
                newdir_rel = os.path.join(dir_rel, s)
            GetimgList(newDir, newdir_rel, fileList, dir_rel_list)
    return fileList

def shuffle_with_single():
    img_root = "/home/yang/Workspace/Study/ML/all_data"
    list_save_path = "/home/yang/Workspace/Study/ML/img_list_100.txt"
    img_save_path = "/home/yang/Workspace/Study/ML/tiny_data"
    if not os.path.exists(img_save_path):
        os.makedirs(img_save_path)

    save_img_list = []
    for dir_i in os.listdir(img_root):
        path_root_i = os.path.join(img_root, dir_i)
        img_list = GetimgList(path_root_i, dir_rel='', fileList=[], dir_rel_list=[])
        random.shuffle(img_list)
        save_img_list += img_list[:100]


    for img_path_i in save_img_list:
        shutil.copy(img_path_i, img_save_path)
    save_img_txt = open(list_save_path,"w")
    save_img_txt.write("\n".join(save_img_list))

def shuffle_with_all():
    img_root = "/home/yang/Workspace/Study/ML/tiny_data"
    list_save_path = "/home/yang/Workspace/Study/ML/img_list_tiny.txt"

    img_list = GetimgList(img_root, dir_rel='', fileList=[], dir_rel_list=[])
    random.shuffle(img_list)

    save_img_txt = open(list_save_path,"w")
    save_img_txt.write("\n".join(img_list))


def rename_img():
    img_root = "/home/yang/Workspace/Study/ML/all_data/{}".format("model_zipai_crop")
    img_list = GetimgList(img_root, dir_rel='', fileList=[], dir_rel_list=[])
    for name_i in img_list:
        new_name_i = name_i.replace('corp','crop')
        os.rename(name_i,new_name_i)

def check():
    list_save_path = "/home/yang/Workspace/Study/ML/img_list_100.txt"
    img_root = "/home/yang/Workspace/Study/ML/tiny_data"
    save_img_txt = open(list_save_path, "r").readlines()
    img_name_txt = [i.split()[0].split("/")[-1] for i in save_img_txt]
    img_name_dir = [j for j in os.listdir(img_root)]
    for m in img_name_txt:
        if not m in img_name_dir:
            print m


def main():
    shuffle_with_single()
    shuffle_with_all()
    # check()
    # rename_img()




if __name__ == '__main__':
     main()