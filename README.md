# LabelStoma
LabelStoma is a graphical image tool for automatically detecting stomata in images. In addition, LabelStoma also provides the necessary tools to correct the detections. LabelStoma is based on the [LabelImg tool](https://github.com/tzutalin/labelImg).

![TestTimeAugmentation](imagen/prueba1.png)

## Installation and Requirements

LabelStoma can be run both on Windows and Linux. 

### Installation Windows:
1. Download the [labelStoma](https://github.com/ancasag/labelStoma/releases/download/v1.0/labelStoma.zip) zip file.
2. Unzip the downloaded file.
3. Execute labelStoma.exe.

### Installation Linux:
This tool requires Python 3.6 and Qt5 and the packages listed in the ```requirements.txt``` file.

1. Clone this repository.
2. Install the necessary dependencies.

```bash
sudo apt-get install pyqt5-dev-tools
pip3 install -r requirements.txt
make qt5py3
```
3. Run labelstoma:
```bash
python3 labelStoma.py
```

## Hotkeys
|          |                                |
|----------|--------------------------------|
| Ctrl + o | Open a image                   |
| Ctrl + u | Open a set of images           |
| Ctrl + q | Close the app                  |
| Ctrl + w | Close the image                |
| z        | Detect stomata                 |
| e        | Generate excel                 |
| r        | Create a new stoma detection   |
| w        | Create a new surface detection |
| l        | Create a new scale detection   |
| del      | Delete the selected rect box   |


## Acknowledgments
This work was partially supported by Ministerio de Economía y Competitividad [MTM2017-88804-P], Ministerio de Ciencia, Innovación y Universidades [RTC-2017-6640-7], and Agencia de Desarrollo Económico de La Rioja [2017-I-IDD-00018].


