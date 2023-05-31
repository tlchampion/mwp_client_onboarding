# Contents

This folder contains setup and launch scripts for the MyWealthPlah applications. The following scripts are provided:

setup.py: a script using prompts to obtain the necessary information to create configuration files for the node.js website and streamlit application

setup_minimum.py: a condensed version of the setup.py script that is launched by the launch.sh script. This script is not intended to be used manually

launch.sh: a bash script that will call setup_minimum.py script to obtain run-time specific variables needed for the applications to function. The three applications are then launched with a predetermined IP address assigned to each one.


## Usage Instructions

### Manual Setup
The setup.py script can be run if it is necessary to manually launch each individual application, such as if a user-defined IP address must be used.  The script can be launched by using the following command at a terminal prompt, being sure a compatable python environment has been activated.

```
python setup.py
```

The script will ask a number of questions in order to properly setup the configuration files used by the applications.


### Auto-Launch

The launch.sh script will manage the setup and launching of the three applications, using pre-defined IP addresses. Please see the project's root-level [README](../README.md) for details on those addresses.

The script may be launched from a terminal prompt as follows. Windows users should be certain to be using a bash-compatable terminal application:

```
bash launch.sh
```

The script will ask a number of questions in order to setup the configuration files needed for the applications to run. 

Once done with the applications, they can all be terminated by issueing a CTRL-C command in the window this script was launched from.