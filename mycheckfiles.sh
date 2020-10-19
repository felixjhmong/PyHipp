#!/bin/bash

cd /data/picasso/20181105/

ls

ls session01

find . -name "*.hkl" | grep -v -e spiketrain -e mountains | wc -l

find . -name "*.hkl" | grep -v -e spiketrain -e mountains | xargs ls -hl

find . -name "*.hkl" | grep -v -e spiketrain -e mountains

ls -hl ./session01/eyelink_24d5.hkl ./session01/rplparallel_d41d.hkl

find mountains -name "firings.mda" | wc -l

cd -
