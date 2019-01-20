#!/usr/bin/env python
import os
import logging
import argparse
import textwrap

SOURCE_DIR = "/wd"
OUTPUT_DIR = "/wd/_build"
PIPREQS_FILE = "pipreqs.txt"

logging.basicConfig(format='%(asctime)s %(message)s')

# Install required packages through pip
def install_pip_reqs():
    os.system(f"pip install --no-cache-dir -r {SOURCE_DIR.rstrip('/')}/{PIPREQS_FILE}")

# Build mode
def mode_build(args):
    # install_pip_reqs()
    os.system(f"sphinx-build {SOURCE_DIR} {OUTPUT_DIR}")

# Live mode
def mode_live(args):
    # install_pip_reqs()
    os.system(f"sphinx-autobuild -H 0.0.0.0 {SOURCE_DIR} {OUTPUT_DIR}")

# map for the different modes of operation
modes = {"BUILD" : mode_build,
         "LIVE" : mode_live,
}

parser = argparse.ArgumentParser(prog="how",
                                 formatter_class=argparse.RawDescriptionHelpFormatter,
                                 description=textwrap.dedent(
'''Hands on Workshop CLI helper tool
---------------------------------

If you run in build mode, the resulting html files will be in the `_build` subfolder.

If you run in live mode, a webserver will be exposed on port 8000.
You can access that webserver from here: http://localhost:8000

'''))
parser.add_argument("mode", help="mode of operation, \"build\" or \"live\"")
# parser.add_argument("-p", "--pip", help="read the specifid pipreqs file and install additional pre-reqs, if any.\n" \
#                                         "NOTE: The docker image should already contain all necessary python libraries")
parser.add_argument("-f", "--force", help="force building even if output directory is not empty",
                    action="store_true")
args = parser.parse_args()

# Check if we have a valid execution mode defined
if args.mode and args.mode.upper() in modes:
    # Check if SOURCE_DIR is a mountpoint as we need something to build
    if not os.path.ismount(SOURCE_DIR):
        logging.error(f"Error: {SOURCE_DIR} is not a mountpoint, nothing to build. Exiting.")
        exit()
    else:
        pass

    # Check if OUTPUT_DIR is empty
    if os.path.exists(OUTPUT_DIR) and os.path.isdir(OUTPUT_DIR):
        if os.listdir(OUTPUT_DIR) and not args.force:
            logging.error(f"Error: Output directory ({OUTPUT_DIR}) is not empty.")
        else:
            # Execute whatever mode we're in:
            modes[args.mode.upper()](args)
    else:
        logging.error(f"Error: Output directory ({OUTPUT_DIR}) don't exists.")

else:
    logging.error(f"Error: mode '{args.mode}' unknown")
