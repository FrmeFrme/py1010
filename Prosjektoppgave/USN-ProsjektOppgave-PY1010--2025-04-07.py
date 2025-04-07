# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 16:21:45 2025

@author: frode meyer
Prosjektoppgave Prosjekt i PY1010
Universitetet i Sørøst-Norge

"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Deloppgave A), Les inn Excel fil med kundehenvendelser. Innlesing er med feilhåndtering
try:
    kundehenvendelser = pd.read_excel('C:\\_py_usn-prosjektoppg\\support_uke_24.xlsx')
except FileNotFoundError:
    print("Feil: Finner ikke filen 'support_uke_24.xlsx'. Sjekk filbanen.")
    exit()
except Exception as e:
    print(f"Feil ved lesing av fil: {e}")
    exit()

# Lagre innlest data i arrays
u_dag = kundehenvendelser.iloc[:, 0].astype(str).str.lower().fillna('')
kl_slett = kundehenvendelser.iloc[:, 1].to_numpy()
varighet = kundehenvendelser.iloc[:, 2].to_numpy()
score = kundehenvendelser.iloc[:, 3].to_numpy()
print(f"\n\nDeloppgave A) utført. Excel fil er lest inn og lagret i array")

# Skriv ut for å sjekke at dataene er lastet inn riktig
# print("\nu_dag:\n", u_dag)
# print("\nkl_slett:\n", kl_slett)
# print("\nvarighet:\n", varighet)
# print("\nscore:\n", score)

# Finn antall henvendelser for hver ukedag
ukedager = ['mandag', 'tirsdag', 'onsdag', 'torsdag', 'fredag']

# print("\nAntall supporthenvendelser per ukedag og vaktbolk i stigende rekkefølge:")
for dag in ukedager:
    # Undersøk hver ukedag lagre resultatet i en liste for plotting
    antall_henvendelser_pr_dag = [np.sum(u_dag == dag) for dag in ukedager]
    # print(f"{dag.capitalize()}: {antall_henvendelser_pr_dag}")



# Deloppgave B) Visualiser antall henvendelser for hver av de 5 ukedagene i søylediagrem /stolpediagram
plt.close('all')

# Plot stolpediagram
plt.figure(figsize=(13, 9))
plt.bar(ukedager, antall_henvendelser_pr_dag, color='skyblue', edgecolor='black')

# Legg til titler og etiketter
plt.xlabel('Ukedager')
plt.ylabel('Antall henvendelser')
plt.title('Supporthenvendelser per ukedag')
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Vis plottet
plt.show()

print(f"\nDeloppgave B) utført. Søylediagram er plottet. Se eget plot-vindu")

def hhmmss_til_sekunder(hhmmss):
    timer, minutter, sekunder = map(int, hhmmss.split(':'))
    return timer * 3600 + minutter * 60 + sekunder

# Deloppgave c) Finn minste og lengste samtaletid fra logg. Print  resultatet til skjerm.
# Konvertere tidene til antall sekunder
# varighet_sekunder_array = np.array([int(t.split(':')[0]) * 3600 + int(t.split(':')[1]) * 60 + int(t.split(':')[2]) for t in varighet])
varighet_sekunder_array = np.array([hhmmss_til_sekunder(t) for t in varighet])


min_varighet_sekunder = np.min(varighet_sekunder_array)
max_varighet_sekunder = np.max(varighet_sekunder_array)

# Konvertere sekunder tilbake til HH:MM:SS format
def sekunder_til_hhmmss(sekunder):
    timer = sekunder // 3600
    minutter = (sekunder % 3600) // 60
    sekunder = sekunder % 60
    return f"{timer:02}:{minutter:02}:{sekunder:02}"

min_tid_str = sekunder_til_hhmmss(min_varighet_sekunder)
max_tid_str = sekunder_til_hhmmss(max_varighet_sekunder)

print(f"\nDeloppgave C) Korteste og lengste samtale i formatet [HH:MM:SS]:")
print(f"Korteste supportsamtale: {min_tid_str}")
print(f"Lengste supportsamtale: {max_tid_str}")


# Deloppgave d) Regn ut gjennomsnittelig samtaletid på alle supportsamtaler i hele sekunder
gjennomsnitt_support_samtale_tid_sekunder = int(np.mean(varighet_sekunder_array))

#Konverter til hhmmss format:
gjennomsnitt_support_samtale_tid_hhmmss = sekunder_til_hhmmss(gjennomsnitt_support_samtale_tid_sekunder)
print(f"\nDeloppgave D) Samtaletid i formatet [HH:MM:SS]:")
print(f"Gjennomsnittelig samtaletid alle samtaler: {gjennomsnitt_support_samtale_tid_hhmmss} ")



# Deloppgave e1) Finn antall henvendelser for hver av vaktene (2 t bolker mellom 8-10, 10-12, 12-14, 14-16
tidsbolker = {
    "08:00-09:59": (8 * 3600, 10 * 3600),
    "10:00-11:59": (10 * 3600, 12 * 3600),
    "12:00-13:59": (12 * 3600, 14 * 3600),
    "14:00-15:59": (14 * 3600, 16 * 3600)
}

antall_henvendelser_tidsbolker = {}

for key, (start, end) in tidsbolker.items():
    # antall_henvendelser_tidsbolker[key] = np.sum((hhmmss_til_sekunder(kl) >= start) & (hhmmss_til_sekunder(kl) < end) for kl in kl_slett)
    antall_henvendelser_tidsbolker[key] = sum((hhmmss_til_sekunder(kl) >= start) & (hhmmss_til_sekunder(kl) < end) for kl in kl_slett)



