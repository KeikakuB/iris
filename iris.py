import logging
import sys
import os

import click
import newspaper


@click.command()
@click.option(
    '-s',
    '--sources',
    type=click.Path(exists=True),
    help=
    "File containing news source URLs on each line, defaults to taking them from stdin if not set."
)
@click.option('-n',
              '--max_articles_per_source',
              type=int,
              default=None,
              help="Maximum number of articles to pull from each source.")
@click.option('-v', '--verbose', is_flag=True, help="Enable verbose logging.")
def cli(sources, verbose, max_articles_per_source):
    logging_level = logging.DEBUG if verbose else logging.ERROR
    logging.basicConfig(stream=sys.stderr, level=logging_level)

    # Get Sources.
    f = open(sources, 'r') if sources else sys.stdin
    lines = f.readlines()
    lines = [x.strip() for x in lines]
    sources = lines
    if f is not sys.stdin:
        f.close()

    for paper_url in sources:
        paper = newspaper.build(paper_url)
        count = 0
        for article in paper.articles:
            if max_articles_per_source and count > max_articles_per_source:
                break
            try:
                article.download()
                article.parse()
                print(article.text)
                count += 1
            except:
                pass
