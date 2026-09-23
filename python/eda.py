import pandas as pd
import matplotlib.pyplot as plt

# Load the cleaned dataset
df = pd.read_excel(r"outputs\cleaned_call_center_data.xlsx")

print("=" * 50)
print("CONNECTTEL CALL CENTER ANALYSIS")
print("=" * 50)

#Total calls handled by each team
team_calls = ( 
    df.groupby("Team")["CallsHandled"]
          .sum()
          .sort_values(ascending=False)
)

print("\n Total Calls Handled by Team")
print("-" * 35)
print(team_calls)

#create a figure
plt.figure(figsize = (8,5))

#create the bars
bars = plt.bar(team_calls.index, team_calls.values)

#Add chart title
plt.title("Total Calls Handled by Team")

#Axis labels
plt.xlabel("Team")
plt.ylabel("Total Calls")

# Add a grid
plt.grid(axis="y", linestyle="--", alpha=0.4)

# Add values above each bar
for bar in bars:
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width()/2,
        height + 20,
        f"{int(height)}",
        ha="center"
    )
    
# Save the chart
plt.savefig("outputs/charts/team_calls.png")

# Show the chart
plt.show()

shift_calls = (  
    df.groupby("Shift")["CallsHandled"]
      .sum()
      .sort_values(ascending=False)
)

print("\n")
print("=" * 50)
print("TOTAL CALLS BY SHIFT")
print("=" * 50)
print(shift_calls)

plt.figure(figsize=(8,5))

bars = plt.bar(shift_calls.index, shift_calls.values)

plt.title("Total Calls Handled by Shift", fontsize=16, fontweight="bold")
plt.xlabel("Shift")
plt.ylabel("Total Calls")
plt.grid(axis="y", linestyle="--", alpha=0.4)

for bar in bars:
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width()/2,
        height + 20,
        f"{int(height)}",
        ha="center"
    )

plt.savefig("outputs/charts/shift_calls.png", dpi=300)
plt.show()

# ==========================
# Average CSAT by Team
# ==========================

team_csat = (
    df.groupby("Team")["CSATScore"]
      .mean()
      .sort_values(ascending=False)
)

print("\n")
print("=" * 50)
print("AVERAGE CSAT SCORE BY TEAM")
print("=" * 50)
print(team_csat)

plt.figure(figsize=(8,5))

bars = plt.bar(team_csat.index, team_csat.values)

plt.title("Average CSAT Score by Team", fontsize=16, fontweight="bold")
plt.xlabel("Team")
plt.ylabel("Average CSAT Score")

plt.grid(axis="y", linestyle="--", alpha=0.4)

for bar in bars:
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width()/2,
        height + 0.02,
        f"{height:.2f}",
        ha="center"
    )

plt.savefig("outputs/charts/team_csat.png", dpi=300)

plt.show()

# ==========================
# Average Calls by Experience
# ==========================

experience_calls = (
    df.groupby("Experience")["CallsHandled"]
      .mean()
      .sort_values(ascending=False)
)

print("\n")
print("=" * 50)
print("AVERAGE CALLS HANDLED BY EXPERIENCE")
print("=" * 50)
print(experience_calls)

plt.figure(figsize=(8,5))

bars = plt.bar(experience_calls.index, experience_calls.values)

plt.title("Average Calls Handled by Experience", fontsize=16, fontweight="bold")
plt.xlabel("Experience")
plt.ylabel("Average Calls Handled")

plt.grid(axis="y", linestyle="--", alpha=0.4)

for bar in bars:
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width()/2,
        height + 0.5,
        f"{height:.1f}",
        ha="center"
    )

plt.savefig("outputs/charts/experience_calls.png", dpi=300)
plt.show()

# ==========================
# Average Cost Per Call by Overtime Hours
# ==========================

overtime_cost = (
    df.groupby("OvertimeHours")["CostPerCall"]
      .mean()
      .sort_index()
)

print("\n")
print("=" * 50)
print("AVERAGE COST PER CALL BY OVERTIME HOURS")
print("=" * 50)
print(overtime_cost)

plt.figure(figsize=(8,5))

bars = plt.bar(overtime_cost.index.astype(str), overtime_cost.values)

plt.title("Average Cost Per Call by Overtime Hours",
          fontsize=16,
          fontweight="bold")

plt.xlabel("Overtime Hours")
plt.ylabel("Average Cost Per Call")

plt.grid(axis="y", linestyle="--", alpha=0.4)

for bar in bars:
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width()/2,
        height + 0.1,
        f"{height:.2f}",
        ha="center"
    )

plt.savefig("outputs/charts/overtime_cost.png", dpi=300)

plt.show()

# ==========================
# Average Escalation Rate by Shift
# ==========================

shift_escalation = (
    df.groupby("Shift")["EscalationRate"]
      .mean()
      .sort_values(ascending=False)
)

print("\n")
print("=" * 50)
print("AVERAGE ESCALATION RATE BY SHIFT")
print("=" * 50)
print(shift_escalation)

plt.figure(figsize=(8,5))

bars = plt.bar(
    shift_escalation.index,
    shift_escalation.values
)

plt.title(
    "Average Escalation Rate by Shift",
    fontsize=16,
    fontweight="bold"
)

plt.xlabel("Shift")
plt.ylabel("Average Escalation Rate")

plt.grid(axis="y", linestyle="--", alpha=0.4)

for bar in bars:
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width()/2,
        height + 0.005,
        f"{height:.2%}",
        ha="center"
    )

plt.savefig(
    "outputs/charts/shift_escalation.png",
    dpi=300
)

plt.show()

# ==========================
# Average CSAT by Experience
# ==========================