# Skriv ut antall henvendelser per tidsbolk
print(f"\nDeloppgave E) Antall henvendelser for av vaktlagene visulisert i sektordiagram/kakediagram. Oppsummert her:")
print("Antall henvendelser per tidsbolk:")
for key, count in antall_henvendelser_tidsbolker.items():
    print(f"Tidsbolk {key}: {count} hendvendelser")

# Deloppgave e2) Visualiser dataljene i oppg e1) i kakediagram
plt.figure(figsize=(8, 8))
plt.pie(antall_henvendelser_tidsbolker.values(), labels=antall_henvendelser_tidsbolker.keys(), autopct='%1.1f%%', startangle=90)
plt.title('Fordeling av supporthenvendelser per tidsbolk')
plt.axis('equal')  # For å få en sirkel
plt.show()



# Deloppgave f) Lag og presenter score i NPS system (Net Promoter Score)
# https://www.blueprnt.com/2018/09/17/net-promoter-score/
# Filtrer ut scoreverdier som ikke er NaN
registrerte_score = score[~pd.isna(score)]

# Konverter scoreverdiene til heltall
registrerte_score = registrerte_score.astype(int)

# Skriv ut alle registrerte scoreverdier
# print("\nRegistrerte NPS-scoreverdier:")
# print(registrerte_score.tolist())


# Filtrer ut scoreverdier som ikke er NaN
registrerte_score = score[~pd.isna(score)]

# Konverter scoreverdiene til heltall
registrerte_score = registrerte_score.astype(int)

# Opprett en DataFrame med relevante data
data = pd.DataFrame({
    'Samtale nr': np.arange(1, len(registrerte_score) + 1),  # Nummererer hver samtale
    'Dag': u_dag[~pd.isna(score)].reset_index(drop=True),
    'Tidsbolk': [
        next((key for key, (start, end) in tidsbolker.items() if start <= hhmmss_til_sekunder(kl) < end), 'Ukjent')
        for kl in kl_slett[~pd.isna(score)]
    ],
    'Score': registrerte_score
})

# Skriv ut score per tidsbolk og dag
print(f"\nDeloppgave F) Beregning av supportavdelingens NPS (score):")
print("NPS-score fordelt på vaktbolk og dag:")
print(data)


# Sorter data etter 'score' i synkende rekkefølge, deretter dDag og tidsbolk" i stigende uukedagnr og tidsbolk innen for hver score verdi
# Gjør om 'dag' til en riktig sorteringsrekkefølge med nadg først og fredag til slutt
data['Dag'] = pd.Categorical(data['Dag'], categories=ukedager, ordered=True)
# Sorter først etter 'score' (synkende), deretter 'dag' og 'tidsbolk' (stigende)
sortert_data = data.sort_values(by=['Score', 'Dag', 'Tidsbolk'], ascending=[False, True, True])


# Skriv ut sortert liste over score og tilhørende vaktlag
# print("\nSortert liste over NPS-score og tilhørende vaktlag:")
# print(sortert_data)


# Opprett en DataFrame med relevante data
data = pd.DataFrame({
    'Dag': u_dag[~pd.isna(score)],
    'Tidsbolk': [
        next((key for key, (start, end) in tidsbolker.items() if start <= hhmmss_til_sekunder(kl) < end), 'Ukjent')
        for kl in kl_slett[~pd.isna(score)]
    ],
    'Score': registrerte_score
})


# Beregn NPS
# Beregn antall og summen av negative, nøytrale og positive tilbakemeldinger
antall_negative = np.sum((registrerte_score >= 1) & (registrerte_score <= 6))
antall_noytrale = np.sum((registrerte_score == 7) | (registrerte_score == 8))
antall_positive = np.sum((registrerte_score == 9) | (registrerte_score == 10))

sum_negative = np.sum(registrerte_score[(registrerte_score >= 1) & (registrerte_score <= 6)])
sum_noytrale = np.sum(registrerte_score[(registrerte_score == 7) | (registrerte_score == 8)])
sum_positive = np.sum(registrerte_score[(registrerte_score == 9) | (registrerte_score == 10)])

# Beregn totalantall tilbakemeldinger
total_tilbakemeldinger = len(registrerte_score)

# Beregn prosentandeler
prosent_negative = (antall_negative / total_tilbakemeldinger) * 100
prosent_positive = (antall_positive / total_tilbakemeldinger) * 100

# Beregn NPS
nps = prosent_positive - prosent_negative

# Print resultater
print(f"\nAntall negative tilbakemeldinger (score 1-6): {antall_negative} stk, i prosent: {antall_negative/total_tilbakemeldinger*100:.2f} %")
# print(f"Score sum av negative tilbakemeldinger: {sum_negative}")
print(f"Antall nøytrale tilbakemeldinger (score 7-8): {antall_noytrale} stk, i prosent: {antall_noytrale/total_tilbakemeldinger*100:.2f} %")
# print(f"Score sum av nøytrale tilbakemeldinger: {sum_noytrale}")
print(f"Antall positive tilbakemeldinger (score 9-10): {antall_positive} stk, i prosent: {antall_positive/total_tilbakemeldinger*100:.2f} %")
# print(f"Score sum av positive tilbakemeldinger: {sum_positive}")
print(f"\nTotalt antall besvarelser: {total_tilbakemeldinger}")

# NPS med 2 desimaler print(f"Net Promoter Score (NPS): {nps:.2f}")
print(f"\nDet gir følgende Net Promoter Score (NPS): {nps:.0f}")
