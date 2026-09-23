# ConnectTel Call Centre Analysis

## Project Overview

This project analyses customer service call centre data for **ConnectTel**, a South African telecommunications provider. The goal is to understand the factors contributing to operating costs and identify patterns related to team performance, shifts, employee experience, call duration, overtime, escalation, first-call resolution (FCR), and customer satisfaction (CSAT).

The analysis combines data cleaning, exploratory data analysis, SQL analysis, visualisation, and a Power BI dashboard to turn the dataset into practical business insights.

## Business Problem

ConnectTel is experiencing high operating costs in its customer service call centre. The analysis investigates where inefficiencies may be occurring and how operational performance and customer experience are related to cost.

## Objectives

* Compare call volumes and costs across teams.
* Analyse performance across different shifts.
* Examine how employee experience relates to call handling and customer satisfaction.
* Investigate the relationship between call duration and cost per call.
* Analyse overtime and its relationship with operational cost.
* Review escalation rates, FCR rates, and CSAT scores.
* Identify high-cost versus low-cost calls.
* Present the findings in an interactive Power BI dashboard.

## Dataset

The final cleaned dataset contains:

* **450 records**
* **13 analysis columns**

Key fields include:

`Team`, `AgentID`, `Day`, `Shift`, `Experience`, `CallsHandled`, `AvgCallDuration`, `EscalationRate`, `FCRRate`, `CSATScore`, `OvertimeHours`, `CostPerCall`, and `CostPerCall(High/Low)`.

## Tools & Technologies

* **Excel** – data inspection, cleaning, validation, and supporting analysis
* **Python** – exploratory data analysis and visualisation
* **Pandas** – data manipulation and aggregation
* **Matplotlib** – charts and visualisations
* **MySQL / SQL** – structured analysis and business queries
* **Power BI** – interactive dashboard and reporting

## Analysis Performed

### Team Analysis

* Total calls handled by each team
* Team cost performance
* Team CSAT
* Team overtime

### Shift Analysis

* Calls handled by shift
* Escalation rate by shift
* Operational differences between shifts

### Experience Analysis

* Calls handled by experience level
* CSAT by experience level
* Performance patterns across employee experience groups

### Cost & Efficiency Analysis

* Average call duration versus cost per call
* Overtime versus cost
* High-cost versus low-cost calls

### Customer Experience Analysis

* FCR rate
* CSAT score
* Escalation rate
* Relationship between FCR and CSAT

## Key Findings

### 1. Team call volume

Team C handled the highest total number of calls, with **8,229 calls**.

Team B handled **8,082 calls**, while Team A handled **8,027 calls**.

This shows that workload was relatively close across the three teams, although Team C had the highest total volume.

### 2. Call duration and cost

The correlation between **average call duration and cost per call was 0.74**.

This indicates a strong positive relationship in this dataset: as call duration increases, cost per call generally increases as well.

### 3. FCR and CSAT

The calculated correlation between **FCR rate and CSAT score was 0.00**.

Within this dataset, the analysis did not show a linear correlation between these two measures. This means FCR should not be used alone to explain customer satisfaction.

### 4. High-cost calls

The dataset contained:

* **113 high-cost calls**
* **337 low-cost calls**

High-cost calls represented approximately **25.1%** of the analysed records.

This provides a useful group for further investigation into the factors driving higher operating costs.

### 5. Shift performance

The analysis compares shifts using call volume and escalation rate to identify differences in workload and service outcomes. These comparisons can help investigate whether staffing levels, workload distribution, or operating conditions differ across shifts.

### 6. Employee experience

Performance was analysed by employee experience level using call handling and CSAT measures. This helps identify whether experience is associated with differences in productivity or customer outcomes and where targeted coaching or support may be useful.

### 7. Overtime and cost

Overtime was analysed alongside cost measures to identify whether additional working hours may be contributing to higher operating costs.

## Visualisations

The `outputs/charts/` folder contains the charts produced during the analysis, including:

* Team calls
* Team cost
* Team CSAT
* Team overtime
* Shift calls
* Shift escalation
* Experience calls
* Experience CSAT
* Overtime vs cost
* Call duration vs cost
* High-cost / low-cost analysis

## Power BI Dashboard

The interactive dashboard is available in:

`powerbi/ConnectTel_Dashboard.pbix`

The dashboard brings the analysis together into a business-facing reporting view.

## SQL Analysis

SQL queries used for the project are available in:

`sql/ConnectTel_Call_Centre_Analysis.sql`

These queries support aggregation, comparison, and business-focused analysis of the call centre data.

## Python Analysis

Python scripts are available in:

`python/`

The analysis includes data loading, cleaning, aggregation, correlation analysis, and chart generation.

## Project Structure

```text
ConnectTel-Call-Centre-Analysis/
│
├── data/
│   └── ConnectTel Customer Service Call Centre Analysis .xlsx
│
├── outputs/
│   ├── cleaned_call_center_data.csv
│   ├── cleaned_call_center_data.xlsx
│   └── charts/
│
├── powerbi/
│   └── ConnectTel_Dashboard.pbix
│
├── python/
│   ├── eda.py
│   └── main.py
│
├── sql/
│   └── ConnectTel_Call_Centre_Analysis.sql
│
└── README.md
```

## Business Recommendations

Based on the analysis, the following areas can be investigated further:

1. **Investigate long-duration calls** to understand why they are more expensive and whether call flows or processes can be improved.
2. **Review shift-level workload and escalation patterns** to support better staffing and workload allocation.
3. **Investigate high-cost calls separately** to identify recurring drivers of cost.
4. **Use experience-level analysis to target coaching and support** where performance differences are observed.
5. **Monitor cost and customer-experience metrics together** rather than relying on a single KPI.

## Learning Outcomes

Through this project, I practised:

* Data cleaning and preparation
* Exploratory data analysis
* Grouping and aggregation
* Correlation analysis
* Data visualisation
* SQL querying
* Dashboard development
* Translating data findings into business recommendations

## Author

**Mamikie Murendeni Malima**
BSc Mathematical Sciences Graduate (Computer Science & Mathematics)

GitHub: [Mamikie02](https://github.com/Mamikie02)

LinkedIn: [Mamikie Malima](https://www.linkedin.com/in/mamikie-malima-6bb341207/)
