# catchhatch
CatchHatch - Pokemon Go Journal OCR and analytics

## Installation

* assumes Python 3.5 (because you should use it anyway) and a Linux platform (probably works similarly on Mac), and anaconda installed
* Will create a fresh conda environment
* Install `tesseract` for your system, see [here](https://github.com/tesseract-ocr/tesseract/wiki), e.g. in Ubuntu do `sudo apt-get install tesseract-ocr`
* You will also need to install `imagemagick`, see e.g. [here](http://tecadmin.net/install-imagemagick-on-linux/)

```bash
conda create -n catch python=3 pandas
source activate catch
```

