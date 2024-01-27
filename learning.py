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


# 第1世代の個体群を生成　個体は以下のようにあらわす
# [ 適応度（最終スコア）, [ 遺伝子（パラメータ]]
def get_population():
    population = []
    for i in range(individual_length):
        population.append([random.random() for j in range(gene_length)]) # 初期パラメータを決める
    return population

# パラメータの次元を変換する
def change_para_dimention(para):
    if(len(para) == 2):
        new_list = []
        for i in range(len(para[0])):
            new_list.append(para[0][i])
        for i in range(len(para[1])):
            new_list.append(para[1][i])
        return new_list
    else:
        return 0


# 適応度の計算(パラメータの次元を合わせるだけ（メイン関数で実際に計算する)
def fitness(pop): # pop は１次元配列で、パラメータを並べたもの（[[weights], [biases]] の形にしてからrunする）
    print(pop)
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
    for i in range(3):
        neural = Neural_Network()
        sum += neural.run(para1, para2)
    return sum/3

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
    main()
'''
Generation : 2
-1000
-1000
66
-1000
-1000
-1000
-1000
-1000
55
60
-1000
-1000
-1000
-1000
-1000
-1000
-1000
-1000
-1000
-1000
-1000
-1000
-1000
-1000
-1000
60
-1000
-1000
-1000
-1000
-1000
-1000
Min : -1000.0
Max : -464.5
Result : [-464.5, [0.8877267130049408, 0.04513974583728053, 0.45087311909200467, 0.7520762463175805, 0.472454159608377, 0.5791802583045745, 0.1727913042676691, 0.21753187549605169, 0.9511616884992243, 0.9924967021387068, 0.8217796304587063, 0.7183518849250142, 0.8667469135591556, 0.855668829932274, 0.5537085275017275, 0.31733647332632, 0.8114397087620755, 0.26668624394570983, 0.2386498756590133, 0.9634261031661933, 0.6978744025254705, 0.464717225026439, 0.842836649821497, 0.6279126459889504, 0.5602128753938861, 0.015590959790790504, 0.9611699248166082, 0.5812012245863031]]
'''