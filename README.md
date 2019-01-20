# how
Hands on Workshops helper Command-Line Interface tool

This tools offer 2 modes of operation:
* Either you only `build` the RST file content (result will be in `_build` folder at the root of your local git repo)
* Or you want to see the results `live` and you open your local browser to `http://localhost:8000`

Tested with:

* MacOSX Sierra (20/01/2019)

## Pre-requisites
* You need to have `docker` installed

## Installation

Download the helper script with wget and enable execution

```shell
wget "https://raw.githubusercontent.com/shuguet/how/master/how" -O /usr/local/bin/how && chmod +x /usr/local/bin/how
```

## Notes
Make sure `/usr/local/bin` is in your `PATH` environment variable
