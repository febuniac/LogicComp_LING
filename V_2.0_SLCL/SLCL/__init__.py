import time
import slcl.parser as p
import slcl.ast
import slcl.environment
import slcl.exceptions
import pprint
import sys


def execute(source, show_ast: bool=False, disable_warnings: bool=True):
    p.disable_warnings = disable_warnings

    try:
        res = p.get_parser().parse(source)
        environment.declare_env(slcl.ast.symbols)

        for node in res.children:
            node.eval()

        if show_ast:
            print("\n\n" + '=' * 80, ' == Syntax tree ==')

            pp = pprint.PrettyPrinter()
            pp.pprint(res.children)
            pp.pprint(slcl.ast.symbols.table())
    except Exception as e:
        print(e.__class__.__name__ + ': ' + str(e), file=sys.stderr)
        if not disable_warnings:
            raise e