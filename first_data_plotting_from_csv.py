import matplotlib.pyplot as plt
import pandas as pd

isuTuition = pd.read_csv('ISU_Tuition_10Yrs.csv')

df = pd.DataFrame(isuTuition)

plt.plot(
    df.Academic_Year,
    df.Undergraduate_In_State,
    '--bo',
    label="Undergraduate In-State")
plt.plot(
    df.Academic_Year,
    df.Undergraduate_Out_of_State,
    '--ro',
    label="Undergraduate Out-of-State")

plt.title(
    "ISU Tuition for the Past 10 Years",
    fontdict={
        'fontsize': 15,
        'fontweight': 'bold',
        'color': 'red'})
plt.xlabel("Academic Year", fontdict={
    'fontsize': 10,
    'fontweight': 'bold'})
plt.ylabel("Tuition ($)", fontdict={
    'fontsize': 10,
    'fontweight': 'bold'})

current_values = plt.gca().get_yticks()
plt.gca().set_yticklabels(['{:,.0f}'.format(x) for x in current_values])

plt.legend(loc="upper left")
plt.show()

# Plot gets created but I get the following UserWarning: FixedFormatter should only be used together with
# FixedLocator plt.gca().set_yticklabels(['{:,.0f}'.format(x) for x in
# current_values])
