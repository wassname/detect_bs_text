import frontmatter
from pathlib import Path
from loguru import logger
import pandas as pd

def load_md(f: Path = Path("../samples/"), max_chars=2000):
    sample_files = sorted(f.glob('*.md'))
    samples = []
    for f in sample_files:
        logger.debug(f)
        with open(f, "r") as file:
            post = frontmatter.load(file)
            samples.append(dict(content=post.content[:max_chars], f=f, **post.metadata))
    return samples

def load_md_df(f, max_chars=2000):
    samples = load_md(f, max_chars=max_chars)
    df = pd.DataFrame(samples)
    df = df[['title', 'f', 'content', 'url', 'novelty', 'date']]
    df['date'] = pd.to_datetime(df['date'], utc=True)
    df['in_training'] = df.date < '2024-01-01'
    return df
