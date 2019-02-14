# wiki_stats

## Dependencies

`pip install -r requirements.txt`

## Usage

Truncate part of Wikidata by running `python truncate.py` with `truncate.py` and `latest-all.json` in the same directory, and move the truncated dataset to `data` directory with name `data.json`.

In `data` directory, there is a sample subset of Wikidata containing first 100 entities in Wikidata.



To get the barchart of **top 20 frequent class with instances**  and **top 20 frequent class with subclasses**  in data, run:

```shell
python reader.py
```