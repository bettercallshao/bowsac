from collections import defaultdict

_steps_from_class = defaultdict(list)


def step(func):
    clsn = func.__qualname__.split('.')[0]
    _steps_from_class[clsn].append(func)
    return func


class Workflow(object):
    def run(self, ctx=dict()):
        clsn = self.__class__.__name__
        for step in _steps_from_class[clsn]:
            print(f'Started step [{step.__name__}]')
            step(self, ctx)
            print(f'Finishd step [{step.__name__}]')
