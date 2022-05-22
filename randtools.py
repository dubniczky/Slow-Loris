import random
from agents import user_agents

# Create random string
def rand_str(length):
    return ''.join((random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(length)))

# Select random agent
def random_agent():
    return random.choice(user_agents)

if __name__ == '__main__':
    print(rand_str(rand_str(16)))
    print(random_agent())