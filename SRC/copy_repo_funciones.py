import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

#checar conteo nulos Columnas, Ascending False
def nancols(x):
    nan_cols = x.isna().sum()
    return nan_cols[nan_cols>0].sort_values(ascending=False)

def nancolsper(data):
    nan_cols = data.isna().mean() * 100
    return nan_cols[nan_cols > 0].sort_values(ascending=False).round(2)

#checar conteo nulos filas, Ascending False
def nanrows(x):
    nan_rows = x.isna().sum(axis=1)
    return nan_rows[nan_rows>0].sort_values(ascending=False)

#checar conteo de valores unicos por columnas, ascending false, X es para el DF entero
def unique_cols(x):
    unique_cols = x.nunique()
    return unique_cols.sort_values(ascending=False)


#conteo de valores unicos por columna devuelto como DF para mejor visu
def col_unique_counts(df, col):
    counts = df[col].value_counts().reset_index()
    counts.columns = [col, 'Count']
    return counts

#conteo de valores unicos por columna devuelto en barplot

def plot_value_counts(df, column):
    # Count the unique values in the specified column
    value_counts = df[column].value_counts()

    # Create a bar plot
    plt.figure(figsize=(10, 6))
    value_counts.plot(kind='bar')
    plt.xlabel(column)
    plt.ylabel('Count')
    plt.title(f'Count of Unique Values in {column} Column')
    plt.xticks(rotation=45)
    plt.show()


# grafico de nulos en un DF 

import matplotlib.pyplot as plt
import seaborn as sns

def plot_missing_values(data):
    plt.figure(figsize=(10, 6))
    sns.heatmap(data.isna(), yticklabels=False, cmap='viridis', cbar=False)
    plt.show()


#checar dtypes unicos por columna
def get_unique_dtypes(df, col):
    unique_dtypes = df[col].apply(lambda x: type(x)).unique()
    return unique_dtypes

# de una cata...busca cual es el valor unico en un array (da por hecho existe, no tiene mucha utilidad)

a= ([ 1, 1, 1, 2, 1, 1 ])

def findUnique(x):
    res=[]
    for num in x:
        if x.count(num) == 1:
            res.append(num)
            return res

#esta checalasgg

def time_of_day(hour): # funcion para agrupar y asi reducir la cantidad de horas del dia en periodos preestablecidos

    if '07' in hour or '08' in hour or '09' in hour or '10' in hour or '11' in hour or '12' in hour:
        return 'Morning'
    elif '13' in hour or '14' in hour or '15' in hour or '16' in hour or '17' in hour or '18' in hour or '19' in hour or '20' in hour or '21' in hour:
        return 'Afternoon'
    elif '22' in hour or '23' in hour or '00' in hour or '01' in hour or '02' in hour or '03' in hour or '04' in hour or '05' in hour or '06' in hour:
        return 'Night'
    else:
        return 'No information'
#data["Time_groups"] = data['Time'].apply(time_of_day)

def age_groups(age):
    if age == 0:
        return 'No information'
    elif age <= 12:
        return 'kid'
    elif age <= 19:
        return 'teen'
    elif age <= 60:
        return 'adult'
    elif age >= 60:
        return 'elderly'
    else:
        return 'No information'

#data['age'] = data['age'].apply(age_of_victims)


def map_to_alcaldia_id(df, col_name):
    alcaldia_dict = {
        'Azcapotzalco': '002',
        'Coyoacán': '003',
        'Cuajimalpa de Morelos': '004',
        'Gustavo A. Madero': '005',
        'Iztacalco': '006',
        'Iztapalapa': '007',
        'La Magdalena Contreras': '008',
        'Milpa Alta': '009',
        'Álvaro Obregón': '010',
        'Tláhuac': '011',
        'Tlalpan': '012',
        'Xochimilco': '013',
        'Benito Juárez': '014',
        'Cuauhtémoc': '015',
        'Miguel Hidalgo': '016',
        'Venustiano Carranza': '017'
    }
    
    df['alcaldia_id'] = df[col_name].map(alcaldia_dict)
    
    return df.head()

#heatmap de correlaciones. Para columnas no numericas. Hay que importar numpy as np, Pylab as plt y seaborn as sns

def plot_correlation_heatmap(df):
    numeric_columns = df.select_dtypes(include=np.number)
    
    plt.figure(figsize=(15, 10))
    sns.set(style='white')
    
    mask = np.triu(np.ones_like(numeric_columns.corr(), dtype=bool))
    cmap = sns.diverging_palette(0, 10, as_cmap=True)
    
    sns.heatmap(numeric_columns.corr(),
                mask=mask,
                cmap=cmap,
                center=0,
                square=True,
                annot=True,
                linewidths=0.5,
                cbar_kws={'shrink': 0.5})
    
    plt.show()


#REMPLAZAR NULOS POR LA MODA. 

def replace_null_with_mode(df):
    # Iterate over each column in the DataFrame
    for column in df.columns:
        # Check if the column contains any null values
        if df[column].isnull().any():
            # Replace null values with the mode of the column
            mode_value = df[column].mode()[0]
            df[column].fillna(mode_value, inplace=True)
    
    return df




