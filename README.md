# 🔍 Predictive Spend & Supplier Risk Analytics using SAP Procurement Data

This project simulates a real-world procurement analytics pipeline using SAP-like data to identify high-risk suppliers and optimize spend. It includes end-to-end processes from data cleaning and feature engineering to machine learning modeling and Power BI dashboarding — making it ideal for data analyst, scientist, and SAP-integrated roles.

---

## 🚀 Project Highlights

- 📦 Simulated SAP MM procurement data (~300 records)
- 📊 Deep exploratory data analysis (EDA)
- 🤖 Predictive modeling to classify high-risk vendors
- 📈 Power BI dashboard to monitor spend, delays, and risk
- 💡 Feature importance insights and scorecards

---

## 🧰 Tech Stack

| Category       | Tools & Technologies                        |
|----------------|---------------------------------------------|
| Language       | Python 3 (pandas, matplotlib, seaborn)      |
| Modeling       | scikit-learn, Random Forest Classifier      |
| Dashboarding   | Power BI                                    |
| Project Tools  | Jupyter Notebook, VS Code, Git              |

---

## 📁 Project Structure

SAP-Procurement-Analytics/

├── data/

│ ├── sap_procurement_data.csv

│ └── supplier_risk_summary.csv

├── notebooks/

│ └── eda_modeling.ipynb

├── scripts/

│ └── model_pipeline.py

├── dashboard/

│ ├── Supplier_Risk_Dashboard.pbix

│ └── Supplier_Risk_Dashboard.pdf

├── README.md



---

## 🧾 Dataset Description

| Column             | Description                                 |
|--------------------|---------------------------------------------|
| Vendor_ID          | Unique supplier identifier                  |
| PO_Date            | Purchase order date                         |
| Delivery_Date      | Actual delivery date                        |
| Quantity, Unit_Price | Order details and pricing                 |
| Delay_Days         | Days between PO and delivery                |
| Supplier_Rating    | Rating (1 to 5) based on delivery/service   |
| Country            | Supplier country                            |
| High_Risk          | Flag: 1 = high-risk supplier                |

---

## 📊 Dashboard Highlights (Power BI)



- **Bar Chart**: Total Spend by Vendor
- **Map**: Spend by Country
- **Stacked Bar**: Risk Breakdown by Country
- **Donut Chart**: High vs Low Risk Vendors
- **Scatter Plot**: Delay vs Rating
- **KPI Cards**: Avg Delay, Total Spend, % High Risk
- **Filters**: Country, Risk Status

---

## 🧠 Machine Learning Model

- **Algorithm**: Random Forest Classifier
- **Target**: `High_Risk` (binary flag based on delay & rating)
- **Features**: Spend, Delay_Days, Supplier_Rating, Total_Orders
- **Accuracy**: ~90%
- **Top Predictors**: Delay_Days, Rating

Run the model:
```bash
python scripts/model_pipeline.py
```
```bash
git clone https://github.com/<your-username>/SAP-Procurement-Analytics.git
cd SAP-Procurement-Analytics
pip install -r requirements.txt  # optional if you generate it

```
“🙋‍♂️ Author 
**Ajaychary Kandukuri** 
🎓 Master’s Student in Data Science 
🔗 [Portfolio](https://ajaychary06.github.io/Portfolio/) 
🐍 [GitHub](https://github.com/ajaychary06) 
💼 [LinkedIn](https://www.linkedin.com/in/ajaychary-kandukuri-053a5a25a/)”


