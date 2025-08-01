import pandas as pd

# Charger le fichier des données moyennes saisonnières
df_saisons = pd.read_csv("data-EAU\moyennes_debit_saisonnieres_1976_2005.csv", sep=",") 

# Charger les métadonnées des stations
df_meta = pd.read_csv("data-EAU/metadonneesHydrostations.csv", 
                      sep=";", 
                      comment="#", 
                      header=None, 
                      names=["Id_station", "code_Hydro", "nom_station", "longitude", "latitude", 
                             "X_Lambert93", "Y_Lambert93", "X_Lambert2e", "Y_Lambert2e"])

# Nettoyage éventuel
df_meta["code_Hydro"] = df_meta["code_Hydro"].str.strip()
df_saisons["CodeHydro"] = df_saisons["CodeHydro"].str.strip()

# Fusion sur le code hydro
df_merged = df_saisons.merge(df_meta, left_on="CodeHydro", right_on="code_Hydro", how="left")

# Sélection et réorganisation des colonnes
df_final = df_merged[[
    "Id_station", "code_Hydro", "nom_station", "longitude", "latitude", 
    "Periode", "Automne", "Hiver", "Printemps", "Été"
]]

# Export du fichier final
df_final.to_csv("sation-debit-saison-historique.csv", index=False, sep=";")
print("✅ Ajout terminé")
