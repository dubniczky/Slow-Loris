import random

# Read agents
user_agents = None
with open('data/user-agents.txt', 'o') as f:
    user_agents = f.readlines()

# Select random agent 
def random_agent():
    return random.choice(user_agents)
