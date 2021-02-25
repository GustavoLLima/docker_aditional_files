# -*- coding: utf-8 -*-
#from fuzzywuzzy import fuzz
import random
import string

import subprocess, sys
import json

import os
import signal

import copy

import socket
import sys
import json
from time import time, sleep

def execute_model():
    #cmd = "netlogo-headless.bat --model teste6_fitness_desvio.nlogo --experiment experiment2"
    # cmd = "netlogo-headless.bat --model "+'"C:\\Program Files\\NetLogo 6.0.4\\teste6_fitness_desvio.nlogo"'+" --experiment experiment2"
    cmd = "/opt/netlogo/netlogo-headless.sh --model /teste/teste6_fitness_desvio.nlogo --experiment experiment2"
    print (cmd)
    os.system(cmd)

    # p = subprocess.Popen(cmd, shell=False, stderr=subprocess.PIPE)

    # while True:
    #     out = p.stderr.read(1)
    #     #print (out.decode())
    #     if out.decode() == '' and p.poll() != None:
    #         break



    # cmd = "netlogo-headless.bat --model teste.nlogo --experiment experiment2"

    # p = subprocess.Popen(cmd, shell=False, stderr=subprocess.PIPE)
    # #p = subprocess.Popen(cmd, stderr=subprocess.PIPE, shell=True, encoding = "ISO-8859-1")

    # while True:
    #     out = p.stderr.read(1)
    #     #if out.decode() == '' and p.poll() != None:
    #     if (out == '' and p.poll() != None):
    #         break
    #     #sys.stdout.flush()

    # #p.kill()

def generate_input_file(parameters):

    conf_parameters = copy.deepcopy(parameters)


    if(len(conf_parameters) != 18):
        conf_parameters.append(["show-energy?", False])
        conf_parameters.append(["enable-seasons", True])
        #parameters.append(["enable-seasons", False])
        conf_parameters.append(["model-version", "sheep-wolves-grass"])


        # conf_parameters.append(["grass-regrowth-time", 30])

        # conf_parameters.append(["sheep-gain-from-food", 4])
        # conf_parameters.append(["wolf-gain-from-food", 20])

        # conf_parameters.append(["sheep-reproduce", 4])
        # conf_parameters.append(["wolf-reproduce", 5])


        conf_parameters.append(["min-temp-summer", 17])
        conf_parameters.append(["max-temp-summer", 28])

        conf_parameters.append(["min-temp-fall", 12])
        conf_parameters.append(["max-temp-fall", 23])

        conf_parameters.append(["min-temp-winter", 9])    
        conf_parameters.append(["max-temp-winter", 19])

        conf_parameters.append(["min-temp-spring", 13])
        conf_parameters.append(["max-temp-spring", 23])

    #open('config.txt', 'w').close()

    with open("/teste/config.txt", "w") as output:
        for x in conf_parameters:

            x[0] = x[0].replace('"', '')
            #if (type(x[1]) == str)

            x[0] = '"' + x[0] + '"'

            if(type(x[1]) is str):
                x[1] = str(x[1]).replace('"', '')
                x[1] = '"' + x[1] + '"'

            aaa = json.dumps(x)

            g = ' '.join(map(str,x))

            g = '[' + g + ']'

            #print (g)
            output.write("%s\n" % (g))

    open('/teste/export-ticks.txt', 'w').close()

def remove_space(filename):
    # filename = "C:/Users/Gustavo/Desktop/export-ticks.txt"

    with open(filename) as f:
        first_line = f.readline()
        first_line = first_line[1:]

    with open(filename, "w") as output:
        output.write("%s" % (first_line))


    # f = open(filename, "r")
    # print(f.read())







class Agent:

    def __init__(self, length):

        list = []

        #print ("parameters")
        #print (len(parameters))

        for name, low, high in parameters:
            list.append([name, random.randint(low, high)])



        #ADICIONAR ISSO NA HORA DE CRIAR O ARQUIVO

        #parameters.append(["show-energy?", False])
        #parameters.append(["enable-seasons", True])    
        
        #parameters.append(["model-version", "sheep-wolves-grass"])

        self.list = list



        self.fitness = 99999

    def __str__(self):

        return 'Agent: ' +  str(self.list) + ' Fitness: ' + str(self.fitness)
        #return 'Fitness: ' + str(self.fitness)


