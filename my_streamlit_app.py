import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

###############

st.title('Bonjour Wilder, bienvenue dans mon application!')

###############

st.write('voici le dataframe :')
link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv"
cars_df = pd.read_csv(link)

cars_df
###############

st.write('une analyse de corrélation et de distribution grâce à différents graphiques et des commentaires :')
###############

viz_correlation = sns.heatmap(cars_df.corr(), 
								center=0,
								cmap = sns.color_palette("vlag", as_cmap=True)
								)

st.pyplot(viz_correlation.figure)
st.write('Grace a cette heatmap, nous pouvons constater une forte coorelation entre le poid, la puissance, les pouces cube, et les cylindres.')
###############


continent_filter = st.selectbox('Sélectionner un continent', cars_df['continent'].unique())


filtered_df = cars_df[cars_df['continent'] == continent_filter]


fig, ax = plt.subplots(figsize=(13, 5))
sns.scatterplot(data=filtered_df, x="hp", y="mpg", hue='continent', palette="bright", ax=ax)

plt.suptitle("Consommation du carburant selon la puissance en chevaux par continent :")
plt.xlabel("Puissance en chevaux")
plt.ylabel("Consommation du carburant")


st.pyplot(fig)


###############

fig, ax = plt.subplots(figsize = (13,5))
plt.subplot()
ax1 = sns.scatterplot(data=cars_df, x="hp", y="mpg", hue='continent', palette=("bright"))


plt.suptitle("Consommation du carburant selon la puissance en chevaux (all) :")
plt.xlabel("Puissance en chevaux")
plt.ylabel("Consommation du carburant")

st.pyplot(ax1.figure)
st.write('Grâce à ces deux scatters plots, nous pouvons constater que plus une voiture a de la puissances chevaux, moins elle consomme. Nous pouvons également constater que les voitures U.S ont plus de voiture avec une puissance chevaux élevés, là où l\'Europe et le Japon ne vont pas au-delà de 130 puissances chevaux. ')
###############

#viz_pairplot = sns.pairplot(cars_df, hue="continent")
#st.pyplot(viz_pairplot.figure)

###############


viz_displot = sns.displot(data=cars_df, x="hp", hue="continent", multiple = 'stack')
plt.title("Nombre de voitures par puissance :")
st.pyplot(viz_displot.figure)
st.write('Grâce à ce graphique ci-dessus, nous constatons qu\'il y a plus de voiture ayant une puissance moteur proche de 100 et de 150.' )

###############

years = list(pd.unique(cars_df['year']))

hist_car_year = plt.figure(figsize=(10, 4))
sns.histplot(cars_df, x = 'year', hue = 'continent', binwidth= 1, multiple = 'stack')
plt.xticks(years)
plt.title("Nombre de voitures par an :")
st.pyplot(hist_car_year)
st.write('Grâce à cet histplot, nous constatons que les U.S sont ceux qui sortent le plus de voiture.')