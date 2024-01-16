import random
import tetris


#適応度関数（テトリスを実行後のスコア＝適応度　とする）
def fitness_function(p):
    tetris.Tetris().ai_run(p)
    return tetris.Tetris().score

#第１世代（ランダム）
def generate_individual():
    tetris.Tetris().ai_run()
    return 

# 選択（トーナメント選択）
def tournament_selection(population, tournament_size):
    tournament = random.sample(population, tournament_size)
    return max(tournament, key=lambda x: x[1])  # 最も適応度が高い個体を選択

# 交叉（一点交叉）
def crossover(parent1, parent2):
    crossover_point = random.randint(0, len(parent1) - 1)
    child = parent1[:crossover_point] + parent2[crossover_point:]
    return child

# 突然変異
def mutate(individual, mutation_rate):
    if random.uniform(0, 1) < mutation_rate:
        mutation_amount = random.uniform(-0.5, 0.5)
        individual += mutation_amount
    return individual


#遺伝的アルゴリズム
def genetic_algorithm(population_size, generations, tournament_size, mutation_rate):
    population = [(generate_individual(), 0) for _ in range(population_size)]

    for generation in range(generations):
        #適応度の計算
        population = [(individual, fitness_function(individual)) for individual, _ in population]

        #新しい世代の生成
        print("Generation " + str(_))
        new_population = []
        for _ in range(population_size // 2):
            parent1 = tournament_selection(population, tournament_size)
            parent2 = tournament_selection(population, tournament_size)

            child1 = crossover(parent1[0], parent2[0])
            child2 = crossover(parent2[0], parent1[0])

            child1 = (mutate(child1, mutation_rate), 0)
            child2 = (mutate(child2, mutation_rate), 0)

            new_population.extend([child1, child2])

        population = new_population

        # 最良個体の表示
        best_individual = max(population, key=lambda x: x[1])
        print(f"Generation {generation + 1}: Best Individual = {best_individual[0]}, Fitness = {best_individual[1]}")

    # 最終世代の最良個体を返す
    return max(population, key=lambda x: x[1])

# メイン関数
if __name__ == "__main__":
    population_size = 3
    generations = 50
    tournament_size = 3
    mutation_rate = 0.1

    best_solution = genetic_algorithm(population_size, generations, tournament_size, mutation_rate)
