# %%
import sqlite3
import pandas as pd

# %%
# create a connection to a database
db = sqlite3.connect("vegetables.db")

# %%
# create a cursor
cur = db.cursor()

# %%
step1 = cur.execute(
    "CREATE TABLE IF NOT EXISTS vegetables (name TEXT, color TEXT, count INTEGER)"
)
step1.fetchall()

# %%
cur.execute('INSERT INTO vegetables VALUES ("carrot", "orange", 10)')

# %%
step3 = cur.execute("SELECT * FROM vegetables")
step3.fetchall()

# %%
cur.execute('UPDATE vegetables SET count = 20 WHERE name = "carrot"')

# %%
cur.execute('INSERT INTO vegetables VALUES ("broccoli", "green", 15)')
cur.execute('INSERT INTO vegetables VALUES ("cauliflower", "white", 31)')
cur.execute('INSERT INTO vegetables VALUES ("zucchini", "green", 27)')
cur.execute('INSERT INTO vegetables VALUES ("spinach", "green", 4)')
cur.execute('INSERT INTO vegetables VALUES ("squash", "yellow", 4)')
cur.execute('INSERT INTO vegetables VALUES ("peas", "green", 3)')
cur.execute('INSERT INTO vegetables VALUES ("potato", "brown", 8)')
cur.execute('INSERT INTO vegetables VALUES ("tomato", "red", 9)')
cur.execute('INSERT INTO vegetables VALUES ("eggplant", "purple", 6)')
cur.execute('INSERT INTO vegetables VALUES ("cucumber", "green", 11)')
cur.execute('INSERT INTO vegetables VALUES ("celery", "green", 12)')
cur.execute('INSERT INTO vegetables VALUES ("asparagus", "green", 13)')
cur.execute('INSERT INTO vegetables VALUES ("garlic", "white", 14)')

# %%
step5 = cur.execute("SELECT * FROM vegetables")
step5.fetchall()

# %%
db.commit()

# %%
db.close()

# %% [markdown]
# ## Section 2 Week 9
# ### I have selected a dataset from Kaggle: https://www.kaggle.com/datasets/shariful07/nice-work-thanks-for-share

# %%
# Connect to DB and create a cursor
sqliteConnection = sqlite3.connect("student.db")
cursor = sqliteConnection.cursor()

# %%
# create database/table

db = pd.read_csv("University Students Monthly Expenses.csv")
db.to_sql("student", sqliteConnection, if_exists="append", index=False)

# %%
db.head()

# %%
max_spend = db.sort_values(by="Monthly_expenses_$", ascending=False)[
    "Monthly_expenses_$"
].iloc[0]
print(f"The maximum monthly spend is ${max_spend}.")

# %%
cursor.execute("select * from student")

# %%
# this will show the first row in the data
cursor.fetchone()

# %%
# show the columns in the database
print(db.columns)

# %%
# select the student with monthly expenses greater than 200
cursor.execute("select * from student where Monthly_expenses_$ > 200")
rich = cursor.fetchall()
[i for i in rich][0]
print(f"There are {len(rich)} students with monthly expenses greater than $200.")

# %%
# select the student with monthly expenses less than 100
cursor.execute(
    "select Scholarship,Part_time_job from student where Monthly_expenses_$ < 150"
)
spd_less = cursor.fetchall()
[i for i in spd_less][0]
print(f"There are {len(spd_less)} students with monthly expenses less than $150.")

# %%
print(spd_less)

# %% [markdown]
# # Last part of Project 3 (11/6)

# %% [markdown]
# ## I want to include a few questions here to answer
#
# 1. find the mean Monthly Expenses of the female and male to see if there's any difference
#
# 2. Check if `Smoking` will increase the Monthly Expenses
#
# 3. Check if `Games_&_Hobbies` will increase the Monthly Expenses
#
# 4. Compare if `Cosmetics_&_Self-care` is a factor
#
# 5. Check if the `Study_year` will affect the  Monthly Expenses

# %%
db.head()

# %%
cursor.execute("select AVG(Monthly_expenses_$),Gender from student GROUP BY Gender")
gender = cursor.fetchall()
[i for i in gender]

# %% [markdown]
# Based on the mean value that I calculated from above, it seems like the males are spending more than the females.

# %%
cursor.execute(
    "select Smoking,Monthly_expenses_$ from student GROUP BY Smoking,Monthly_expenses_$ Having Smoking = 'Yes' or Smoking = 'No' Order By Monthly_expenses_$ DESC"
)
smoke = cursor.fetchall()
[i for i in smoke]

# %% [markdown]
# Smoking or not smoking will not help to determine whether the student spend a lot or very little in a month. It doesn't seem to be a factor.

# %%
db.columns

# %%
cursor.execute(
    "select AVG(Monthly_expenses_$),student.'Games_&_Hobbies' from student GROUP BY student.'Games_&_Hobbies'"
)
games = cursor.fetchall()
[i for i in games]

# %% [markdown]
# The result surprises me, the students who do not play games and have hobbies tend to spend more on average.

# %%
cursor.execute(
    "select AVG(Monthly_expenses_$),student.'Cosmetics_&_Self-care' from student GROUP BY student.'Cosmetics_&_Self-care' Having student.'Cosmetics_&_Self-care' == 'Yes' or student.'Cosmetics_&_Self-care' == 'No'"
)
cos = cursor.fetchall()
[i for i in cos]

# %% [markdown]
# In this case, the students that do have self-care spends more than the students who don't.

# %%
cursor.execute(
    "select AVG(Monthly_expenses_$),student.'Study_year' from student GROUP BY student.'Study_year'"
)
yr = cursor.fetchall()
[i for i in yr]

# %% [markdown]
# According to the output, it seems like the students who are older tend to spend more money.
