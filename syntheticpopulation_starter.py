'''
This file provides example code for taking the files created through the synthetic population
jupyter notebooks and using them to see an Agent Based Model

This file assumes the users has run through the below data pipelines:

1. Population_Data_Download
2. Density Exploration and Conversion
3. Demographic Exploration and Conversion

These files created two files necessary for the below code:
 -- ./data/demographics.h5
 -- ./data/demo_ref.json

'''


import random
from mesa import Agent, Model
from mesa.time import RandomActivation
import pandas as pd
import json
import pickle
import os


def get_base_population(self, col, sched, n_agents, data_store):
    '''
    :param self: obj: an instance of the model class
    :param col: pandas DataFrame: first column from .h5 file
    :param sched: object: an instance of the model schedule
    :param n_agents: int: number of agents counter
    :param data_store: .h5 file: consisting of pandas dataframes called vi data_store.groups()
    :return: int: Number of agents so update self.num_agent
    '''

    col_split = col.split("_")
    gender = col_split[0]
    age = col_split[1]

    pop1 = data_store[col]
    #print(pop1.index)
    for idx, row in pop1.iterrows():
        for num  in range(int(row[col])):
            a = SynPop_Agent(n_agents,self, gender, age, row["latitude"], row["longitude"])
            sched.add(a)
            n_agents += 1

    print("Population now {} agents.".format(n_agents))

    return n_agents

def get_population(self, col, base, sched, n_agents, data_store):

    '''
    :param self: obj: an instance of the model class
    :param col: pandas DataFrame: first column from .h5 file
    :param base: Pandas DataFrame: first frame in demo_ref.json contains latitude and longitude coordinates
    :param sched: object: an instance of the model schedule
    :param n_agents: int: number of agents counter
    :param data_store: .h5 file: consisting of pandas dataframes called vi data_store.groups()
    :return: int: Number of agents so update self.num_agent
    '''


    print("Creating " + col)
    col_split = col.split("_")
    gender = col_split[0]
    age = col_split[1]

    pop = data_store[col]
    ref = data_store[base]
    #print(pop.index)
    for idx, row in pop.iterrows():
        lat = ref.loc[idx, "latitude"]
        long = ref.loc[idx,"longitude"]
        for num in range(int(row[col])):
            a = SynPop_Agent(n_agents,self, gender, age, lat, long)
            sched.add(a)
            n_agents += 1

    print("Population now {} agents.".format(n_agents))
    return n_agents



class SynPop(Model):
    '''
    A generic model instantiation
    '''
    def __init__(self):
        data_store = pd.HDFStore("./data/demographics.h5")
        self.num_agents = 0
        self.running = True
        self.schedule = RandomActivation(self)

        #read in reference
        f = open("./data/demo_ref.json")
        col = json.load(f)
        columns = col["columns"]
        f.close()

        self.num_agents = get_base_population(self, columns[0], self.schedule, self.num_agents, data_store)

        for col in columns[1:]:
            self.num_agents = get_population(self, col, columns[0], self.schedule, self.num_agents, data_store)

        data_store.close()

class SynPop_Agent(Agent):
    '''
    A generic agent class
    '''

    def __init__(self, unique_id, model, gender, age, lat,long):
        super().__init__(unique_id, model)
        self.gender = gender
        self.age = age
        self.lat = lat
        self.long = long


#Create a model instance
model = SynPop()
#Verify agents
print(model.schedule.get_agent_count())
print(model.schedule._agents[2346].lat)

#To delete .h5 files if desired
#os.remove("./data/demographics.h5")
#os.remove("./data/density.h5")
