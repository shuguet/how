# how
Hands on Workshops helper Command-Line Interface tool

This tools offer 2 modes of operation:
* Either you only `build` the RST file content (result will be in `_build` folder at the root of your local git repo)
* Or you want to see the results `live` and you open your local browser to `http://localhost:8000`

Tested with:

* MacOSX Sierra (20/01/2019)

## usage
```shell
usage: how [-h] [-f] mode

Hands on Workshop CLI helper tool
---------------------------------

If you run in build mode, the resulting html files will be in the `_build` subfolder.

If you run in live mode, a webserver will be exposed on port 8000.
You can access that webserver from here: http://localhost:8000

positional arguments:
  mode         mode of operation, "build" or "live"

optional arguments:
  -h, --help   show this help message and exit
  -f, --force  force building even if output directory is not empty
```

## Pre-requisites
* You need to have `docker` installed

## Installation

Download the helper script with wget and enable execution

```shell
wget "https://raw.githubusercontent.com/shuguet/how/master/how" -O /usr/local/bin/how && chmod +x /usr/local/bin/how
```

## Notes
Make sure `/usr/local/bin` is in your `PATH` environment variable
