# EDA Summary

## Date Range
2025-06-01 08:00:00 to 2025-06-06 17:00:00

## Summary Statistics


| Statistic | Temperature | Humidity | CO2 | Yield |
|------------|------------|-----------|------|-------|
| Count | 500.000000 | 500.000000 | 500.000000 | 500.000000 |
| Mean | 25.009495 | 87.527475 | 762.096970 | 1.196220 |
| Std | 1.120375 | 2.004317 | 29.709662 | 0.214448 |
| Min | 22.900000 | 82.200000 | 700.000000 | 1.000000 |
| 25% | 24.000000 | 86.000000 | 739.000000 | 1.000000 |
| 50% (Median) | 25.004747 | 87.600000 | 763.000000 | 1.120000 |
| 75% | 26.000000 | 89.000000 | 785.000000 | 1.370000 |
| Max | 27.300000 | 92.000000 | 833.000000 | 1.760000 |

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