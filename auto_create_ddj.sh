#!/bin/bash -
#===============================================================================
#
#          FILE: auto_create_ddj.sh
#
#         USAGE: ./auto_create_ddj.sh
#
#   DESCRIPTION: 
#
#       OPTIONS: ---
#  REQUIREMENTS: ---
#          BUGS: ---
#         NOTES: ---
#        AUTHOR: YOUR NAME (), 
#  ORGANIZATION: 
#       CREATED: 01/08/2025 12:02:03 PM
#      REVISION:  ---
#===============================================================================

set -o nounset                                  # Treat unset variables as an error
USERNAME='ddjima'
DOMAIN='ddjima.com'
BASE_URL='https:\/\/www.$(DOMAIN)\/'
CURRENT_ICON_PATH=./assets/media/icon.png
UNAME_S := $(shell uname -s)
ifeq ($(UNAME_S),Darwin)
	BROWSER=/Applications/Firefox.app/Contents/MacOS/firefox-bin
endif
ifeq ($(UNAME_S),Linux)
	BROWSER=firefox
endif

.PHONY: build test clean deploy setBaseUrl setLogo

build:
	hugo -D

test:
	hugo server -D &
	$(BROWSER) --new-tab http://localhost:1313/

clean:
	@rm -rf public

deploy:
	@echo 'Make sure BASE_URL is correct.'
	rsync -avz --delete public/ $(USERNAME)@moons.$(DOMAIN):~/public_html

setBaseUrl:
	sed -i "s/baseURL:.*/baseURL: $(BASE_URL)/g" ./config/_default/config.yaml

setLogo:
	@cp $(CURRENT_ICON_PATH) ./assets/media/icon.png

updatePublications:
	academic --overwrite import --bibtex ./static/CV/publications.bib

