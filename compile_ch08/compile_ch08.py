# coding=utf-8

'''
Author: ripples
Email: ripplesaround@sina.com

date: 2020/6/25 16:52
desc: 编译计算ud链和du链的程序
'''

# 流图G 如何表示
# 矩阵？两个矩阵，既要表示基本块内部的信息，也要表示之间的联系

# num_block = 6
# num_var   = 5
# num_sen   = 11
num_block = 4
num_var   = 6
num_sen   = 10

# 行表示变量(ABCDE)，列表示第几句(11)，1表示定值，2表示引用,3表示即定值又引用
# G_inside = [[1,1,2,2,3,4,4,5,5,6,6],    #块号
#             [0,0,1,2,0,0,2,0,0,0,0],    #A
#             [1,0,2,0,0,2,2,2,0,1,2],    #B
#             [0,1,2,2,2,3,0,2,0,2,1],    #C
#             [0,0,0,1,3,0,0,1,0,2,2],    #D
#             [0,0,0,0,0,0,1,0,3,0,0]     #E
#             ]

G_inside = [[1,1,2,2,2,3,3,4,4,4],    #块号
            [1,2,0,0,0,0,0,0,0,0],    #f
            [2,0,0,0,0,2,0,0,1,0],    #i
            [2,0,0,1,0,0,0,2,0,0],    #b
            [0,2,2,2,0,0,2,0,0,0],    #g
            [0,0,1,0,2,0,0,0,0,0],     #a
            [0,0,0,0,0,1,2,1,2,2]     #c
            ]
# 基本块的相连情况(6个)  有向图
# G_connect = [[0,1,0,0,0,0],
#              [0,0,1,1,0,0],
#              [0,0,0,1,1,0],
#              [0,1,0,0,0,1],
#              [0,0,1,0,0,0],
#              [0,0,0,0,0,0]
#              ]

G_connect = [[0,1,1,0],
             [0,0,0,1],
             [0,0,1,0],
             [1,0,0,0]
             ]

# 定值点数据流方程
Gen_var = [set() for i in range(num_block)]
Kill_var = [set() for i in range(num_block)]
In = [set() for i in range(num_block)]
Out = [set() for i in range(num_block)]
ud_link = [[set() for i in range(num_var)] for i in range(num_block)]

def ud_init():
    '''
    没有考虑一个基本快内多次定值
    :return:
    '''
    for i in range(num_sen):
        for j in range(num_var):
            if G_inside[j+1][i] == 1 or G_inside[j+1][i] == 3:
                Gen_var[G_inside[0][i]-1].add(i+1)
                for k in range(num_sen):
                    if (G_inside[j+1][k] == 1 or G_inside[j+1][k] == 3) and k != i:
                        Kill_var[G_inside[0][i] - 1].add(k+1)
                break
    for i in range(num_block):
        Out[i] = Gen_var[i]

def data_stream_cal_ud():
    cnt = 1
    change = True
    while(change):
        change = False
        print("第{cnt}次循环".format(cnt = cnt))
        cnt+=1
        for i in range(num_block):
            newIn = set()
            # 找到前驱节点
            pred = []
            for j in range(num_block):
                if G_connect[j][i] == 1:
                    pred.append(j)
            for j in pred:
                for item in Out[j]:
                    newIn.add(item)

            if not (newIn.issubset(In[i]) and In[i].issubset(newIn)):
                change = True
                In[i] = newIn
                # Out[i] = In[i] - (Kill_var[i]|Gen_var[i])
                Out[i] = (In[i] - Kill_var[i]) | Gen_var[i]





# 活跃变量数据流方程
var_info = [[] for i in range(num_var)]
var_table = [[] for i in range(num_block)]
In_L = [[set() for i in range(num_var)] for i in range(num_block)]
Out_L = [[set() for i in range(num_var)] for i in range(num_block)]
Use_L = [[set() for i in range(num_var)] for i in range(num_block)]
Use = [[set() for i in range(num_var)] for i in range(num_block)]   # 最后计算ud链可以用
Def_L = [[set() for i in range(num_var)] for i in range(num_block)]
Def = [[set() for i in range(num_var)] for i in range(num_block)]  # 最后计算du链的时候使用
Out_L_norm =  [[] for i in range(num_block)]
du_link =  [[set() for i in range(num_var)] for i in range(num_block)]

