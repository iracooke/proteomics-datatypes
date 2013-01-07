#!/bin/bash

rm -f package.tar.bz2
tar --exclude=.DS_Store --exclude=.hgcheck --exclude=package.tar --exclude=.hg/ --exclude=make_package.sh --exclude=README.md -cvf package.tar ./ 
bzip2 package.tar
