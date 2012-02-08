#!/bin/bash

rm protk-toolshed.tar.bz2
tar --exclude=.hg/ --exclude=protk-toolshed.tar --exclude=make_package.sh --exclude=make_package_data.sh --exclude=README.md --exclude=.hgcheck -cvf  protk-toolshed.tar ./
bzip2 protk-toolshed.tar
