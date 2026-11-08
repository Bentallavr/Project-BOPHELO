"""Conceptual community-centered TB care pathway diagram."""
from graphviz import Digraph


def build_diagram():
    pipeline = Digraph('bophelo_pipeline', format='png')
    pipeline.attr(rankdir='TB', size='6,10')
    pipeline.attr('node', shape='box', style='rounded,filled', fillcolor='#F4F7FB', fontname='Helvetica', fontsize='11')
    pipeline.node('A', 'Community Entry\n(Stigma Free)\n\nCHWs • Chiefs • Trusted Groups\nNo TB / HIV Labeling')
    pipeline.node('B', 'Care Without Cost Buffer\n\nTransport Coordination\nFood Support\nTime Protection')
    pipeline.node('C', 'Parallel Care Processing\n\nReferral Scheduling\nDiagnostics Booking\nCHW Assignment')
    pipeline.node('D', 'Single Trip Clinic Visit\n\nTesting + Clinical Evaluation\nSame Day')
    pipeline.node('E', 'Treatment & Accompaniment\n\nAdherence Support\nNutrition\nSide Effect Management')
    pipeline.node('F', 'Missed Visit?\n\nSupportive Reengagement\nNo Exclusion • No Punishment')
    pipeline.node('G', 'Monitoring & Learning Layer\n\n5 Year: Access & Delays\n10 Year: Completion & MDR TB\n15 Year: Transmission & Mortality')
    for source, target in [('A','B'),('B','C'),('C','D'),('D','E'),('E','F'),('E','G')]:
        pipeline.edge(source, target)
    pipeline.edge('F', 'E', label='Return to Care')
    return pipeline


if __name__ == '__main__':
    build_diagram().render('care_pipeline', cleanup=True)
