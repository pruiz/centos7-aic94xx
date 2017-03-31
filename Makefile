##
## A sample Makefile for building driver disks
##

KVERSIONS := $(shell \
		if [ -f kversions ]; \
		then \
			cat kversions | sed 's/\([^\#]*\)\#.*/\1/' ; \
		else \
			uname -r ; \
		fi)
KARCH := $(shell uname -m)

SUBDIRS := aic94xx
FSTYPE=ext2

SU=/bin/su

CREATEREPO=/usr/bin/createrepo

TOPDIR := $(shell /bin/pwd)

.PHONY: all

all: diskiso
#all: sources diskiso
#all: sources diskimg diskiso

include Build.rules
