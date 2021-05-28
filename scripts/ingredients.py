#!/usr/bin/env python
"""
Turn the ingredients folder into a single json file
"""
import json
import sys
import yaml
from pathlib import Path
from slugify import slugify

ROOT = Path(__file__).parent.parent / "ingredients"


def main():
    """
    Walk through ROOT and parse things
    """
    ingredients = {"types": {}}
    for path in ROOT.iterdir():
        if path.is_dir():
            continue

        group = yaml.safe_load(path.read_text())
        ingredients[path.stem] = list(
            parse_ingredients(group.pop("ingredients"), type=path.stem, **group)
        )
        ingredients["types"][path.stem] = group

    json.dump(ingredients, sys.stdout)


def parse_ingredients(items, **metadata):
    for item in items:
        if isinstance(item, str):
            yield {"name": item, "id": slugify(item), "type": metadata.get("type")}

        # only objects from here
        # assert isinstance(item, dict)
        if isinstance(item, dict):
            item.setdefault("id", slugify(item["name"]))
            item.setdefault("type", metadata.get("type"))
            item.setdefault("allergies", metadata.get("allergies", []))

            yield item


if __name__ == "__main__":
    main()