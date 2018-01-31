# $Id: Makefile,v 1.6 2010/02/16 13:49:02 lukas Exp $
#

PYTHON=`which python`
DESTDIR=/
BUILDIR=$(CURDIR)/debian/luma
RPMROOT=$(HOME)/rpmbuild
RPMSOURCE=$(RPMROOT)/SOURCES
RPMSRCRPM=$(RPMROOT)/SRPMS
RPMBINRPM=$(RPMROOT)/RPMS/noarch
VERSION=$(shell python -c "import luma; print luma.VERSION")

all:
	@echo "make build - Build everything needed to install"
	@echo "make install - Install on local system"
	@echo "make clean - Get rid of scratch and byte files"
	@echo "make source - Create source package"
	@echo "make buildrpm - Generate a rpm package"
	@echo "make builddeb - Generate a deb package"

build:
	# build

source:
	# source

install:
	# install

buildrpm:
	tar zcf ${RPMSOURCE}/luma-${VERSION}.tar.gz --exclude ".git/*" --exclude ".gitignore" --exclude .git --exclude "*.swp*" --transform="s,\./,luma-${VERSION}/,g" .
	rpmbuild -ba setup/rpm/luma.spec

builddeb:
	# build a .deb package

clean:	
	# clean up
