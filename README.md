# Project BOPHELO: Simulation Code

This repository contains a conceptual healthcare pathway diagram, a synthetic
patient simulation, and a proposed monitoring framework for a rural Lesotho TB
care intervention developed for a Partners In Health Canada case competition.

## Running the code

Install Python 3 and Graphviz (the system executable), then run:

```bash
pip install -r requirements.txt
python tb_simulation.py
python pipeline_diagram.py
python monitoring_framework.py
```

The simulation writes `simulation_summary.csv` and `diagnostic_comparison.png`.
The diagram writes `care_pipeline.png`. These are generated outputs.

**Important:** The simulated 5,000 patients, assumptions, probabilities, and
resulting improvements are hypothetical. The model is not calibrated to real
Lesotho patient data and cannot establish clinical effectiveness, transmission
reduction, or treatment benefit. The infectious-days variable is a simplified
proxy rather than a validated infectiousness model.
