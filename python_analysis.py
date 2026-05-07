import pymysql
import pandas as pd
import matplotlib.pyplot as plt
print("Connecting...")
conn = pymysql.connect(
    host="127.0.0.1",
    user="root",
    password="han tan jani na",
    database="uber_project",
    port=3306
)
print("Connected!")
#LOAD DATA FROM MYSQL
query = "SELECT * FROM trips"
df = pd.read_sql(query, conn)
# Convert Pickup_Time to datetime
df["Pickup_Time"] = pd.to_datetime(df["Pickup_Time"])
df["Hour"] = df["Pickup_Time"].dt.hour
df["Fare"]=pd.to_numeric(df["Fare"])
# Count trips per hour(PEAK HOUR)
hourly_trips = df["Hour"].value_counts().sort_index()
print(hourly_trips)
print(df.head())
#REVENUE PER HOUR
revenue_per_hour = df.groupby("Hour")["Fare"].sum()
print(revenue_per_hour)
#AVG FARE
avg_fare = df["Fare"].mean()
print("Average Fare:", round(avg_fare, 2))
#BUSY AREA
top_area = df["Pickup_Area"].value_counts().idxmax()
print("Most Busy Pickup Area:", top_area)
#PIE CHART FOR PAYMENT_TYPE
payment_counts=df["Payment_Type"].value_counts()
plt.figure()
payment_counts.plot(kind="pie", autopct="%1.1f%%")
plt.title("Payment Method Distribution")
plt.ylabel("")
plt.show()
#BAR CHART Revenue by Area
area_revenue = df.groupby("Pickup_Area")["Fare"].sum().sort_values(ascending=False)
print("\nRevenue by Area:")
print(area_revenue)

plt.figure()
area_revenue.plot(kind="bar")
plt.title("Revenue by Pickup Area")
plt.xlabel("Pickup Area")
plt.ylabel("Total Revenue")
plt.show()
conn.close()