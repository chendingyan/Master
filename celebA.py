import pickle
import shutil
import numpy as np
import matplotlib.pyplot as plt
txt_path = '/Users/mikechen/Downloads/Anno/list_attr_celeba.txt'
new_txt = '/Users/mikechen/Downloads/Anno/female_list.txt'
new_txt1 = '/Users/mikechen/Downloads/Anno/female_list_headpose.txt'
new_txt2 = '/Users/mikechen/Downloads/Anno/female_list_headpose1.txt'
old_dir = '/Users/mikechen/Downloads/img_align_celeba'
new_dir = '/Users/mikechen/Downloads/celebA'
data_path = '/Users/mikechen/Downloads/proc_align_celeba.pkl'

def process():
    ob = pickle.load(open(data_path, 'rb'))
    with open(new_txt2) as f:
        for line in f:
            num = line[0:-5]
            landmarks = ob[num]['landmarks']
            landmark_socres = ob[num]['landmark_scores']
            print ('landmarks' , landmarks)
            print ('landmark_socres' , landmark_socres)

def del_head_pose():
    ob = pickle.load(open(data_path, 'rb'))
    with open(new_txt, 'r') as f:
        with open(new_txt1, 'a') as new:
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
    with open(new_txt1, 'r') as f:
        with open(new_txt2, 'a') as new:
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

    np_pitch = np.asarray(pitch)
    np_yaw = np.asarray(yaw)
    np_roll = np.asarray(roll)
    plt.subplot(221)
    binwidth = 1
    n, bins, patches = plt.hist(x=np_pitch, bins=np.arange(min(np_pitch), max(np_pitch) + binwidth, binwidth), color='#0504aa',
                                alpha=0.7, rwidth=0.85, normed=True)
    print(np_pitch)

    plt.subplot(222)
    binwidth = 1
    n, bins, patches = plt.hist(x=np_yaw, bins=np.arange(min(np_yaw), max(np_yaw) + binwidth, binwidth),
                                color='#0504aa',
                                alpha=0.7, rwidth=0.85, normed=True)
    print(np_yaw)

    plt.subplot(212)
    binwidth = 1
    n, bins, patches = plt.hist(x=np_roll, bins=np.arange(min(np_roll), max(np_roll) + binwidth, binwidth),
                                color='#0504aa',
                                alpha=0.7, rwidth=0.85, normed=True)
    print(np_roll)
    plt.show()

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
# count = 0
# with open(new_txt, 'r') as f:
#     for line in f:
#         count += 1
# print(count)
if __name__ == '__main__':
    process()