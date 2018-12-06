#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os

def options(opt):
    opt.load('compiler_c')

def configure(conf):
    conf.load('compiler_c')
    conf.load('clib')

def build(bld):
    bld.load('clib')

    includes = []

    cflags = """
        -Werror=int-to-pointer-cast
        -g
        -O0
        -Werror=unused-variable
        -Werror=return-type
        -Werror=uninitialized
        -Werror=pointer-to-int-cast
    """.split()

    lib = []

    libpath = [os.getcwd()]

    # if sys.platform == 'darwin':
    #     cflags.extend("""
    #         -fcolor-diagnostics
    #         -fdiagnostics-color
    #     """.split())

    #     # Added due to El Capitan changes
    #     includes.append('/usr/local/opt/openssl/include')
    #     libpath.append('/usr/local/opt/openssl/lib')

    # elif sys.platform.startswith('linux'):
    #     cflags.extend("""
    #         -DLINUX
    #     """.split())
    #     lib.append('pthread')
    #     lib.append('rt')

    clibs = """
    """.split()

    h2o_includes = """
    """.split()

    uv_includes = """
    """.split()

    bld.program(
        source="""
        src/main.c
        """.split() + bld.clib_c_files(clibs),
        includes=['./include'] + includes + bld.clib_h_paths(clibs) + h2o_includes + uv_includes,
        target='water',
        stlibpath=['.'],
        libpath=libpath,
        lib=lib,
        cflags=cflags)