def ga():

    best_agent = Agent(0)

    agents = init_agents(population, in_str_len)

    for generation in range(generations):

        print ("------------------------------------------------------")
        print ('Generation: ' + str(generation))

        # print ("agentes antes do fitness:")
        # for agent in agents:
        #     print (agent)

        agents = fitness(agents)
        

        # print ("sorted agents:")
        # for agent in agents:
        #     print (agent.fitness)


        print ("agent0 fitness")
        print (agents[0].fitness)
        print ("best_agent fitness")
        print (best_agent.fitness)
        if(agents[0].fitness < best_agent.fitness):
            # print ("entrou")
            # print (agents[0].fitness)
            # print (best_agent.fitness)
            # print ("Prev. best")
            # print(best_agent)
            best_agent = copy.deepcopy(agents[0])
            print ("New best")
            print(best_agent)

            if (best_agent.fitness == 0):
                print ("********")
                print ("Threshold met!")
                print ("Best Agent")
                print(best_agent)
                print ("Number of generations: ")
                print (str(generation))
                print ("********")
                exit(0)

        print ("Best of generation:")
        print (agents[0].fitness)
        print ("Best until now:")
        print (best_agent)
        print ("------------------------------------------------------")


        


        agents = selection(agents)
        agents = crossover(agents)
        #agents = mutation(agents)

        # if(agents[0].fitness > best_agent.fitness):
        #     print ("entrou")
        #     print (agents[0].fitness)
        #     print (best_agent.fitness)
        #     print ("Prev. best")
        #     print(best_agent)
        #     best_agent = agents[0]
        #     print ("New best")
        #     print(best_agent)

        # print ("Best of generation:")
        # print (agents[0].fitness)
        # print ("Best until now:")
        # print (best_agent)
        # print ("------------------------------------------------------")

        # if any(agent.fitness >= 90 for agent in agents):

        #     print ('Threshold met!')
        #     #best = agents[0]
        #     #break
        #     exit(0)
    return best_agent

def init_agents(population, length):

    list_pop = []

    special_agent = Agent(length)

    special_agent.list = []

    special_agent.list.append(["initial-number-sheep", 171])
    special_agent.list.append(["initial-number-wolves", 156])

    special_agent.list.append(["grass-regrowth-time", 14])

    special_agent.list.append(["sheep-gain-from-food", 10])
    special_agent.list.append(["wolf-gain-from-food", 6])

    special_agent.list.append(["sheep-reproduce", 8])
    special_agent.list.append(["wolf-reproduce", 2])

    list_pop.append(special_agent)

    for x in range(population - 1):
        new_agent = Agent(length)
        list_pop.append(special_agent)

    return list_pop

    # return [Agent(length) for _ in range(population)]




    # agents = []

    # agent_id = 0

    # for x in range(population):
    #     new_agent = Agent(length, agent_id)
    #     agent_id += 1
    #     agents.append(new_agent)


    # return agents

def fitness(agents):

    for agent in agents:

        if agent.fitness == 99999:

            avg = 0

            for x in range(1):

                ##AQUI VAI CRIAR O ARQUIVO, CHAMAR A FUNÇÃO, LER O RETORNO. ESSE VAI SER O FITNESS
                #TALVEZ AQUI VER SE TODOS OS PARÂMETROS SÃO ACEITOS. SE NÃO, RETORNAR FITNESS SEM SIMULAR
                
                #agent.fitness = fuzz.ratio(agent.list, in_str)

                generate_input_file(agent.list)
                #print ("-")
                execute_model()
                os.remove("/teste/config.txt")
                #print ("-")

                filename = "/teste/export-ticks.txt"

                remove_space(filename)
                f = open(filename, "r")

                #agent.fitness = (int(f.read()))

                avg = avg + (float(f.read()))
                #print("fitness: ")
                #print((f.read()))

                # print ("\n")
                # print(agent)
                
                #agent.fitness = random.randint(0, 89)

            avg = avg / 1

            agent.fitness = avg

        print ("\n")
        print(agent)

    agents = sorted(agents, key=lambda agent: agent.fitness, reverse=False)
    return agents


