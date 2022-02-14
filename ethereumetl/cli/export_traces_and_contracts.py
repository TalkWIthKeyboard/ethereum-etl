import click

from ethereumetl.cli.export_all import get_partitions
from ethereumetl.jobs.export_all_common import export_traces_and_contracts_common
from ethereumetl.utils import check_classic_provider_uri


@click.command(context_settings=dict(help_option_names=['-h', '--help']))
@click.option('-s', '--start', required=True, type=str, help='Start block/ISO date/Unix time')
@click.option('-e', '--end', required=True, type=str, help='End block/ISO date/Unix time')
@click.option('-b', '--partition-batch-size', default=10000, show_default=True, type=int,
              help='The number of blocks to export in partition.')
@click.option('-p', '--provider-uri', default='https://mainnet.infura.io', show_default=True, type=str,
              help='The URI of the web3 provider e.g. '
                   'file://$HOME/Library/Ethereum/geth.ipc or https://mainnet.infura.io')
@click.option('-o', '--output-dir', default='output', show_default=True, type=str,
              help='Output directory, partitioned in Hive style.')
@click.option('-w', '--max-workers', default=5, show_default=True, type=int, help='The maximum number of workers.')
@click.option('-B', '--export-batch-size', default=100, show_default=True, type=int,
              help='The number of requests in JSON RPC batches.')
@click.option('-sb', '--s3-bucket', default='ifcrypto', show_default=True, type=str)
@click.option('-c', '--chain', default='ethereum', show_default=True, type=str, help='The chain network to connect to.')
def export_traces_and_contracts(start, end, partition_batch_size, provider_uri, output_dir, max_workers,
                                export_batch_size, s3_bucket, chain='ethereum'):
    """Exports traces and contracts for a range of blocks."""
    provider_uri = check_classic_provider_uri(chain, provider_uri)
    export_traces_and_contracts_common(
        get_partitions(start, end, partition_batch_size, provider_uri, 'export_traces_and_contracts'),
        output_dir, provider_uri, max_workers, export_batch_size, s3_bucket)
