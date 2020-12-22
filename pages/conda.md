title: Using (Mini)Conda for Machine Learning
date: 2020-12-13
category: development


# Abstract
* conda can resolve non-python dependencies, keeping your system clean and spinning up your dev envs quickly, 
whether local or containerized
* is also used behind-the-scenes in major platforms like Microsoft Azure ML  
* also lets you use pip like normal
* this post will walk through setup, describe how to take advantage of the environment.yml, and get a data 
science env complete with jupyter-lab (and matplotlib widget!) support

# Initial Setup
* wget script
* chmod & run
* restart terminal 

# First Environment
* focus on env.yml, reference conda "managing envs" page
* discuss name, channels, dependencies
* show how pip can be used
* include nodejs


``` python
# some test python
import argparse

def blah(max_value):
  return [i**2 for i in range(max_value)]

def parse_args():
  parser = argparse.ArgumentParser()
  parser.add_argument('--max', type=int, default=100, help="Max value to calculate")
  return parser.parse_args()

if __name__ == '__main__':
  # what a complex snippet
  args = parse_args()
  print(blah(args.max))
```



