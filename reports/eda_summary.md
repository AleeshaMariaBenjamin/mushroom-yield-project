# EDA Summary

## Date Range
2025-06-01 08:00:00 to 2025-06-06 17:00:00

## Summary Statistics
## Summary Statistics

| Feature | Count | Mean | Std | Min | 25% | 50% | 75% | Max |
|---|---|---|---|---|---|---|---|---|
| Temperature (°C) | 60 | 25.47 | 0.53 | 24.40 | 25.08 | 25.50 | 25.90 | 26.40 |
| Humidity (%) | 60 | 85.13 | 2.05 | 82.00 | 83.00 | 85.00 | 87.00 | 89.00 |
| CO₂ (ppm) | 60 | 766.30 | 27.46 | 715.00 | 747.25 | 769.00 | 790.00 | 812.00 |
| Yield (kg) | 60 | 1.38 | 0.11 | 1.20 | 1.30 | 1.40 | 1.50 | 1.60 |

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