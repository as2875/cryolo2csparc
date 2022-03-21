# cryolo2csparc

This is a small Python script that joins a set of STAR files produced by the crYOLO particle picking platform into a single STAR file which can be recognised by cryoSPARC. Note that to import particles into cryoSPARC you must previously have imported the micrographs.

```
usage: cryolo2csparc.py [-h] [--cryolo PATTERN] [--output OUTPUT] [--doseweighted]

optional arguments:
  -h, --help        show this help message and exit
  --cryolo PATTERN  STAR files written by crYOLO
  --output OUTPUT   Location of output STAR file
  --doseweighted    Whether to append '_doseweighted' to filenames
```
