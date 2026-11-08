"""Proposed monitoring indicators; no real patient data is included."""
import pandas as pd


def build_monitoring_framework():
    return pd.DataFrame([
        ['5 years', 'Median days to diagnosis', 'Decrease', 'Pipeline log: symptom onset to test date'],
        ['5 years', 'Missed visit rate', 'Decrease', 'Scheduled versus attended visits'],
        ['5 years', 'Encounters before test', 'Decrease', 'Encounter count'],
        ['10 years', 'Treatment completion rate', 'Increase', 'Clinic and CHW registers'],
        ['10 years', 'Loss to follow up', 'Decrease', 'Program retention tracking'],
        ['10 years', 'MDR TB completion rate', 'Increase', 'MDR registry'],
        ['15 years', 'TB incidence', 'Decrease', 'District surveillance'],
        ['15 years', 'TB mortality', 'Decrease', 'Vital registration and facility data'],
    ], columns=['Time_horizon', 'Indicator', 'Direction', 'Proposed_data_source'])


if __name__ == '__main__':
    print(build_monitoring_framework().to_string(index=False))
