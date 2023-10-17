from sample_madlibs import hp, code, zombie, hungergames
import madlibs
import random

if __name__ == '__main__':
    m = random.choice([hp, code, zombie, hungergames, madlibs])
    m.madlib()