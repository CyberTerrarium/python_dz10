import random
import pandas as pd


lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})


# вариант_1
data["human"] = [1 if elem == "human" else 0 for elem in lst]
data["robot"] = [1 if elem == "robot" else 0 for elem in lst]

# если столбец "whoAmI" не нужен совсем:
# data = pd.DataFrame({"human": [1 if elem == "human" else 0 for elem in lst],
#                      "robot": [1 if elem == "robot" else 0 for elem in lst]})


#вариант_2
# data.loc[data["whoAmI"] == "human", "human"] = 1
# data.loc[data["whoAmI"] == "robot", "robot"] = 1
# data.loc[data["whoAmI"] == "human", "robot"] = 0
# data.loc[data["whoAmI"] == "robot", "human"] = 0
# data["human"] = data["human"].astype(int)
# data["robot"] = data["robot"].astype(int)

# # если столбец "whoAmI" не нужен совсем:
# data.pop("whoAmI")


print(data)