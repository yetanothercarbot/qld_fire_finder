# Queensland Fire Finder
This program will find the closest fire to your location by using QFES' RSS feed of current bushfires.

## Running Executable (Recommended)
For normal users, the executable can be downloaded from the releases tab at the top. Only Windows binaries are provided.

Download the file to a folder of your choice and double-click to run. It will guide you through setup (which consists of finding your current position) and then display the closest fire.

## Running Script
If you have Python installed, or you are running MacOS or Linux, it is recommended to run the script:

### Requirements:
Fire Finder requires Python3, and the BeautifulSoup 4 and requests modules:
```shell
pip3 install BeautifulSoup4 requests lxml # Linux install
```

```shell
py -3 -m pip install BeautifulSoup4 requests lxml # Windows install
```
### Running
In a terminal window, run:
```shell
python3 fire_finder.py
```
and then follow the prompts.

## License
Queensland Fire Finder is licensed under the AGPLv3. This means you are permitted to modify and redistribute but you must include the same license and make your changes open-source too. It also means that **serving over the network also requires open-sourcing**.
