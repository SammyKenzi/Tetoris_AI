import random
import numpy
import copy
from neural_network import Neural_Network

# パラメータ
neural = Neural_Network()
gene_length = neural.layers[0]*neural.layers[1] + neural.layers[1] + neural.layers[1] + neural.layers[2] # 遺伝子長
individual_length = 10 # 個体数
generation = 50 # 世代数
mutate_rate = 0.1 # 突然変異の確率
eliter_rate = 0.2 # エリート選択の割合
neural = Neural_Network()
try_num = 4


# 第1世代の個体群を生成　個体は以下のようにあらわす
# [ 適応度（最終スコア）, [ 遺伝子（パラメータ]]
def get_population(): # １次元配列で出力
    population = []
    for i in range(individual_length):
        population.append([random.random() for j in range(gene_length)]) # 初期パラメータを決める
    return population


# パラメータの次元を合わせる 
# １次元配列　-> 
# [[[隠れ層1への枝(16)], [隠れ層2への枝(16)], [隠れ層3への枝(16)]],
# [[出力層への枝(3)]],
# [[隠れ層のバイアス(3)],
# [出力層のバイアス(1)]]]
def fitness(pop): # pop は１次元配列
    mini_list = []
    pop2 = []
    middle_list1 = []
    middle_list2 = []
    for k in range(len(pop)):
        if k < neural.layers[0]*neural.layers[1] + neural.layers[1]:
            if k < neural.layers[0] * neural.layers[1]:
                pop2.append(pop[k])
            else:
                middle_list2.append(pop[k])       
        else:
            if k < (neural.layers[0]+2)*neural.layers[1]:
                mini_list.append(pop[k])
    middle_list1 = numpy.array(pop2).reshape(neural.layers[1], -1).tolist()
    new_list = [[middle_list1, [middle_list2]], [mini_list, [pop[len(pop)-1]]]]
    return [new_list[0], new_list[1]]

# 適応度を高い順に並び替え
def evaluate(pop):
    pop.sort(reverse=True, key=lambda x:x[0])
    return pop

# 交叉（1点交叉法）（遺伝子は１次元のほうが扱いやすい）
def two_point_crossover(parent1, parent2):
    r1 = random.randint(0, gene_length-1)
    #r2 = random.randint(r1, gene_length-1)
    child = copy.deepcopy(parent1)
    child[r1:gene_length] = parent2[r1:gene_length]
    return child

# 突然変異
def mutate(parent):
    r = random.randint(0, gene_length-1)
    child = copy.deepcopy(parent)
    child[r] *= 2 # 与える変化
    return child

# ランキング選択(fitness : [ 適応度, [パラメータ], ...] (降順))
def ranking_chice(fitness):
    ranking_rate = [1,1,1,1,1,1, 2,2,2,2, 3,3,3, 4,4, 5, 6, 7, 8, 9]
    point = random.randint(1, 20)
    choiced = ranking_rate[point-1]
    return fitness[choiced-1][1] #選ばれた遺伝子

#average
def try_average(para1,para2):
    sum = 0
    for i in range(try_num):
        neural = Neural_Network()
        sum += neural.run(para1, para2)
    return sum/try_num

def main():
    # 初期個体生成
    pop = []
    for i in range(individual_length):
        neural = Neural_Network()
        pop.append([try_average(fitness(get_population()[i])[0], fitness(get_population()[i])[1]), get_population()[i]])
    pop = evaluate(pop)
    print('Generation : 0')
    print('Max Score : ' + str(pop[0][0]))
    print('------------------------------')

    for g in range(generation):
        print('Generation : ' + str(g+1))

        # エリートを選択
        eva = evaluate(pop)
        elites = eva[:int(len(pop)*eliter_rate)]
        pop = elites
        # 突然変異, 交叉
        while len(pop) < individual_length:
            if random.random() < mutate_rate:
                m = random.randint(0, len(elites)-1)
                child = mutate(elites[m][1])
            else:
                m1 = ranking_chice(eva)
                m2 = ranking_chice(eva)
                child = two_point_crossover(m1, m2)
            neural = Neural_Network()
            pop.append([try_average(fitness(child)[0], fitness(child)[1]), child])
        
        # 評価
        eva = evaluate(pop)
        pop = eva

        print('Min : {}'.format(pop[-1][0]))
        print('Max : {}'.format(pop[0][0]))
        print('Result : {}'.format(pop[0]))
        print('--------------------------')


if __name__ == '__main__':
    a = get_population()
    print(a[0])
    try_average(fitness([0.5687704444210947, 0.7514973650297183, 0.5999409274909423, 0.3160275218886778, 0.5649244889410366, 0.056615117677696336, 0.8049260401867924, 0.2135799446852602, 0.9232150419431141, 0.8805907136485752, 0.21958168475209816, 0.39345737845541406, 0.4143307471447828, 0.37777281617494574, 0.8568384085120957, 0.8788756418422684, 0.9130737355988718, 0.32779641878412835, 0.08852187739344652, 0.49554531080780306, 0.4537544189441871, 0.2588918321184205, 0.018643081348969193, 0.20213123684666912, 0.49600564548643544, 0.28553855718433707, 0.6838658241374191, 0.5746408897812404])[0], fitness([0.5687704444210947, 0.7514973650297183, 0.5999409274909423, 0.3160275218886778, 0.5649244889410366, 0.056615117677696336, 0.8049260401867924, 0.2135799446852602, 0.9232150419431141, 0.8805907136485752, 0.21958168475209816, 0.39345737845541406, 0.4143307471447828, 0.37777281617494574, 0.8568384085120957, 0.8788756418422684, 0.9130737355988718, 0.32779641878412835, 0.08852187739344652, 0.49554531080780306, 0.4537544189441871, 0.2588918321184205, 0.018643081348969193, 0.20213123684666912, 0.49600564548643544, 0.28553855718433707, 0.6838658241374191, 0.5746408897812404])[1])
