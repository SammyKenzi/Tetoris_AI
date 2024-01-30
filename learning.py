import random
import numpy
import copy
from neural_network import Neural_Network

# パラメータ
neural = Neural_Network()
gene_length = neural.layers[0]*neural.layers[1] + neural.layers[1] + neural.layers[1] + neural.layers[2] # 遺伝子長
individual_length = 5 # 個体数
generation = 50 # 世代数
mutate_rate = 0.1 # 突然変異の確率
neural = Neural_Network()
try_num = 3
top_indivisual = 1


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

# 交叉（一様交叉）（遺伝子は１次元のほうが扱いやすい）
def cross(parent1, parent2):
    child_gene = []
    for i in range(gene_length):
        x = random.random()
        if x < 0.42:
            p = parent1[i]
        elif x < 0.84:
            p = parent2[i]
        elif x < 0.99:
            p = (parent1[i] + parent2[i]) / 2
        else: # 突然変異
            p = random.random()
        child_gene.append(p)
    return child_gene # １次元配列で返す


# ランキング選択(fitness : [ 適応度, [パラメータ], ...] (降順))
def ranking_chice(fitness):
    #ranking_rate = [1,1,1,1,1,1, 2,2,2,2, 3,3,3, 4,4, 5, 6, 7, 8, 9]
    ranking_rate = [1,1,2,2,3]
    point = random.randint(1, len(ranking_rate))
    choiced = ranking_rate[point-1]
    return fitness[choiced-1][1] #選ばれた遺伝子

#average
def try_average(para): # para1 : runを実行できる直前のlist ([重み , バイアス])
    sum = 0
    for i in range(try_num):
        neural = Neural_Network()
        sum += neural.run(para[0], para[1])
    return sum/try_num

def main():
    # 初期個体生成
    pop = []
    for i in range(individual_length):
        neural = Neural_Network()
        pop.append([try_average(fitness(get_population()[i])), get_population()[i]])
    pop = evaluate(pop)
    print('Generation : 0')
    print('Max Score : ' + str(pop[0][0]))
    print('------------------------------')

    for g in range(generation):
        print('Generation : ' + str(g+1))
        # エリートを選択
        eva = evaluate(pop)
        pop = []
        for i in range(top_indivisual):
            elites = eva[i]
            pop.append(elites)
        # 突然変異, 交叉
        while len(pop) < individual_length:
            parent1 = ranking_chice(eva)
            parent2 = ranking_chice(eva)
            child_gene = cross(parent1, parent2) # 子の遺伝子を１次元配列で
            score = try_average(fitness(child_gene))
            pop.append([score, child_gene])
        
        # 評価
        eva = evaluate(pop)
        pop = eva
        print(len(pop))

        print('Min : {}'.format(pop[-1][0]))
        print('Max : {}'.format(pop[0][0]))
        print('Result : {}'.format(pop[0]))
        print('--------------------------')


if __name__ == '__main__':
    main()