def selection(agents):

    agents = sorted(agents, key=lambda agent: agent.fitness, reverse=False)
    #print ('\n'.join(map(str, agents)))
    #os 2% melhores indivíduos vão para a próxima


    # print ("agents antes de cortar:")
    # for agent in agents:
    #     print (agent.fitness)

    agents = agents[:int(0.2 * len(agents))]

    # print ("agents depois de cortar:")
    # for agent in agents:
    #     print (agent.fitness)

    return agents


def weighted_random_choice(agents):
    max = sum((1/agent.fitness) for agent in agents)
    pick = random.uniform(0, max)
    current = 0
    for agent in agents:
        current += (1/agent.fitness)
        if current > pick:
            return agent


def crossover(agents):

    offspring = []

    for _ in range((population - len(agents)) // 2):

        #ESTÁ PERMITINDO AUTO REPRODUÇÃO - 2 VEZES O MESMO AGENTE

        # parent1 = random.choice(agents)
        # parent2 = random.choice(agents)

        parent1 = weighted_random_choice(agents)
        parent2 = weighted_random_choice(agents)

        # print ("Pai 1:")
        # print (parent1)
        # print ("Pai 2:")
        # print (parent2)




        child1 = Agent(in_str_len)
        child2 = Agent(in_str_len)
        split = random.randint(0, in_str_len)
        #child1.list = parent1.list[0:split] + parent2.list[split:in_str_len]
        #child2.list = parent2.list[0:split] + parent1.list[split:in_str_len]

        child1.list = parent1.list[0:split] + parent2.list[split:]
        child2.list = parent2.list[0:split] + parent1.list[split:]

        # print ("Ponto de corte:")
        # print (split)

        # print ("Filho 1:")
        # print (child1)
        # print ("Filho 2:")
        # print (child2)

        offspring.append(child1)
        offspring.append(child2)

    agents.extend(offspring)

    #print ("Agents antes da mutação:")

    # for agent in agents:
    #     print (agent.fitness)

    agents = mutation(agents)

    #print ("Agents depois da mutação:")

    # for agent in agents:
    #     print (agent.fitness)

    return agents


def mutation(agents):

    for agent in agents:

        for idx, param in enumerate(agent.list):

            #Chance de mutação = 10%
            if random.uniform(0.0, 1.0) <= 0.1:
                #print ("Aconteceu Mutação")
                #a = 1
                #print ("mutação")

                #print (agent.list[idx][0])
                for name, low, high in parameters:
                    #print ("0:")
                    #print (agent.list[idx][0])
                    #print ("name:")
                    #print (name)
                    #print (idx)
                    #print (type(idx))
                    #print("a")
                    #print (type(name))
                    #print("b")
                    #print (type(agent.list[idx][0]))
                    v1 = name
                    v2 = agent.list[idx]

                    #print (v2[0])

                    # if (type(v1) == type(v2)):
                    #     print ("igual")
                    # if(name == agent.list[idx][0]):
                    if(v1 == v2[0]):
                        #list.append([name, random.randint(low, high)])
                        #print ("before mutation")
                        #print(agent.list)
                        # new_gen = [v1, random.randint(low, high)]
                        # prev_gen = agent.list[0:idx]
                        # next_gen = agent.list[idx+1:in_str_len]
                        # agent.list = prev_gen + new_gen + next_gen
                        agent.list[idx] = [v1, random.randint(low, high)]
                        #print ("after mutation")
                        #print(agent.list)
                        break




                #print(agent.list[idx][0])
                #list.append([name, random.randint(low, high)])
                #agent.list = agent.list[0:idx] + random.choice(string.ascii_letters) + agent.list[idx+1:in_str_len]

    return agents


def init_agents(population, length):

    list_pop = []

    special_agent = Agent(length)

    special_agent.list = []

    special_agent.list.append(["initial-number-sheep", 171])
    special_agent.list.append(["initial-number-wolves", 156])

    special_agent.list.append(["grass-regrowth-time", 14])

    special_agent.list.append(["sheep-gain-from-food", 10])
    special_agent.list.append(["wolf-gain-from-food", 6])

    special_agent.list.append(["sheep-reproduce", 8])
    special_agent.list.append(["wolf-reproduce", 2])

    list_pop.append(special_agent)

    for x in range(population - 1):
        new_agent = Agent(length)
        list_pop.append(special_agent)

    return list_pop

    # return [Agent(length) for _ in range(population)]




    # agents = []

    # agent_id = 0

    # for x in range(population):
    #     new_agent = Agent(length, agent_id)
    #     agent_id += 1
    #     agents.append(new_agent)


    # return agents

def fitness(agents):

    for agent in agents:

        if agent.fitness == 99999:

            avg = 0

            for x in range(1):

                ##AQUI VAI CRIAR O ARQUIVO, CHAMAR A FUNÇÃO, LER O RETORNO. ESSE VAI SER O FITNESS
                #TALVEZ AQUI VER SE TODOS OS PARÂMETROS SÃO ACEITOS. SE NÃO, RETORNAR FITNESS SEM SIMULAR
                
                #agent.fitness = fuzz.ratio(agent.list, in_str)

                generate_input_file(agent.list)
                #print ("-")
                execute_model()
                os.remove("/teste/config.txt")
                #print ("-")

                filename = "/teste/export-ticks.txt"

                remove_space(filename)
                f = open(filename, "r")

                #agent.fitness = (int(f.read()))

                avg = avg + (float(f.read()))
                #print("fitness: ")
                #print((f.read()))

                # print ("\n")
                # print(agent)
                
                #agent.fitness = random.randint(0, 89)

            avg = avg / 1

            agent.fitness = avg

        print ("\n")
        print(agent)

    agents = sorted(agents, key=lambda agent: agent.fitness, reverse=False)
    return agents


def selection(agents):

    agents = sorted(agents, key=lambda agent: agent.fitness, reverse=False)
    #print ('\n'.join(map(str, agents)))
    #os 2% melhores indivíduos vão para a próxima


    # print ("agents antes de cortar:")
    # for agent in agents:
    #     print (agent.fitness)

    agents = agents[:int(0.2 * len(agents))]

    # print ("agents depois de cortar:")
    # for agent in agents:
    #     print (agent.fitness)

    return agents


def weighted_random_choice(agents):
    max = sum((1/agent.fitness) for agent in agents)
    pick = random.uniform(0, max)
    current = 0
    for agent in agents:
        current += (1/agent.fitness)
        if current > pick:
            return agent


def crossover(agents):

    offspring = []

    for _ in range((population - len(agents)) // 2):

        #ESTÁ PERMITINDO AUTO REPRODUÇÃO - 2 VEZES O MESMO AGENTE

        # parent1 = random.choice(agents)
        # parent2 = random.choice(agents)

        parent1 = weighted_random_choice(agents)
        parent2 = weighted_random_choice(agents)

        # print ("Pai 1:")
        # print (parent1)
        # print ("Pai 2:")
        # print (parent2)




        child1 = Agent(in_str_len)
        child2 = Agent(in_str_len)
        split = random.randint(0, in_str_len)
        #child1.list = parent1.list[0:split] + parent2.list[split:in_str_len]
        #child2.list = parent2.list[0:split] + parent1.list[split:in_str_len]

        child1.list = parent1.list[0:split] + parent2.list[split:]
        child2.list = parent2.list[0:split] + parent1.list[split:]

        # print ("Ponto de corte:")
        # print (split)

        # print ("Filho 1:")
        # print (child1)
        # print ("Filho 2:")
        # print (child2)

        offspring.append(child1)
        offspring.append(child2)

    agents.extend(offspring)

    #print ("Agents antes da mutação:")

    # for agent in agents:
    #     print (agent.fitness)

    agents = mutation(agents)

    #print ("Agents depois da mutação:")

    # for agent in agents:
    #     print (agent.fitness)

    return agents


def mutation(agents):

    for agent in agents:

        for idx, param in enumerate(agent.list):

            #Chance de mutação = 10%
            if random.uniform(0.0, 1.0) <= 0.1:
                #print ("Aconteceu Mutação")
                #a = 1
                #print ("mutação")

                #print (agent.list[idx][0])
                for name, low, high in parameters:
                    #print ("0:")
                    #print (agent.list[idx][0])
                    #print ("name:")
                    #print (name)
                    #print (idx)
                    #print (type(idx))
                    #print("a")
                    #print (type(name))
                    #print("b")
                    #print (type(agent.list[idx][0]))
                    v1 = name
                    v2 = agent.list[idx]

                    #print (v2[0])

                    # if (type(v1) == type(v2)):
                    #     print ("igual")
                    # if(name == agent.list[idx][0]):
                    if(v1 == v2[0]):
                        #list.append([name, random.randint(low, high)])
                        #print ("before mutation")
                        #print(agent.list)
                        # new_gen = [v1, random.randint(low, high)]
                        # prev_gen = agent.list[0:idx]
                        # next_gen = agent.list[idx+1:in_str_len]
                        # agent.list = prev_gen + new_gen + next_gen
                        agent.list[idx] = [v1, random.randint(low, high)]
                        #print ("after mutation")
                        #print(agent.list)
                        break




                #print(agent.list[idx][0])
                #list.append([name, random.randint(low, high)])
                #agent.list = agent.list[0:idx] + random.choice(string.ascii_letters) + agent.list[idx+1:in_str_len]

    return agents


if __name__ == '__main__':

    #in_str = 'TroySquillaci'
    # in_str = 'UmaFraseGrande'
    # in_str_len = len(in_str)
    # ga()

    #teste = Agent(18)
    #print (teste)

    #in_str_len = len(parameters)

    # generate_input_file(parameters)
    # execute_model()

    # filename = "C:/Users/Gustavo/Desktop/export-ticks.txt"

    # remove_space(filename)
    # print("Resultados:")
    # f = open(filename, "r")
    # print(int(f.read()))
    # print("Fim")


    #in_str = None


    parameters = []

    parameters.append(["initial-number-sheep", 1, 250])
    parameters.append(["initial-number-wolves", 1, 250])

    parameters.append(["grass-regrowth-time", 1, 100])

    parameters.append(["sheep-gain-from-food", 1, 50])
    parameters.append(["wolf-gain-from-food", 1, 100])

    parameters.append(["sheep-reproduce", 1, 20])
    parameters.append(["wolf-reproduce", 1, 20])


    # parameters.append(["min-temp-summer", 17, 17])
    # parameters.append(["max-temp-summer", 28, 28])

    # parameters.append(["min-temp-fall", 12, 12])
    # parameters.append(["max-temp-fall", 23, 23])

    # parameters.append(["min-temp-winter", 9, 9])    
    # parameters.append(["max-temp-winter", 19, 19])

    # parameters.append(["min-temp-spring", 13, 13])
    # parameters.append(["max-temp-spring", 23, 23])

    # parameters.append(["min-temp-summer", 0, 100])
    # parameters.append(["max-temp-summer", 0, 100])

    # parameters.append(["min-temp-fall", 0, 100])
    # parameters.append(["max-temp-fall", 0, 100])

    # parameters.append(["min-temp-winter", 0, 100])    
    # parameters.append(["max-temp-winter", 0, 100])

    # parameters.append(["min-temp-spring", 0, 100])
    # parameters.append(["max-temp-spring", 0, 100])

    in_str_len = len(parameters)
    # population = 20
    # generations = 1000

    population = 5
    generations = 2


    best = ga()

    print ("********************")
    print ("End of Simulation!")
    print ("********************")
    print("Best of All Agents: ")
    print(best)


    # ------------PARTE DO SOCKET------------------------
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    m = {"id": 1, "action": best.fitness} # a real dict.
    # m = {"id": str(randrange(10)), "action": best.fitness} # a real dict.
    command = json.dumps(m)

    print ("Enviando para o servidor:"+command)
    sock.connect(('talker', 9999))
    sock.sendall(command.encode())