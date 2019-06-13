#!/usr/bin/env python3

import logging
import sys
import os

import click
import newspaper

@click.command()
@click.option('-s', '--sources', type=click.Path(exists=True), help="File containing news source URLs on each line, defaults to taking them from stdin if not set.")
@click.option('-v', '--verbose', is_flag=True, help="Enable verbose logging.")
def cli(sources, verbose):
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
        for article in paper.articles:
            try:
                article.download()
                article.parse()
                print(article.text)
            except:
                pass
