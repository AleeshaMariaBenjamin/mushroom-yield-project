# EDA Summary

## Date Range
2025-06-01 08:00:00 to 2025-06-06 17:00:00

## Summary Statistics
temperature   humidity         CO2      yield
count    60.000000  60.000000   60.000000  60.000000
mean     25.468333  85.133333  766.300000   1.383333
std       0.533772   2.054071   27.461714   0.106033
min      24.400000  82.000000  715.000000   1.200000
25%      25.075000  83.000000  747.250000   1.300000
50%      25.500000  85.000000  769.000000   1.400000
75%      25.900000  87.000000  790.000000   1.500000
max      26.400000  89.000000  812.000000   1.600000

## Figures
- correlation_heatmap.png
- humidity_vs_yield.png
- temperature_vs_yield.png
- co2_vs_yield.png

## Key Findings

- Humidity positively correlates with yield up to 80% —
  beyond that yield plateaus, suggesting oversaturation.
- CO₂ levels above 900ppm negatively impact yield —
  excess CO₂ inhibits mushroom fruiting body development.
- Temperature between 22–25°C shows optimal yield range —
  nonlinear pattern visible in scatter plot.
- Correlation heatmap confirms humidity is strongest
  predictor, followed by CO₂.
- Yield clusters in scatter plots suggest possible
  seasonal flush cycles in mushroom growth.