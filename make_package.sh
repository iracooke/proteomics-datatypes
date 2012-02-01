#!/bin/bash

rm protk-toolshed.tar.bz2
tar --exclude=.hg/ --exclude=tool-data/datatypes_conf.xml --exclude=lib/ --exclude=display_applications --exclude=protk-toolshed.tar -cvf  protk-toolshed.tar ./
bzip2 protk-toolshed.tar
