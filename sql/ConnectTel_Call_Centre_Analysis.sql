create database connecttel;
use connecttel;
show databases;

CREATE TABLE call_center (
    Team VARCHAR(20),
    AgentID VARCHAR(20),
    Day VARCHAR(20),
    Shift VARCHAR(20),
    Experience VARCHAR(30),
    CallsHandled INT,
    AvgCallDuration DECIMAL(10,2),
    EscalationRate DECIMAL(10,2),
    FCRRate DECIMAL(10,2),
    CSATScore DECIMAL(10,2),
    OvertimeHours DECIMAL(10,2),
    CostPerCall DECIMAL(10,2),
    CostCategory VARCHAR(10)
);

show tables;
describe call_center;

USE connecttel;

SELECT COUNT(*) AS total_records
FROM call_center;

SELECT *
FROM call_center
LIMIT 5;

SELECT
    Team,
    SUM(CallsHandled) AS TotalCalls
FROM call_center
GROUP BY Team
ORDER BY TotalCalls DESC;

SELECT
    Team,
    AVG(AvgCallDuration) AS AverageCallDuration
FROM call_center
GROUP BY Team
ORDER BY AverageCallDuration DESC;

SELECT
    Team,
    AVG(CostPerCall) AS AverageCostPerCall
FROM call_center
GROUP BY Team
ORDER BY AverageCostPerCall DESC;

SELECT
    Team,
    COUNT(*) AS HighCostCalls
FROM call_center
WHERE CostCategory = 'High'
GROUP BY Team
ORDER BY HighCostCalls DESC;

SELECT
    Team,
    COUNT(CASE WHEN CostCategory = 'High' THEN 1 END) * 100.0 / COUNT(*) AS HighCostRate
FROM call_center
GROUP BY Team
ORDER BY HighCostRate DESC;

SELECT
    Team,
    AVG(OvertimeHours) AS AverageOvertimeHours
FROM call_center
GROUP BY Team
ORDER BY AverageOvertimeHours DESC;

SELECT
    Team,
    AVG(CSATScore) AS AverageCSAT
FROM call_center
GROUP BY Team
ORDER BY AverageCSAT DESC;

SELECT
    Team,
    AVG(FCRRate) AS AverageFCR
FROM call_center
GROUP BY Team
ORDER BY AverageFCR DESC;

SELECT
    Team,
    AVG(EscalationRate) AS AverageEscalationRate
FROM call_center
GROUP BY Team
ORDER BY AverageEscalationRate DESC;

SELECT
    CostCategory,
    COUNT(*) AS NumberOfCalls
FROM call_center
GROUP BY CostCategory
ORDER BY NumberOfCalls DESC;

SELECT
    CostCategory,
    AVG(AvgCallDuration) AS AverageCallDuration
FROM call_center
GROUP BY CostCategory
ORDER BY AverageCallDuration DESC;

SELECT
    Shift,
    COUNT(*) AS NumberOfCalls,
    AVG(CostPerCall) AS AverageCostPerCall
FROM call_center
GROUP BY Shift
ORDER BY AverageCostPerCall DESC;

SELECT
    Experience,
    COUNT(*) AS NumberOfCalls,
    AVG(CostPerCall) AS AverageCostPerCall,
    AVG(CSATScore) AS AverageCSAT
FROM call_center
GROUP BY Experience
ORDER BY AverageCostPerCall DESC;

SELECT
    OvertimeHours,
    AVG(CostPerCall) AS AverageCostPerCall
FROM call_center
GROUP BY OvertimeHours
ORDER BY OvertimeHours;

SELECT
    OvertimeHours,
    AVG(CSATScore) AS AverageCSAT
FROM call_center
GROUP BY OvertimeHours
ORDER BY OvertimeHours;

SELECT
    Shift,
    AVG(OvertimeHours) AS AverageOvertimeHours
FROM call_center
GROUP BY Shift
ORDER BY AverageOvertimeHours DESC;

SELECT
    Shift,
    COUNT(CASE WHEN CostCategory = 'High' THEN 1 END) * 100.0 / COUNT(*) AS HighCostRate
FROM call_center
GROUP BY Shift
ORDER BY HighCostRate DESC;

SELECT
    FCRRate,
    AVG(CostPerCall) AS AverageCostPerCall
FROM call_center
GROUP BY FCRRate
ORDER BY FCRRate;

SELECT
    CASE
        WHEN FCRRate < 0.70 THEN '60-69%'
        WHEN FCRRate < 0.80 THEN '70-79%'
        WHEN FCRRate < 0.90 THEN '80-89%'
        ELSE '90%+'
    END AS FCRRange,
    COUNT(*) AS NumberOfCalls,
    AVG(CostPerCall) AS AverageCostPerCall,
    AVG(CSATScore) AS AverageCSAT
FROM call_center
GROUP BY FCRRange
ORDER BY FCRRange;

SELECT
    EscalationRate,
    AVG(CostPerCall) AS AverageCostPerCall
FROM call_center
GROUP BY EscalationRate
ORDER BY EscalationRate;

SELECT
    AgentID,
    COUNT(*) AS NumberOfCalls,
    AVG(CostPerCall) AS AverageCostPerCall
FROM call_center
GROUP BY AgentID
ORDER BY AverageCostPerCall DESC;

SELECT
    AgentID,
    COUNT(*) AS NumberOfCalls,
    AVG(AvgCallDuration) AS AverageCallDuration
FROM call_center
GROUP BY AgentID
ORDER BY AverageCallDuration DESC;

SELECT
    Team,
    SUM(CostPerCall) AS TotalCost
FROM call_center
GROUP BY Team
ORDER BY TotalCost DESC;

SELECT
    Team,
    SUM(CostPerCall) AS TotalCost,
    SUM(CallsHandled) AS TotalCalls,
    SUM(CostPerCall) / SUM(CallsHandled) AS CostPerHandledCall
FROM call_center
GROUP BY Team
ORDER BY CostPerHandledCall DESC;

SELECT
    AvgCallDuration,
    CostPerCall
FROM call_center
ORDER BY AvgCallDuration;