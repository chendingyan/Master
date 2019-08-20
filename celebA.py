import pickle
import shutil
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.path import Path
import torch
import sys
import scipy.misc
import os
import dlib
import cv2


txt_path = '/Users/mikechen/Downloads/Anno/list_attr_celeba.txt'
new_txt = '/Users/mikechen/Downloads/Anno/female_list.txt'
new_txt1 = '/Users/mikechen/Downloads/Anno/female_list_headpose.txt'
new_txt2 = '/Users/mikechen/Downloads/Anno/female_list_headpose1.txt'
old_dir = '/Users/mikechen/Downloads/img_align_celeba'
new_dir = '/Users/mikechen/Downloads/celebA'
data_path = '/Users/mikechen/Downloads/proc_align_celeba.pkl'
test = '/Users/mikechen/Downloads/Anno/output.txt'
mask_path = '/Users/mikechen/Downloads/masks/'

man_txt = '/Users/mikechen/Downloads/Anno/All_people.txt'
man_txt_1 = '/Users/mikechen/Downloads/Anno/All_people_1.txt'
man_headpose = '/Users/mikechen/Downloads/Anno/All_people_headpose.txt'
def process():
    ob = pickle.load(open(data_path, 'rb'))
    with open(new_txt2,'r') as f:
        for line in f:
            num = line[0:-5]
            print(num)

            landmarks = ob[num]['landmarks']
            landmark_socres = ob[num]['landmark_scores']
            #
            left_eye = landmarks[36:42]
            right_eye = landmarks[42:48]
            nose = np.concatenate(([landmarks[28]],landmarks[31:36]), axis=0)
            mouth = landmarks[48:60]
            mask = np.full((218, 178), 0,dtype=int)
            image_points = np.empty((178*218,2), dtype=int)
            for i in range(178*218):
                image_points[i][0] = i / 178
                image_points[i][1] = i % 218

            for part in [left_eye, right_eye, nose, mouth]:
                p = Path(part)
                idx = p.contains_points(image_points)
                res = np.array(idx).reshape(178, 218).T
                mask[res] = 1
            name = mask_path + num + '.png'
            print(name)
            scipy.misc.imsave(name, mask)
            # np.savetxt(test,mask, fmt='% 1d')

def process3():
    ob = pickle.load(open(data_path, 'rb'))
    with open(new_txt2, 'r') as f:
        for line in f:
            num = line[0:-5]
            print(num)
            if int(num) < 5:
                face_box = ob[num]['face_box']
                print(face_box)
            # img = cv2.imread(new_dir + '/' + num +'.jpg')
            # cropped = img[int(face_box[0]): int(face_box[3]), int(face_box[1]): int(face_box[2])]
            # cv2.imwrite('/Users/mikechen/Desktop/cv.jpg',cropped)

# 对于任意一个celebA数据集 进行dlib 68点检测并且生成对应mask
def process2(celebA_path, mask_path):
    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor('dlib/shape_predictor_68_face_landmarks.dat')
    files = os.listdir(celebA_path)  # 得到文件夹下的所有文件名称
    for f in files:
        img_rd = cv2.imread(celebA_path + '/' + f)
        img_gray = cv2.cvtColor(img_rd, cv2.COLOR_RGB2GRAY)
        faces = detector(img_gray, 0)
        if len(faces) != 0:
            # 检测到人脸
            for i in range(len(faces)):
                # 取特征点坐标
                landmarks = np.matrix([[p.x, p.y] for p in predictor(img_rd, faces[i]).parts()])
                for idx, point in enumerate(landmarks):
                    # 68 点的坐标
                    pos = (point[0, 0], point[0, 1])
                    print(pos)
        break




def del_head_pose():
    ob = pickle.load(open(data_path, 'rb'))
    with open(man_txt, 'r') as f:
        with open(man_txt_1, 'a') as new:
            for line in f:
                num = line[0:-5]
                image_id = ob[num]['image_id']
                if ob[num].__contains__('head_pose') == True:
                    new.write(line)
                else:
                    print(num)
    #         face_box = ob[num]['face_box']
    #         head_pose = ob[num]['head_pose']
    #         landmarks = ob[num]['landmarks']
    #         landmark_socres = ob[num]['landmark_scores']
    #
    #         # print ('face_box', face_box)
    #         print ('head_pose' ,head_pose)
    #         # print ('landmarks' , len(landmarks))
    #         # print ('landmark_socres' , landmark_socres)

def draw_head_pose():
    pitch = []
    yaw = []
    roll = []
    ob = pickle.load(open(data_path, 'rb'))
    # print(ob['000042'])
    with open(man_txt_1, 'r') as f:
        with open(man_headpose, 'a') as new:
            for line in f:
                num = line[0:-5]
                head_pose = ob[num]['head_pose']
                pitch.append(head_pose[0])
                yaw.append(head_pose[1])
                roll.append(head_pose[2])
                if -25 <= head_pose[1] <= 25:
                    new.write(line)
                else:
                    print(num)
    #
    # np_pitch = np.asarray(pitch)
    # np_yaw = np.asarray(yaw)
    # np_roll = np.asarray(roll)
    # plt.subplot(221)
    # binwidth = 1
    # n, bins, patches = plt.hist(x=np_pitch, bins=np.arange(min(np_pitch), max(np_pitch) + binwidth, binwidth), color='#0504aa',
    #                             alpha=0.7, rwidth=0.85, normed=True)
    # print(np_pitch)
    #
    # plt.subplot(222)
    # binwidth = 1
    # n, bins, patches = plt.hist(x=np_yaw, bins=np.arange(min(np_yaw), max(np_yaw) + binwidth, binwidth),
    #                             color='#0504aa',
    #                             alpha=0.7, rwidth=0.85, normed=True)
    # print(np_yaw)
    #
    # plt.subplot(212)
    # binwidth = 1
    # n, bins, patches = plt.hist(x=np_roll, bins=np.arange(min(np_roll), max(np_roll) + binwidth, binwidth),
    #                             color='#0504aa',
    #                             alpha=0.7, rwidth=0.85, normed=True)
    # print(np_roll)
    # plt.show()

def copyfiles():
    with open(new_txt2, 'r') as f:
        for line in f:
            old = old_dir+'/'+line[0:-1]
            print(old)
            new = new_dir+'/'+line[0:-1]
            shutil.copyfile(old, new)

def filter_female():

    # f = open(txt_path, "r")
    # print (f)
    count = 0 # 202601
    female = 0
    with open(txt_path, 'r') as f:
        with open(new_txt, 'a') as new:
            for line in f:
                if count < 202602:
                    if count > 1:
                        x = line.split()
                        if x[21] == '-1':
                            print(x[0])
                            new.write(x[0]+'\n')
                            female+=1
                    count+=1
                else:
                    break
    print(female)
    count = 0
    with open(new_txt, 'r') as f:
        for line in f:
            count+=1
    print(count)

# copyfiles()
# draw_head_pose()

if __name__ == '__main__':
    # process()
    # process3()
    # draw_head_pose()
    # count = 0
    # with open(man_headpose, 'r') as f:
    #     for line in f:
    #         count += 1
    # print(count)