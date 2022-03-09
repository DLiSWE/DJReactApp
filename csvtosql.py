import pandas as pd
import psycopg2
from sqlalchemy import create_engine

# DATA
ingredient_id_list = []
ingredient_name_list = []
# get spoonify ingredient csv, clean
ingredient_df = pd.read_csv('day15\ingredients.csv')
ingredient_len = len(ingredient_df)
# rename ingredient column and add initial column name to column
for column in ingredient_df:
    ingredient_df.loc[ingredient_len] = column
    ingredient_df.rename(columns={column:'Ingredient Name'}, inplace=True)

for ingredient in ingredient_df['Ingredient Name']:
    ingredient = ingredient.title()
    ingredient_id_list.append(ingredient.split(';')[1])
    ingredient_name_list.append(ingredient.split(';')[0])

ingredient_df['id'] = ingredient_id_list
ingredient_df['Ingredient Name'] = ingredient_name_list

print(ingredient_df)

# UPLOAD TO POSTGRES
# psycopg2
# conn = psycopg2.connect(
#                     host='127.0.0.1',
#                     user='postgres',
#                     password='1123',
#                     dbname='Proj4')
# SQLAlchemy
engine = create_engine('postgresql://postgres:1123@127.0.0.1:5432/Proj4')

ingredient_df.to_sql('Ingredients', engine,if_exists='append', index=False)
