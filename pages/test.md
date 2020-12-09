title: How I Learned to Stop Worrying and Embrace My Inner Demons, Oh YEAH
date: 2020-06-12
category: test


# My First Blog

Here is some content for this blog. Written in Markdown.

- Bullet point 1
- Bullet point 2
- Bullet point 3


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



