import ast
from typing import Iterable, TYPE_CHECKING

if TYPE_CHECKING:
    from generator.parser.types.domain import Domain


def _imports():
    return [
        ast.ImportFrom(
            module='dataclasses',
            names=[
                ast.alias(
                    name='dataclass'
                )
            ],
            render_context={
                'lines_before': 2,
            }
        ),
        ast.ImportFrom(
            module='typing',
            names=[
                ast.alias(
                    name='TYPE_CHECKING'
                )
            ]
        )
    ]


def _type_checked_imports(domains: Iterable['Domain']):
    aliases = []

    for domain in domains:
        aliases.append(
            ast.alias(
                domain.domain.snake_case
            )
        )

    return [
        ast.ImportFrom(
            module='cdp.target.target',
            names=[
                ast.alias('Target')
            ]
        ),
        ast.ImportFrom(
            module='cdp.generated.types',
            names=aliases
        )
    ]


def _domain():
    pass


def generate(domains: Iterable['Domain']):
    root = ast.Module(
        body=[]
    )

    domains_definition = ast.ClassDef(
        name='Domains',
        body=[
            ast.AnnAssign(
                target=ast.Name('ws_target'),
                annotation=ast.Constant('Target'),
            )
        ],
        decorator_list=[
            ast.Name('dataclass')
        ],
        render_context={
            'lines_before': 2,
        }
    )

    root.body.extend(_imports())
    root.body.append(
        ast.If(
            test=ast.Name('TYPE_CHECKING'),
            body=_type_checked_imports(domains),
            render_context={
                'lines_before': 1,
            }
        )
    )
    root.body.append(domains_definition)

    return root
