#+++++++++++++++++++++++++++++++++++++++++++++++#
#                                               #
#   MAKEFILE                                    #
#   --------                                    #
#                                               #
#   Contains commands for setting up a          #
#   development environment, linting,           #
#   running test, and packaging.                #
#                                               #
#   - develop:    creates a development         #
#                 environment using `venv`.     #
#                                               #
#   - test:       runs all tests with py.test   #
#                 and reports coverage.         #
#                                               #
#   - build:      builds docker images, CLI,    #
#                 and the web UI.               #
#                                               #
#   - clean:      cleans build directory.       #
#                                               #
#+++++++++++++++++++++++++++++++++++++++++++++++#

all:
	streamlit run app/app.py


dev:
	streamlit run app/app.py
	