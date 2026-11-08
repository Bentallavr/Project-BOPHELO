"""Exploratory synthetic TB care pathway comparison for Project BOPHELO.

All probabilities and time distributions are hypothetical, not calibrated to
clinical data. Outputs are not estimates of intervention effectiveness.
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def simulate(n=5000, seed=42):
    rng = np.random.default_rng(seed)
    barrier = np.clip(rng.beta(2, 2, size=n), 0, 1)

    encounters_baseline = rng.integers(2, 22, size=n)
    days_between = np.clip(rng.lognormal(mean=2.0, sigma=0.6, size=n), 2, 45)
    days_to_dx_baseline = np.clip(encounters_baseline * days_between + rng.normal(0, 7, size=n), 5, 365)
    missed_baseline = rng.random(n) < np.clip(0.15 + 0.35 * barrier, 0, 0.85)
    dropped_baseline = rng.random(n) < np.clip(0.18 + 0.25 * barrier + 0.20 * missed_baseline.astype(float), 0, 0.95)
    infectious_days_baseline = np.where(dropped_baseline, np.clip(days_to_dx_baseline + 60, 30, 425), days_to_dx_baseline)

    encounters_pipeline = np.where(rng.random(n) < 0.75, 1, 2)
    days_between_pipeline = np.clip(rng.lognormal(mean=1.2, sigma=0.5, size=n), 1, 21)
    days_to_dx_pipeline = np.clip(encounters_pipeline * days_between_pipeline + rng.normal(0, 4, size=n), 2, 120)
    missed_pipeline = rng.random(n) < np.clip(0.08 + 0.12 * barrier, 0, 0.50)
    dropped_pipeline = rng.random(n) < np.clip(0.10 + 0.15 * barrier + 0.10 * missed_pipeline.astype(float), 0, 0.70)
    infectious_days_pipeline = np.where(dropped_pipeline, np.clip(days_to_dx_pipeline + 30, 15, 250), days_to_dx_pipeline)

    df = pd.DataFrame({
        'barrier_index': barrier,
        'encounters_baseline': encounters_baseline,
        'days_to_dx_baseline': days_to_dx_baseline,
        'missed_visit_baseline': missed_baseline,
        'dropout_baseline': dropped_baseline,
        'infectious_days_baseline': infectious_days_baseline,
        'encounters_pipeline': encounters_pipeline,
        'days_to_dx_pipeline': days_to_dx_pipeline,
        'missed_visit_pipeline': missed_pipeline,
        'dropout_pipeline': dropped_pipeline,
        'infectious_days_pipeline': infectious_days_pipeline,
    })
    metrics = [
        ('Median encounters before test', 'encounters', np.median),
        ('Median days to diagnosis', 'days_to_dx', np.median),
        ('Missed visit rate', 'missed_visit', np.mean),
        ('Dropout rate', 'dropout', np.mean),
        ('Median infectious days proxy', 'infectious_days', np.median),
    ]
    summary = pd.DataFrame([{
        'Metric': label,
        'Baseline': float(fn(df[f'{stem}_baseline'])),
        'Pipeline': float(fn(df[f'{stem}_pipeline'])),
    } for label, stem, fn in metrics])
    summary['Relative_change'] = (summary['Pipeline'] - summary['Baseline']) / summary['Baseline']
    return df, summary


def main():
    df, summary = simulate()
    print('HYPOTHETICAL MODEL OUTPUTS, NOT CLINICAL EVIDENCE')
    print(summary.to_string(index=False, float_format=lambda x: f'{x:.3f}'))
    plt.figure(figsize=(7, 4))
    plt.hist(df['days_to_dx_baseline'], bins=40, alpha=0.6, label='Baseline')
    plt.hist(df['days_to_dx_pipeline'], bins=40, alpha=0.6, label='Proposed pipeline')
    plt.xlabel('Days to diagnosis (synthetic)')
    plt.ylabel('Synthetic patient count')
    plt.title('Hypothetical time to diagnosis comparison')
    plt.legend()
    plt.tight_layout()
    plt.savefig('diagnostic_comparison.png', dpi=180)
    plt.close()
    summary.to_csv('simulation_summary.csv', index=False)


if __name__ == '__main__':
    main()
