#
# Makefile for the Chevah's G.E.C.K.
#

ifeq "$(MSYSTEM)" "MINGW32"
       BASE_PATH='build/venv/Scripts'
       PYTHON='build/venv/python.exe'
else
       BASE_PATH='build/venv/bin'
       PYTHON='build/venv/bin/python'
endif

all: generate	

env:
	@if [ ! -d "build/venv" ]; then ./paver.sh venv build/venv; fi
	@$(PYTHON) -m pip install sphinx sphinx-autobuild sphinx_rtd_theme


generate:
	$(BASE_PATH)/sphinx-build -b html -j 2 -n docs/ build/html
	@echo "Open the result in a browser: file://$$PWD/build/html/index.html"

test:
	rm -f build/errors
	$(BASE_PATH)/sphinx-build -b html -Ean -j 2 -w build/errors \
		docs/ build/html
	if [ -s build/errors ]; then false ; fi

clean:
	@rm -rf build
