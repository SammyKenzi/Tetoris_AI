import random
import numpy
import copy
from battle import Battle

# パラメータ
battle = Battle(0,[0,0])
gene_length = battle.layers[0]*battle.layers[1] + battle.layers[1] + battle.layers[1] + battle.layers[2] # 遺伝子長
individual_length = 18 # 個体数
generation = 100 # 世代数
try_num = 3
top_individual = 5


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
        if k < battle.layers[0]*battle.layers[1] + battle.layers[1]:
            if k < battle.layers[0] * battle.layers[1]:
                pop2.append(pop[k])
            else:
                middle_list2.append(pop[k])       
        else:
            if k < (battle.layers[0]+2)*battle.layers[1]:
                mini_list.append(pop[k])
    middle_list1 = numpy.array(pop2).reshape(battle.layers[1], -1).tolist()
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
    ranking_rate = [1,1,1,1,1,1, 2,2,2,2, 3,3,3, 4,4, 5, 6, 7, 8, 9]
    #ranking_rate = [1,1,2,2,3]
    point = random.randint(1, len(ranking_rate))
    choiced = ranking_rate[point-1]
    return fitness[choiced-1][1] #選ばれた遺伝子

# 総当たり(population : [[weights, biases], ...])
def round_robin(population,generation):
    wins = [0] * individual_length
    for i in range(individual_length):
        for j in range(i+1,individual_length):
            if i != j:
                print("Number {} VS Number {}".format(i,j))
                for k in range(try_num):
                    battle = Battle(generation,[i,j])
                    win = battle.run(population[i], population[j])
                    if win == 1:
                        wins[i] += 1
                    else:
                        wins[j] += 1
    return wins

def main():
    # 初期個体生成
    battle_list= []
    first_gene = get_population()
    for i in range(individual_length):
        battle_list.append(fitness(first_gene[i]))
    pop = [] # [ [score, [weights, biases]], ...]
    wins = round_robin(battle_list, 0)
    for i in range(individual_length):
        pop.append([wins[i], first_gene[i]])
    pop = evaluate(pop)
    print('Generation : 0')
    print('Max Score : ' + str(pop[0][0]))
    print('------------------------------')

    for g in range(generation):
        print('Generation : ' + str(g+1))
        # エリートを選択
        eva = evaluate(pop)
        pop = []
        battle_list = []
        for i in range(top_individual):
            elites = eva[i]
            pop.append(elites)
        # 突然変異, 交叉
        next_gene = []
        while len(pop) < individual_length:
            parent1 = ranking_chice(eva)
            parent2 = ranking_chice(eva)
            child_gene = cross(parent1, parent2) # 子の遺伝子を１次元配列で
            next_gene.append(child_gene) # 次世代の遺伝子リスト
            battle_list.append(fitness(child_gene))
        wins = round_robin(battle_list, g+1)
        for i in range(individual_length):
            pop.append([wins[i], next_gene[i]])
        
        # 評価
        eva = evaluate(pop)
        pop = eva

        print('Min : {}'.format(pop[-1][0]))
        print('Max : {}'.format(pop[0][0]))
        print('Result : {}'.format(pop[0]))
        print('--------------------------')


if __name__ == '__main__':
    main()
