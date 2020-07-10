# -*- coding: utf-8 -*-

import sys

import bots
import functions


if __name__ == '__main__':
    args = sys.argv[1:]

    botname = args[0]
    funcname = args[1]

    botmodule = getattr(bots, botname)
    funcmodule = getattr(functions, funcname)
    run_function = getattr(funcmodule, 'run')

    botmodule.main(run_function)
