import pandas as pd

employees = pd.read_csv("employees.csv", index_col=0)

print(employees)