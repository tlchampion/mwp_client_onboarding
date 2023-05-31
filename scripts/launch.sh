#!/bin/bash

while true; do

read -p "Did you either leave the solidity contract as-is or, if you modified it, did you copy the new ABI configuration to the abi.txt file as instructed? (Y/n)" yn

case $yn in
	[yY] ) echo OK, proceeding;
		break;;
	[nN] ) echo Aborting launch. Please update the /solidity_contract/abi.txt file with the updated ABI configuration information and rerun this launch script;
		exit;;
	* ) echo invalid response;;
esac

done

while true; do

read -p "Did you activate a compatable python environment? (Y/n)" yn

case $yn in
	[yY] ) echo OK, proceeding;
		break;;
	[nN] ) echo Aborting launch. Please activate correct python environment and rerun this launch script;
		exit;;
	* ) echo invalid response;;
esac

done


python ./setup_minimum.py

(trap 'kill 0' SIGINT; (cd ../streamlit && streamlit run ./streamlit_interfaces.py --server.headless true --server.port 8501) & (cd ../panel_dashboard && panel serve --port 9501 mywealthpath.py) & (cd ../react && PORT=3000 npm run start) & wait)
# streamlit run ./streamlit/streamlit_interfaces.py --server.headless true --server.port 8501
# panel serve --port 9501 mywealthpath.py
# PORT=3000 npm --prefix ./react/ run start

