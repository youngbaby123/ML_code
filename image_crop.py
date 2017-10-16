#-*-coding:utf-8-*- 
import os
import random
import cv2



def img_crop(img_path, save_path, scale = 1):
    if scale < 0 or scale > 1:
        print "error."
    ori_img = cv2.imread(img_path)
    h, w = ori_img.shape[:-1]
    img_out_size = int(min(h,w) * scale)
    h_ori = random.randint(0, h - img_out_size - 1)
    w_ori = random.randint(0, w - img_out_size - 1)
    res_img = ori_img[h_ori : h_ori + img_out_size, w_ori : w_ori + img_out_size]
    cv2.imwrite(save_path, res_img)
    print img_out_size
    print h,w
    print ori_img.shape

def main():
    img_root = "/home/yang/Workspace/Study/ML/all_data/{}".format("model_pass")
    save_root = "/home/yang/Workspace/Study/ML/all_data/{}".format("model_pass_fix")
    if not os.path.exists(save_root):
        os.makedirs(save_root)
    for img_name in os.listdir(img_root):
        img_dir = os.path.join(img_root, img_name)
        for i in range(1):
            save_dir = os.path.join(save_root,"{}_crop_{}.jpg".format(img_name.split(".")[0], i))
            scale = random.uniform(0.99,1.0)
            img_crop(img_dir, save_dir, scale)


if __name__ == "__main__":
    main()