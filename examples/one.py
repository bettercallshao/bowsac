from bowsac.workflow import Workflow, step


class DoWork(Workflow):

    @step
    def setup(self, ctx):
        print('setup...')
        if 'verbosity' not in ctx:
            ctx['verbosity'] = 'debug'

    @step
    def compose(self, ctx):
        print('composing...')
        if ctx['verbosity'] == 'debug':
            ctx['payload'] = 'debug debug debug'
        else:
            ctx['payload'] = 'normal payload'

    @step
    def send(self, ctx):
        print('sending...')
        print(f'The payload is {ctx["payload"]}')
