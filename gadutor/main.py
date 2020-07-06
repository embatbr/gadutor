# -*- coding: utf-8 -*-

import sys

import bots
from gadizator import run as gadizator_run


if __name__ == '__main__':
    args = sys.argv[1:]

    botname = args[0]

    botmodule = getattr(bots, botname)
    botmodule.main(gadizator_run)
