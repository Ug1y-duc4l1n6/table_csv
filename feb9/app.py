import sqlite3
import pandas as pd

conn = sqlite3.connect('../baseball.db')
cursor = conn.cursor()
query = """
    SELECT teamID, sum(HR) as seasonHR
    FROM batting
    WHERE yearID = 2025
    GROUP BY teamID
    HAVING seasonHR >= 200
"""
cursor.execute(query)
results = cursor.fetchall()
conn.close()
results_df = pd.DataFrame(results, columns=['teams','homeruns'])
print(results_df)




'''query = """
    SELECT yearID, sum(HR)
    FROM batting
    WHERE teamID = 'PHI'
    GROUP BY yearID
    ORDER BY sum(HR) desc
    LIMIT 10
"""
"""
    SELECT playerID
    FROM batting
    WHERE playerID LIKE 'ch%'
    GROUP BY playerID
"""

'''