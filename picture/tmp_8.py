from research.research import Research
import pandas as pd

data = pd.read_csv("./input/sz_result.csv")

r = Research(data)
r.test()