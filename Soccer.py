#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 21 17:51:40 2021

@author: sandeepdiddi
"""


#Import Libraries for loading data from SQLITE 

import pandas as pd
import sqlite3



#Declare the connection string

#For class purpose i am declaring the exported DB from ER Diagram , however 
#Prefered way is through JDBC route 
conn = sqlite3.connect('/Users/sandeepdiddi/Documents/Soccer_DB/database.sqlite')
cur = con.cursor()


#Verify the connection by running a Query against the SQLITE DB 
for row in cur.execute("select * from Country c "):
    print(row)
    


#Fetch Coutries Table from SQL Lite to Data Frame with Pandas     
countries = pd.read_sql("""SELECT *
                        FROM Country;""", conn)
countries



#Listing the leagues of the coutries in the Soccer 
#For this I wil be joining Country and League tables and fetch the results 


leagues = pd.read_sql("""SELECT *
                        FROM League
                        JOIN Country ON Country.id = League.country_id;""", 
                        conn)


print(leagues)

#https://www.kaggle.com/mmcgovern/esd-data-analysis-using-sql -- P1 

#https://www.kaggle.com/hugomathien/soccer/activity

#https://www.kaggle.com/dimarudov/data-analysis-using-sql -- P2

#https://www.kaggle.com/mmcgovern/exploring-the-european-soccer-database-with-sql --P3







per = pd.read_sql("""SELECT 
c.name AS country,
ROUND(AVG(CASE WHEN m.season='2013/2014' AND m.home_team_goal = m.away_team_goal THEN 1
 WHEN m.season='2013/2014' AND m.home_team_goal != m.away_team_goal THEN 0
END),2) AS pct_ties_2013_2014,
ROUND(AVG(CASE WHEN m.season='2014/2015' AND m.home_team_goal = m.away_team_goal THEN 1
 WHEN m.season='2014/2015' AND m.home_team_goal != m.away_team_goal THEN 0
END),2) AS pct_ties_2014_2015
FROM country AS c
LEFT JOIN match AS m
ON c.id = m.country_id
GROUP BY country
;""", conn)

per