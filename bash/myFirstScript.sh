#!/bin/bash

a=$(ip a | grep 'noprefixroute dynamic ens192' | awk '{print $2}')
echo "My IP is $a"
