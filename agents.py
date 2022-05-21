import random

# Read agents
user_agents = None
with open('data/user-agents.txt', 'r') as f:
    user_agents = f.read().splitlines()

# Select random agent 
def random_agent():
    return random.choice(user_agents)

if __name__ == '__main__':
    print(user_agents[0])
    print(user_agents[-1])