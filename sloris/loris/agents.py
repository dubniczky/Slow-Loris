import random
import os

# Read agents
user_agents = None
file_name = os.path.join(os.path.dirname(__file__), 'user-agents.txt')
with open(file_name, 'r') as f:
    user_agents = f.read().splitlines()

# Select random agent
def random_agent():
    return random.choice(user_agents)

if __name__ == '__main__':
    print(user_agents[0])
    print(user_agents[-1])