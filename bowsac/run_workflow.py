import importlib.util
import json
from pathlib import Path
import inspect
import sys
import click

from .workflow import Workflow


def load_json(ctx, param, value):
    try:
        return json.loads(value)
    except ValueError:
        raise click.BadParameter(f"Invalid JSON: {value}.")


def load_file(ctx, param, file_str):
    # https://github.com/ManimCommunity/manim/blob/9d1f066d637cb15baea10e6907ab85efff8fb36f/manim/utils/module_ops.py#L48
    try:
        file_path = Path(file_str)
        module_name = '.'.join(file_path.with_suffix('').parts)
        spec = importlib.util.spec_from_file_location(module_name, file_path)
        module = importlib.util.module_from_spec(spec)
        sys.modules[module_name] = module
        sys.path.insert(0, str(file_path.parent.absolute()))
        spec.loader.exec_module(module)
        return module
    except AttributeError:
        raise click.BadParameter(f"Unloadable python file: {file_str}.")


def is_workflow(obj, module):
    return (
        inspect.isclass(obj)
        and issubclass(obj, Workflow)
        and obj != Workflow
        and obj.__module__.startswith(module.__name__)
    )


@click.command()
@click.option('-f', "--file", "module",
              required=True, help="Python file to load workflows.",
              type=click.UNPROCESSED, callback=load_file)
@click.option('-c', "--ctx", "ctx",
              default='{}', help="Context as JSON.",
              type=click.UNPROCESSED, callback=load_json)
def main(module, ctx):

    for cls_name, cls in inspect.getmembers(module, lambda cls: is_workflow(cls, module)):
        print(f'Started workflow [{cls_name}]')
        instance = cls()
        instance.run(ctx)
        print(f'Finishd workflow [{cls_name}]')


if __name__ == '__main__':
    main()
