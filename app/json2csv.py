#!/usr/bin/env python

import pandas as pd
import subprocess

print('Converting JSON files to CSV')

df_people = pd.read_json("./resources/people.json")
df_people.index +=1
df_people.to_csv("./data/people.csv", index=True, index_label="id")

df_project = pd.read_json("./resources/projects.json")
df_project.index +=1
df_project.to_csv("./data/projects.csv", index=True, index_label="id")

subprocess.call(["sed -i 's/[][]//g' ./data/people.csv"], shell=True)
subprocess.call(["sed -i 's/[][]//g' ./data/projects.csv"], shell=True)



