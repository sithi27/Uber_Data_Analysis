<div align="center">

# 🚗 Uber Dhaka — Ride Analytics Project

[![Trips](https://img.shields.io/badge/Total_Trips-200-0d1117?style=for-the-badge&labelColor=0d1117&color=238636)](/)
[![Revenue](https://img.shields.io/badge/Total_Revenue-৳87%2C275-0d1117?style=for-the-badge&labelColor=0d1117&color=1f6feb)](/)
[![Zones](https://img.shields.io/badge/Pickup_Zones-7-0d1117?style=for-the-badge&labelColor=0d1117&color=8957e5)](/)
[![Period](https://img.shields.io/badge/Period-2025_Full_Year-0d1117?style=for-the-badge&labelColor=0d1117&color=da3633)](/)

<br/>

> A complete end-to-end data analysis project on Uber ride data from Dhaka, Bangladesh —
> covering **SQL querying**, **Python analysis**, and an interactive **Power BI dashboard**.

</div>

---

<div align="center">

### Tech Stack

![MySQL](https://img.shields.io/badge/MySQL-00758F?style=for-the-badge&logo=mysql&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557c?style=for-the-badge&logo=python&logoColor=white)
![Power BI](https://img.shields.io/badge/Power%20BI-F2C811?style=for-the-badge&logo=powerbi&logoColor=black)
![Excel](https://img.shields.io/badge/Excel-217346?style=for-the-badge&logo=microsoft-excel&logoColor=white)

</div>

---

## About

> This project analyzes **200 Uber trips** across **7 pickup zones in Dhaka** to uncover patterns in revenue, demand, driver performance, and payment behavior. Built as a final-year academic project covering the full data pipeline — from raw CSV → MySQL → Python → Power BI.

| 🏙️ City | 🗓️ Period | 🚗 Total Trips | 💰 Total Revenue | 💳 Payment Types |
|---------|----------|--------------|----------------|----------------|
| Dhaka, BD | Jan – Dec 2025 | 200 | ৳87,275 | Card · bKash · Cash |

---

## Project Structure

```
📦 uber-dhaka-analysis
 ┣ 📄 ubar_project_excel_file.csv     ← Raw dataset
 ┣ 🗃️ uber_project_queries.sql        ← SQL queries for data exploration
 ┣ 🐍 python_analysis.py              ← Python analysis & visualizations
 ┗ 📊 uber_dashboard_final.pbix       ← Power BI interactive dashboard
```

---

## SQL Analysis — `uber_project_queries.sql`

Key queries written in **MySQL** to explore the dataset:

```sql
-- Total trips and revenue
SELECT COUNT(*) AS Total_Trips FROM trips;
SELECT SUM(Fare) AS Total_Revenue FROM trips;

-- Peak hour with most trips
SELECT Hour_of_Day, COUNT(*) AS Trips
FROM trips
GROUP BY Hour_of_Day
ORDER BY Trips DESC LIMIT 1;

-- Top revenue-generating area
SELECT Pickup_Area, SUM(Fare) AS Revenue
FROM trips
GROUP BY Pickup_Area
ORDER BY Revenue DESC LIMIT 1;

-- Average fare across all trips
SELECT AVG(Fare) AS Average_Fare FROM trips;
```

A **SQL View** was also created for reusable trip summaries:

```sql
CREATE VIEW trip_summary AS
SELECT Pickup_Area, COUNT(*) AS Total_Trips, SUM(Fare) AS Total_Revenue
FROM trips
GROUP BY Pickup_Area;
```

---

## Python Analysis — `python_analysis.py`

The script connects to MySQL via `pymysql`, loads data into **Pandas**, and generates charts with **Matplotlib**.

### Libraries Used
| Library | Role |
|---------|------|
| `pymysql` | MySQL database connection |
| `pandas` | Data manipulation & aggregation |
| `matplotlib` | Chart generation |

### Analysis Performed
| Analysis | Method |
|----------|--------|
| Peak Hour Detection | `value_counts()` on `Hour` column |
| Revenue Per Hour | `groupby("Hour")["Fare"].sum()` |
| Average Fare | `df["Fare"].mean()` |
| Busiest Pickup Area | `value_counts().idxmax()` |
| Payment Distribution | Pie chart via `matplotlib` |
| Revenue by Area | Bar chart via `matplotlib` |

### Key Findings
- 🕖 **Peak Hour:** 19:00 (7 PM) — 23 rides
- 📍 **Busiest Area:** Gulshan & Mirpur (39 trips each)
- 💰 **Average Fare:** ৳436.38
- 💳 **Top Payment Method:** Card (39% of revenue)

---

## Power BI Dashboard — `uber_dashboard_final.pbix`

An interactive dashboard with **6 visuals** built in Power BI:

| Chart | Description |
|-------|-------------|
| 📈 Monthly Revenue Trend | Bar chart of total fare Jan–Dec |
| 🍩 Payment Methods | Donut chart — Card / bKash / Cash split |
| 🗺️ Trips by Area | Horizontal bar chart per pickup zone |
| ⏰ Hourly Demand | Line chart of rides by hour of day |
| 🏆 Top 5 Drivers | Highest-earning drivers by revenue |
| 🏙️ Avg Fare by Area | Which zones command higher fares |

> Open `uber_dashboard_final.pbix` in **Power BI Desktop** to explore.

---

## Key Insights

```
May was the peak revenue month ............ ৳12,029  (~25× January)
Card payments dominate total revenue ....... 39%  (৳34,234)
Mirpur has the highest average fare ........ ৳471.7 per trip
Peak demand hours .......................... 19:00 – 22:00
Top earning driver ......................... D16 with ৳6,181
Busiest pickup zones ....................... Gulshan & Mirpur (39 trips each)
```

---

## How to Run

**1 — Set up the database**
```sql
CREATE DATABASE uber_project;
USE uber_project;
-- Import the CSV into a `trips` table
```

**2 — Run SQL queries**

Open `uber_project_queries.sql` in MySQL Workbench and execute.

**3 — Run Python analysis**
```bash
pip install pymysql pandas matplotlib
python python_analysis.py
```
> ⚠️ Update credentials in `python_analysis.py` first:
> ```python
> conn = pymysql.connect(host="127.0.0.1", user="root", password="YOUR_PASSWORD", database="uber_project")
> ```

**4 — View the dashboard**

Open `uber_dashboard_final.pbix` in [Power BI Desktop](https://powerbi.microsoft.com/desktop/).

---

## Dataset — `ubar_project_excel_file.csv`

| Column | Description |
|--------|-------------|
| `Trip_ID` | Unique identifier for each trip |
| `Trip_Date` | Date of the trip |
| `Pickup_Time` | Timestamp of pickup |
| `Hour_of_Day` | Extracted hour (0–23) |
| `Pickup_Area` | Zone where the ride started |
| `Distance_Km` | Trip distance in kilometers |
| `Ride_Duration_Min` | Ride duration in minutes |
| `Fare` | Fare charged in BDT (৳) |
| `Payment_Type` | Card / bKash / Cash |
| `Driver_ID` | Anonymized driver identifier |

---

<div align="center">



## Author

**Faria Afrin Sithi**

Final Year Student · Diploma in Engineering, Computer Science

*Passionate about data analysis, business intelligence, and turning raw data into meaningful insights.*

<br/>

[![Email](https://img.shields.io/badge/Gmail-fariaafrinsithi%40gmail.com-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:fariaafrinsithi@gmail.com)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Faria_Afrin_Sithi-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/faria-afrin-264a693a6/)




---

*This project is for educational purposes. Dataset is synthetic/anonymized.*
<img width="902" height="498" alt="image" src="https://github.com/user-attachments/assets/784f9ce5-a54a-4c85-a406-91a87c9eb2ac" />

</div>
