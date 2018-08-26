# coding=utf-8
import os
from random import choice

# path_data_from_trans = "./"
# path_data_from_truth = "../decode_out"
# files_from_trans = os.listdir(path_data_from_trans)
# files_from_truth = os.listdir(path_data_from_truth)
TP = 0
FP = 0
FN = 0
TN = 0

Auxiliary_Do = ['do']
Auxiliary_Be = ['be']
Auxiliary_So = ['so', 'same', 'likewise', 'opposite']
Auxiliary_Have = ['have']
Auxiliary_To = ['to']
Auxiliary_Modal = ['will', 'would', 'can', 'could', 'should', 'may', 'might', 'must']

all_sum = 0
do_sum = 0
do_correct = 0
be_sum = 0
be_correct = 0
so_sum = 0
so_correct = 0
have_sum = 0
have_correct = 0
to_sum = 0
to_correct = 0
modal_sum = 0
modal_correct = 0

f = open('./PRF1_mlp_feature_res.txt', 'w+')

for i in range(0, 5):
    with open('../decode_out/Wsj.Section2' + str(i) + '_feature_out.txt') as truth, open(
            './Wsj_out_feature_from_mlp_2' + str(i) + '_new.txt') as trans:

        false_arr = []

        for l1 in truth:
            l1 = l1.strip()
            l2 = trans.readline().strip()

            f.write('Truth=' + l1 + ' === Predict='+l2[-1] + '\n')

            # if '1' in l1:
            #     f.write(choice(false_arr))
            #     false_arr.clear()
            #     f.write('Truth=' + l1 + ' === Predict='+l2 + '\n')
            #
            # if '0' in l1:
            #     false_arr.append('Truth=' + l1 + ' === Predict=' + l2 + '\n')

f.close()

with open('./PRF1_mlp_feature_res.txt') as res:
    for line in res:

        all_sum += 1

        if 'Truth=1' in line and 'Predict=1' in line:
            TP += 1
        if 'Truth=1' in line and 'Predict=0' in line:
            FN += 1
        if 'Truth=0' in line and 'Predict=1' in line:
            FP += 1
        if 'Truth=0' in line and 'Predict=0' in line:
            TN += 1

        if 'do' in line:
            do_sum += 1
            if 'Truth=1' in line and 'Predict=1' in line:
                do_correct += 1
            if 'Truth=0' in line and 'Predict=0' in line:
                do_correct += 1

        if 'be' in line:
            be_sum += 1
            if 'Truth=1' in line and 'Predict=1' in line:
                be_correct += 1
            if 'Truth=0' in line and 'Predict=0' in line:
                be_correct += 1

        for so in Auxiliary_So:
            if so in line:
                so_sum += 1
                if 'Truth=1' in line and 'Predict=1' in line:
                    so_correct += 1
                if 'Truth=0' in line and 'Predict=0' in line:
                    so_correct += 1

        if 'have' in line:
            have_sum += 1
            if 'Truth=1' in line and 'Predict=1' in line:
                have_correct += 1
            if 'Truth=0' in line and 'Predict=0' in line:
                have_correct += 1

        if 'to' in line:
            to_sum += 1
            if 'Truth=1' in line and 'Predict=1' in line:
                to_correct += 1
            if 'Truth=0' in line and 'Predict=0' in line:
                to_correct += 1

        for modal in Auxiliary_Modal:
            if modal in line:
                modal_sum += 1
                if 'Truth=1' in line and 'Predict=1' in line:
                    modal_correct += 1
                if 'Truth=0' in line and 'Predict=0' in line:
                    modal_correct += 1


P = TP / (TP + FP)
R = TP / (TP + FN)
F1 = (2 * P * R) / (P + R)

print('do = ' + str(do_correct/do_sum))
print('be = ' + str(be_correct/be_sum))
print('have = ' + str(have_correct/have_sum))
print('modal = ' + str(modal_correct/modal_sum))
print('to = ' + str(to_correct/to_sum))
print('so = ' + str(so_correct/so_sum))
print('all = ' + str((TP+TN)/all_sum))

print('')
print('P = ' + str(P))
print('R = ' + str(R))
print('F1 = ' + str(F1))

print ('')
print('FP = ' + str(FP))
print('FN = ' + str(FN))
print('TP = ' + str(TP))
print('TN = ' + str(TN))
