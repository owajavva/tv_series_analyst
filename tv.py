import matplotlib.pyplot as plt
import pandas as pd

plt.rcParams['figure.figsize'] = [11, 7]
# office_df='Filza'
office_df= pd.read_csv('office_episodes.csv')
print(office_df.head())
cols=[]

for ind, row in office_df.iterrows():
    if row['scaled_ratings'] < 0.25:
        cols.append('red')
    elif row['scaled_ratings'] >= 0.25 and row['scaled_ratings'] <0.50:
        cols.append('orange')
    elif row['scaled_ratings'] >= 0.50 and row['scaled_ratings'] <0.75:
        cols.append('lightgreen')
    elif row['ratings'] >= 0.75:
        cols.append('darkgreen')

sizes=[]

for ind,row in office_df.iterrows():
    if row['has_guests']== False:
        sizes.append(25)
    else:
        sizes.append(250)

# print(sizes)
fig= plt.figure()
#
plt.scatter(x=office_df['episode_number'],
            y=office_df['viewership_mil'],
           c=cols, s=sizes)
plt.title('Popularity, Quality, and Guest Appearances on the Office')
plt.xlabel('Episode Number')
plt.ylabel('Viewership (Millions)')
plt.show()

office_df[office_df['viewership_mil']== office_df['viewership_mil'].max()]
top_star = 'Jessica Alba'
print(top_star)
# pd.show_versions()