experience_csat = (
    df.groupby("Experience")["CSATScore"]
      .mean()
      .sort_values(ascending=False)
)

print("\n")
print("=" * 50)
print("AVERAGE CSAT SCORE BY EXPERIENCE")
print("=" * 50)
print(experience_csat)

plt.figure(figsize=(8,5))

bars = plt.bar(
    experience_csat.index,
    experience_csat.values
)

plt.title(
    "Average CSAT Score by Experience",
    fontsize=16,
    fontweight="bold"
)

plt.xlabel("Experience")
plt.ylabel("Average CSAT Score")

plt.grid(axis="y", linestyle="--", alpha=0.4)

for bar in bars:
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width()/2,
        height + 0.02,
        f"{height:.2f}",
        ha="center"
    )

plt.savefig(
    "outputs/charts/experience_csat.png",
    dpi=300
)

plt.show()

# ==========================
# Average Cost Per Call by Team
# ==========================

team_cost = (
    df.groupby("Team")["CostPerCall"]
      .mean()
      .sort_values(ascending=False)
)

print("\n")
print("=" * 50)
print("AVERAGE COST PER CALL BY TEAM")
print("=" * 50)
print(team_cost)

plt.figure(figsize=(8,5))

bars = plt.bar(
    team_cost.index,
    team_cost.values
)

plt.title(
    "Average Cost Per Call by Team",
    fontsize=16,
    fontweight="bold"
)

plt.xlabel("Team")
plt.ylabel("Average Cost Per Call")

plt.grid(axis="y", linestyle="--", alpha=0.4)

for bar in bars:
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width()/2,
        height + 0.1,
        f"{height:.2f}",
        ha="center"
    )

plt.savefig(
    "outputs/charts/team_cost.png",
    dpi=300
)

plt.show()

# ==========================
# Average Overtime Hours by Team
# ==========================

team_overtime = (
    df.groupby("Team")["OvertimeHours"]
      .mean()
      .sort_values(ascending=False)
)

print("\n")
print("=" * 50)
print("AVERAGE OVERTIME HOURS BY TEAM")
print("=" * 50)
print(team_overtime)

plt.figure(figsize=(8,5))

bars = plt.bar(
    team_overtime.index,
    team_overtime.values
)

plt.title(
    "Average Overtime Hours by Team",
    fontsize=16,
    fontweight="bold"
)

plt.xlabel("Team")
plt.ylabel("Average Overtime Hours")

plt.grid(axis="y", linestyle="--", alpha=0.4)

plt.savefig(
    "outputs/charts/team_overtime.png",
    dpi=300
)

plt.show()

# ==========================
# Call Duration vs Cost Per Call
# ==========================

plt.figure(figsize=(8,5))

plt.scatter(
    df["AvgCallDuration"],
    df["CostPerCall"]
)

plt.title(
    "Call Duration vs Cost Per Call",
    fontsize=16,
    fontweight="bold"
)

plt.xlabel("Average Call Duration (minutes)")
plt.ylabel("Cost Per Call")

plt.grid(alpha=0.4)

plt.savefig(
    "outputs/charts/duration_vs_cost.png",
    dpi=300
)

plt.show()

# ==========================
# Correlation: Call Duration vs Cost
# ==========================

correlation = df["AvgCallDuration"].corr(df["CostPerCall"])

print("\n")
print("=" * 50)
print("CORRELATION: CALL DURATION VS COST")
print("=" * 50)
print(f"Correlation: {correlation:.2f}")

# ==========================
# FCR Rate vs Customer Satisfaction
# ==========================

correlation_fcr_csat = df["FCRRate"].corr(df["CSATScore"])

print("\n")
print("=" * 50)
print("CORRELATION: FCR RATE VS CSAT SCORE")
print("=" * 50)
print(f"Correlation: {correlation_fcr_csat:.2f}")

# ==========================
# High vs Low Cost Calls
# ==========================

cost_category = df["CostPerCall(High/Low)"].value_counts()

print("\n")
print("=" * 50)
print("HIGH VS LOW COST CALLS")
print("=" * 50)
print(cost_category)

# ==========================
# Average Call Duration by Cost Category
# ==========================

cost_duration = (
    df.groupby("CostPerCall(High/Low)")["AvgCallDuration"]
      .mean()
      .sort_values(ascending=False)
)

print("\n")
print("=" * 50)
print("AVERAGE CALL DURATION BY COST CATEGORY")
print("=" * 50)
print(cost_duration)

# ==========================
# High-Cost Calls by Team
# ==========================

high_cost_by_team = (
    df[df["CostPerCall(High/Low)"] == "High"]
    .groupby("Team")
    .size()
    .sort_values(ascending=False)
)

print("\n")
print("=" * 50)
print("HIGH-COST CALLS BY TEAM")
print("=" * 50)
print(high_cost_by_team)

# ==========================
# High-Cost Call Rate by Team
# ==========================

team_cost_rate = (
    df.groupby("Team")["CostPerCall(High/Low)"]
      .apply(lambda x: (x == "High").mean() * 100)
      .sort_values(ascending=False)
)

print("\n")
print("=" * 50)
print("HIGH-COST CALL RATE BY TEAM")
print("=" * 50)
print(team_cost_rate.round(2))

# ==========================
# High-Cost Call Rate by Shift
# ==========================

shift_cost_rate = (
    df.groupby("Shift")["CostPerCall(High/Low)"]
      .apply(lambda x: (x == "High").mean() * 100)
      .sort_values(ascending=False)
)

print("\n")
print("=" * 50)
print("HIGH-COST CALL RATE BY SHIFT")
print("=" * 50)
print(shift_cost_rate.round(2))