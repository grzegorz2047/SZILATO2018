from deap import creator, base, tools
import random
import A_star
import game_logic
import copy



def prepare_genetic(LogicEngine):
    """
    prepares the genetic algorithm using the deap library
    :param LogicEngine:
    :return:
    """
    #1: count of enemies, my_own hp, number of enemy hp
    #fitness function that aims to minimize first objective, and maximize the second, minimize the third
    creator.create("FitnessMulti", base.Fitness, weights=(-100.0, 1.0, -10.0))


    creator.create("Individual", list, fitness=creator.FitnessMulti)
    #individual with genes of the form of list, that take previously defined fitness function
    toolbox = base.Toolbox()

    #registers function that generates genes
    max_gene_value = len(LogicEngine.monsters + LogicEngine.mixtures)
    toolbox.register("attr_int", random.randrange, 0, max_gene_value,  1)

    #registers how to make an individual
    toolbox.register("individual", tools.initRepeat, creator.Individual,
                     toolbox.attr_int,  len(LogicEngine.monsters + LogicEngine.mixtures) * 3)


    #registers evaluate function
    toolbox.register("evaluate", evaluate_state_after_moves, LogicEngine = LogicEngine)
    #registers how to make a population
    toolbox.register("population", tools.initRepeat, list, toolbox.individual)

    #create population of 300
    pop = toolbox.population(n=350)

    print("GENETIC LOG: PREPARED THE GENETIC ALGORITHM")

    #evaluates the entire population
    fitnesses = list(map(toolbox.evaluate, pop))
    for ind, fit in zip(pop, fitnesses):
        ind.fitness.values = fit
        print(ind.fitness.values)
    print("GENETIC LOG: SIMULATED SCORES OF 1ST GEN")




def evaluate_state_after_moves(individual, LogicEngine):
    """
    function that evaluates individual's fitness socre
    :param individual:
    :return:
    """
    simulated_logic_engine = simulate_from_list(individual, LogicEngine)
    count_of_alive_enemies = simulated_logic_engine.alive_monsters_count()
    player_hp = simulated_logic_engine.player.hp
    sum_of_enemy_hp = simulated_logic_engine.get_all_hp()
    if(player_hp > 0):
        return count_of_alive_enemies, player_hp, sum_of_enemy_hp
    else:
        return 100000, 0, 100000

def simulate_from_list(list_of_indexes_of_objects_to_visit, LogicEngine):
    """
    simulates the game from starting LogicEngine Position using the list of objects in order to visit
    :param LogicEngine: starting state of LogicEngine
    :param list_of_indexes_of_objects_to_visit:
    :return:
    """
    original_object_list = copy.deepcopy(LogicEngine.original_object_list)
    simulated_logic_engine = LogicEngine
    for index in list_of_indexes_of_objects_to_visit:
        if(simulated_logic_engine.get_list_of_all_objects()[index].alive == True
        and [simulated_logic_engine.get_list_of_all_objects()[index].x, simulated_logic_engine.get_list_of_all_objects()[index].y] in simulated_logic_engine.get_all_available_targets()):
            simulated_logic_engine = simulated_logic_engine.simulate_move_absolute_coordinate(save_simulated_state_JSON = False, x = simulated_logic_engine.get_list_of_all_objects()[index].x, y = simulated_logic_engine.get_list_of_all_objects()[index].y)
            if(simulated_logic_engine.alive_monsters_count() == 0 or simulated_logic_engine.player.hp <= 0):
                break
    return simulated_logic_engine