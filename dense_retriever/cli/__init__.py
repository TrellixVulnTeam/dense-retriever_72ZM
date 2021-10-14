import click
from .ann_index import run_search_prebuilt_index_command, run_search_from_scratch_command, \
    run_evaluation_command


@click.group()
def run():
    pass


run.add_command(run_search_prebuilt_index_command, 'search_from_prebuilt')
run.add_command(run_search_from_scratch_command, 'search_from_scratch')
run.add_command(run_evaluation_command, 'evaluate_index')
