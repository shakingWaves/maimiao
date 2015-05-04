#!/bin/sh
who | cut -d ' ' -f 1 |sort|uniq
