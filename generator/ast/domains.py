import ast

from generator.parser.types import Protocol


def _generate_imports(protocols: list[Protocol]):
    imports = [
        ast.ImportFrom(
            module='dataclasses',
            names=[
                ast.alias('dataclass'),
                ast.alias('field')
            ],
        ),
        ast.ImportFrom(
            module='typing',
            names=[
                ast.alias('TYPE_CHECKING')
            ]
        )
    ]

    for protocol in protocols:
        for domain in protocol.domains:
            imports.append(
                ast.ImportFrom(
                    module=f'cdp.domains.{domain.domain_snake_case}.domain',
                    names=[
                        ast.alias(domain.domain)
                    ],
                    level=0
                )
            )

    return imports


def _generate_class_definition(protocols: list[Protocol]):
    root = ast.ClassDef(
        name='Domains',
        bases=[],
        keywords=[],
        body=[
            ast.AnnAssign(
                target=ast.Name('_target'),
                annotation=ast.Constant('_Target'),
            )
        ],
        decorator_list=[
            ast.Name('dataclass')
        ],
        render_context={
            'lines_before': 2
        }
    )

    for protocol in protocols:
        for domain in protocol.domains:
            root.body.append(
                ast.AnnAssign(
                    target=ast.Name(domain.domain_snake_case),
                    annotation=ast.Name(domain.domain),
                    value=ast.Call(
                        func=ast.Name('field'),
                        keywords=[
                            ast.keyword(
                                arg='init',
                                value=ast.Constant(False)
                            )
                        ],
                        render_context={
                            'expand': True
                        }
                    ),
                    simple=1
                )
            )

    post_init = ast.FunctionDef(
        name='__post_init__',
        args=ast.arguments(
            args=[
                ast.arg(
                    arg='self'
                )
            ]
        ),
        body=[],
        decorator_list=[],
        render_context={
            'lines_before': 1
        }
    )

    for protocol in protocols:
        for domain in protocol.domains:
            post_init.body.append(
                ast.Assign(
                    targets=[
                        ast.Attribute(
                            value=ast.Name('self'),
                            attr=domain.domain_snake_case
                        )
                    ],
                    value=ast.Call(
                        func=ast.Name(domain.domain),
                        args=[
                            ast.Attribute(
                                value=ast.Name('self'),
                                attr='_target'
                            )
                        ],
                        render_context={
                            'expand': True
                        }
                    )
                )
            )

    root.body.append(post_init)

    return root


def generate(protocols: list[Protocol]):
    root = ast.Module(
        body=[]
    )

    if imports := _generate_imports(protocols):
        root.body.extend(imports)

    root.body.append(
        ast.If(
            test=ast.Name(
                id='TYPE_CHECKING',
                ctx=ast.Load()
            ),
            body=[
                ast.ImportFrom(
                    module='cdp.target.target',
                    names=[
                        ast.alias(
                            name='Target',
                            asname='_Target'
                        )
                    ],
                )
            ]
        )
    )

    if class_definition := _generate_class_definition(protocols):
        root.body.append(class_definition)

    return root
