import re

str1 = input()
str2 = input()

str1 = str1.lower()
str2 = str2.lower()

str1_dic, str2_dic = {}, {}
for key in range(0,len(str1)-1):
    sub = re.sub("[0-9]|[\s]+|[+-=.#/?:$!*^}]",'', str1[key:key+2])
    if len(sub) == 2:
        if str1[key:key+2] in str1_dic:
            str1_dic[str1[key:key+2]] += 1
        else :
            str1_dic[str1[key:key+2]] = 1

for key in range(0, len(str2) - 1):
    sub = re.sub("[0-9]|[\s]+|[+-=.#/?:$!*^}]", '', str2[key:key+2])
    if len(sub) == 2:
        if str2[key:key+2] in str2_dic:
            str2_dic[str2[key:key+2]] += 1
        else :
            str2_dic[str2[key:key+2]] = 1

inter_num = 0
uni_num = 0

for key in str1_dic.keys():
    if key in str2_dic:
        inter_num += min(str1_dic[key], str2_dic[key])
        uni_num += max(str1_dic[key], str2_dic[key])
        del str2_dic[key]
    else:
        uni_num += str1_dic[key]

for value in str2_dic.values():
    uni_num += value

similarity = 0
if uni_num == 0:
    similarity = 1
else:
    similarity = inter_num/uni_num

print(int(similarity*65536))


