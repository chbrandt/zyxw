#-*- coding:utf-8 -*-

_DESCRIPTION = """Search (USVAO) registry for services."""

import logging

def run(args,desc=None):
    """
    """
    from .run import search
    from eada import vo as vos

    if not desc:
        desc = _DESCRIPTION
    arguments = RegArguments(desc)

    table = search(arguments,vos.registry.search)

    return table


from .arguments import Arguments
from ..constants import WAVEBANDS,SERVICES

class RegArguments(Arguments):
    def __init__(self,description):
        super(RegArguments,self).__init__(description)

    def init_arguments(self):
        super(RegArguments,self).init_arguments()
        self.parser.add_argument('service',
                                choices=SERVICES.keys(),
                                help='Service (resource) to search for.')

        self.parser.add_argument('--wavebands',
                                choices=WAVEBANDS.keys(),
                                const=None, default=None,
                                action='store',
                                help='Waveband of interest to search for.')

        self.parser.add_argument('--keywords',
                                const=None, default=None,
                                action='store',
                                help='Keywords to be found (anywhere) in resources.')

        self.parser.add_argument('--ucds',
                                const=None, default=None,
                                action='store',
                                help='UCDs to be found in resources.')

        self.parser.add_argument('--units',
                                const=None, default=None,
                                action='store',
                                help='Units to be found in resources.')

    def parse_arguments(self,args):
        super(RegArguments,self).parse_arguments(args)

# class Registry(object):
#     def __init__(self,description=None):
#         if not description:
#             description = _DESCRIPTION
#         self.init_arguments(description)
#
#     def init_arguments(self,desc):
#         #from registry import RegArguments
#         self.arguments = RegArguments(desc)
#
#     def search(self,args):
#         from eada import vo as vos
#         self.arguments.parse_arguments(args)
#         args = self.arguments.dargs()
#         wbs = args.get('wavebands')
#         kws = args.get('keywords')
#         ucds = args.get('ucds')
#         unts = args.get('units')
#         catalogues = vos.registry.search(wbs, kws, ucds, unts)
