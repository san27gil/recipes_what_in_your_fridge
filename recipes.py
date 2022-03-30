import pandas as pd
from tabulate import tabulate

print('''
\n* Hola! Tengo algunas recetas anotadas en mis circuitos que te pueden gustar. Dime los ingredientes que tienes y yo te ayudo.
\n* 1. Si quieres saber qué ingredientes conozco, escribe 'ingredientes'.
\n* 2. Si tienes tanta hambre que no eres ni capaz de escribir, tranquilo, tan solo dime 'random' y te diré recetas aleatoriamente:
\n* 3. Y si ya sabes que ingredientes tienes, vete diciéndome uno por uno y pulsa dos veces enter cuando finalices.
\n* 4. PD ===> Si quieres volver a empezar la lista de ingredientes que tienes escribe 'clear'.
''')

ingredients_list = []

def recipes():
    df = pd.read_csv('/Users/santi/Documents/PROGRAMACIÓN/Proyectos/Recipes/recetas.csv', index_col=0)
    # Know number of ingredients required
    df['Required'] = df.iloc[:, 1:12].nunique(axis=1)
    new_list = ', '.join(ingredients_list)
    print("* Muy bien, así que tienes:", new_list,"... \n* Déjame pensar ...\n")
    table = df.isin(ingredients_list)
    num_ingr = table.sum(axis=1)
    df = df[num_ingr >= df['Required'].multiply(0.6)]
    df_list = df['Receta'].to_list()
    df_list = ', '.join(df_list)
    print("* Podrías hacer alguna de estas recetas:", df_list, ".\n")
    df = df.drop(['Required'], axis=1)
    df = df.dropna(axis=1, how='all')
    df = df.fillna('-')
    print(tabulate(df, headers='keys', tablefmt='pretty', showindex=False))


def ingredientes():
    df = pd.read_csv('/Users/santi/Documents/PROGRAMACIÓN/Proyectos/Recipes/recetas.csv', index_col=0)
    # Count unique ingredients:
    unique_values = set()
    for col in df.iloc[:, 1:12]:
        unique_values.update(df[col])
    # Remove NaN values:
    unique_values = list(unique_values)
    unique_values = [x for x in unique_values if str(x) != 'nan']
    print("\n",', '.join(unique_values))


def random():
    df = pd.read_csv('/Users/santi/Documents/PROGRAMACIÓN/Proyectos/Recipes/recetas.csv', index_col=0)
    print(tabulate(df.sample().dropna(axis=1, how='all'), 
        headers='keys', tablefmt='pretty', showindex=False))

while True:
    ingredient = input('> ')
    if ingredient == '':
        recipes()
    elif ingredient == 'random':
        random()
    elif ingredient == 'ingredientes':
        ingredientes()
    elif ingredient == 'clear':
        ingredients_list.clear()
    else:
        ingredients_list.append(ingredient)
