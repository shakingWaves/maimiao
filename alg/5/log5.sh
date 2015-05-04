#!/bin/sh
awk '{print $1}' log.txt |sort|uniq 
