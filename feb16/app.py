import sqlite3
import pandas as pd  
import gradio as gr  

conn = sqlite3.connect('../baseball.db')
cursor = conn.cursor()
query = """
WITH top_hitters AS (SELECT nameFirst, nameLast, batting.playerID
FROM batting INNER JOIN people
ON batting.playerID = people.playerID
WHERE teamID = 'PHI'
GROUP BY batting.playerID
ORDER BY sum(HR) desc
LIMIT 10)

SELECT CONCAT(nameFirst,' ',nameLast) as player, playerID
FROM top_hitters
ORDER BY nameLast
"""
cursor.execute(query)
records = cursor.fetchall()
conn.close()

# print(records)

'''players = []
for record in records:
    players.append(record[0])'''

with gr.Blocks() as iface:
    gr.Dropdown(records, interactive = True)

iface.launch()