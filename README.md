# bowsac

## Usage

Use `bowsac.workflow` to run `Workflow` classes with a context (`ctx`). It comes with a main method (`run_workflow`), so all you need to do is to define a `Workflow` with `step`'s.

Try it with following command. (after installing `click`)

```
# python3 -m bowsac.run_workflow -f examples/one.py -c '{"verbosity":"normal"}'
Started workflow [DoWork]
Started step [setup]
setup...
Finishd step [setup]
Started step [compose]
composing...
Finishd step [compose]
Started step [send]
sending...
The payload is normal payload
Finishd step [send]
Finishd workflow [DoWork]
```

## TODO

1. Improve documentation.

1. Set up a package for this and put on PyPI.
