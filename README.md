# Project BOPHELO

### Redesigning Tuberculosis Care Through Community Centred Systems Engineering

**McMaster University | Global Health Case Competition**

**Research Areas:** Global Health, Health Systems Engineering, Computational Modeling, Health Equity

**Technologies:** Python, NumPy, Pandas, Matplotlib, Graphviz

## Overview

Project BOPHELO was developed as part of a McMaster University case competition addressing delayed tuberculosis (TB) care seeking in rural Lesotho.

Although tuberculosis is preventable and treatable, individuals living in rural communities often experience significant barriers to timely diagnosis and treatment. These include geographical isolation, transportation costs, food insecurity, social stigma, and limited healthcare resources.

Our team proposed an equity focused healthcare framework that addresses these challenges by redesigning how patients access and navigate tuberculosis care.

Rather than introducing an entirely new diagnostic technology, the project focuses on improving the coordination, accessibility, and continuity of existing healthcare services.

## Proposed Framework

The intervention integrates six components:

1. **Community Engagement:** Establishing trusted entry points through community health workers, local leaders, and community organizations.

2. **Care Without Cost:** Coordinating transportation, nutritional assistance, and support for time away from work to reduce financial barriers.

3. **Parallel Care Coordination:** Organizing referrals, diagnostic appointments, and community health worker assignments simultaneously.

4. **Consolidated Clinical Visits:** Reducing unnecessary travel by coordinating testing and clinical evaluation within a single visit where feasible.

5. **Treatment Support:** Providing continued guidance, nutritional support, and community health worker involvement throughout treatment.

6. **Supportive Reengagement:** Responding to missed appointments through outreach and assistance rather than exclusion.

## Computational Modeling

To explore the potential impact of this framework, I developed a Python simulation using 5,000 synthetic patient records.

The model compared a conventional tuberculosis care pathway with the proposed redesigned system, incorporating simulated barriers related to socioeconomic conditions, geography, stigma, and healthcare accessibility.

The analysis examined diagnostic delays, the number of healthcare encounters before testing, missed appointments, treatment dropout, and a simplified proxy for infectious time.

NumPy was used for synthetic data generation, Pandas for comparative analysis, Matplotlib for visualization, and Graphviz for illustrating the proposed healthcare pipeline.

## Simulation Findings

Under the selected assumptions, the redesigned care pathway produced shorter simulated diagnostic delays, fewer healthcare encounters, and lower missed appointment and treatment dropout rates.

These findings illustrate the potential effects of the proposed system design within a hypothetical model. They do not represent observed patient outcomes or validated predictions of clinical effectiveness.

## Monitoring and Evaluation

A monitoring framework was developed to examine outcomes over three periods.

**5 Years:** Healthcare access, diagnostic delays, and missed appointments.

**10 Years:** Treatment completion, continuity of care, and multidrug resistant tuberculosis outcomes.

**15 Years:** Long term tuberculosis incidence, transmission, and mortality trends.

## My Contributions

My primary contributions focused on the computational and systems engineering components of the project, including:

* Designing and visualizing the proposed healthcare delivery pipeline.
* Developing the Python simulation comparing conventional and redesigned care pathways.
* Analyzing simulated diagnostic delays, missed appointments, and treatment dropout.
* Establishing a monitoring framework for evaluating outcomes over 5, 10, and 15 years.
* Presenting the proposed intervention through a health systems engineering perspective.

## Limitations and Future Directions

The simulation uses synthetic data and assumed probability distributions rather than empirical clinical data. Its results should therefore be interpreted as exploratory.

Future work could involve incorporating real world healthcare access data, conducting sensitivity analyses, evaluating feasibility with local healthcare stakeholders, and refining the proposed model for rural healthcare settings.

## Project Significance

Project BOPHELO highlights how meaningful healthcare innovation can emerge from improving existing systems rather than relying exclusively on new medical technologies.

By addressing the structural barriers that influence healthcare access, the project explores how community centred systems engineering may contribute to more equitable and sustainable tuberculosis care.