def du_init():
    '''
    构造表，参考课件
    :return:
    '''
    global  var_table
    len = 0
    for i in range(num_var):
        for j in range(num_sen):
            if G_inside[i+1][j] == 2 or G_inside[i+1][j] == 3:
                var_info[i].append(j+1)
                len+=1
    temp = [ 0 for i in range(len)]
    var_table = [temp for i in range(num_block)]

    # 构造use_L和def_L
    # def_L 为在基本块B中定值的，但定之前未曾在B中引用过的集合
    for i in range(num_sen):
        current_block = G_inside[0][i]
        for j in range(num_var):
            if G_inside[j+1][i] == 1 or G_inside[j+1][i] == 3:
                # 之前未引用
                flag = 0
                temp = i-1
                while(temp>=0):
                    now_block = G_inside[0][temp]
                    if now_block != current_block:
                        break
                    if G_inside[j + 1][temp]== 2 or G_inside[j + 1][temp] == 3:
                        flag = 1
                    temp-=1
                if flag == 0:
                    Def_L[current_block-1][j].add(i+1)
                Def[current_block-1][j].add(i+1)

    # use_L 为在基本块B中引用的，但引用前未曾在B中定值的集合
    for i in range(num_sen):
        current_block = G_inside[0][i]
        for j in range(num_var):
            if G_inside[j+1][i] == 2 or G_inside[j+1][i] == 3:
                # 之前未引用
                flag = 0
                temp = i-1
                while(temp>=0):
                    now_block = G_inside[0][temp]
                    if now_block != current_block:
                        break
                    if G_inside[j + 1][temp]== 1 or G_inside[j + 1][temp] == 3:
                        flag = 1
                    temp-=1
                if flag == 0:
                    Use_L[current_block-1][j].add(i+1)
                Use[current_block - 1][j].add(i + 1)

def data_stream_cal_du():
    global Out_L
    global In_L
    global Out_L_norm
    cnt = 1
    change = True
    while(change):
        change = False
        print("第{cnt}次循环".format(cnt = cnt))
        cnt+=1
        for i in range(num_block-1,-1,-1):
            temp = [set() for i in range(num_var)]
            # 找到后继节点
            succ = []
            for j in range(num_block):
                if G_connect[i][j] == 1:
                    succ.append(j)
            for j in succ:
                for k in range(num_var):
                    temp[k] = temp[k]|In_L[j][k]
            Out_L[i] = temp
            newIn = [set() for i in range(num_var)]

            flag = False
            for j in range(num_var):
                # newIn[j] = (Out_L[i][j] - Def_L[i][j])
                # 这里要注意 只要集合里有就不能要
                newIn[j] = Out_L[i][j]
                if len(Def_L[i][j])>0:
                    newIn[j] =  set()
                newIn[j] = newIn[j]|Use_L[i][j]
                if not (In_L[i][j].issubset(newIn[j]) and newIn[j].issubset(In_L[i][j])):
                    flag = True
            # print(newIn)
            if flag:
                change = True
                In_L[i] = newIn
    for i in range(num_block):
        for j in range(num_var):
            if len(Out_L[i][j])>0:
                Out_L_norm[i].append(j+1)

def cal_link():
    '''
    计算ud_link要用到use集合，计算du链要用到def集合
    :return:
    '''
    global ud_link
    global du_link
    global Out_L_norm
    global Out_L

    # 计算ud链
    for i in range(num_block):
        if len(In[i])>0:
            for j in range(num_var):
                if len(Use[i][j])>0:
                    for temp in In[i]:
                        if G_inside[j+1][temp-1] == 1 or G_inside[j+1][temp-1] == 3:
                            # 块内存在定值点
                            flag = True
                            for use_temp in Use[i][j]:
                                tem = -1
                                for item in Def[i][j]:
                                    # 可能有多个use
                                    if item < use_temp and item > tem:
                                        tem = item
                                        flag = False
                                        # print("tem",tem)
                                if tem>-1:
                                    ud_link[i][j].add(tem)


                            if flag:
                                ud_link[i][j].add(temp)

    # 计算du链
    for i in range(num_block):
        for j in range(num_var):
            if len(Def[i][j])>0:
                du_link[i][j] = Out_L[i][j]
                for def_sen_num in Def[i][j]:
                    def_sen_num -=1
                    current_block = G_inside[0][def_sen_num]
                    temp = def_sen_num + 1
                    while(temp < num_sen):
                        now_block = G_inside[0][temp]
                        if(now_block!=current_block):
                            break
                        if G_inside[j+1][temp] == 2 or G_inside[j+1][temp] == 3:
                            du_link[i][j].add(temp+1)
                        temp+=1
                    if len(du_link[i][j])==0:
                        du_link[i][j].add(-1)

if __name__ == '__main__':
    print("程序开始运行")
    print("到达—定值数据流方程")
    ud_init()
    data_stream_cal_ud()
    print("In")
    for i in range(num_block):
        print(In[i])
    print("--------------------------")
    print("活跃变量数据流方程")
    du_init()
    data_stream_cal_du()
    print("Out_L")
    for i in range(num_block):
        print(Out_L_norm[i])
    print("--------------------------")
    cal_link()
    print("ud链")
    for i in range(num_block):
        print(ud_link[i])
    print("du链")
    for i in range(num_block):
        print(du_link[i])