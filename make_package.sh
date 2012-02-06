#!/bin/bash

rm protk-toolshed.tar.bz2
tar --exclude=.hg/ --exclude=tool-data/datatypes_conf.xml --exclude=lib/ --exclude=display_applications --exclude=protk-toolshed.tar --exclude=make_package.sh --exclude=README.md -cvf  protk-toolshed.tar ./
bzip2 protk-toolshed.tar
