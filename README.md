# Prettify JSON

This script allows you to open a JSON file and print out its content to the console in a human-readable form
(i.e. with newlines, left indents for each level of data structure and extra spaces between words).

## Usage

Clone or download the project to your computer. Run the file *pprint_json.py* in your console, giving a path to a JSON file as the first argument.

*Example of script launch on Linux, Python 3.5:*

```
$ python pprint_json.py <full path to JSON file>

{
    "properties": {
        "RowId": "243b42c4-294d-451e-919b-0d65b9811c84",
        "ReleaseNumber": 2,
        "VersionNumber": 2,
        "DatasetId": 1796,
        "Attributes": {
            "Address": "город Зеленоград, корпус 315",
            "OperatingCompany": null,
            "District": "район Савёлки",
            "global_id": 281494735,
            "Name": "Гудсон бар",
            "AdmArea": "Зеленоградский административный округ",
            "SeatsCount": 30,
            "PublicPhone": [
                {
                    "PublicPhone": "(499) 740-97-58"
                }
            ],
            "IsNetObject": "нет",
            "SocialPrivileges": "нет"
        }
    },
    "type": "Feature",
    "geometry": {
        "type": "Point",
        "coordinates": [
            37.744234974114,
            55.917568731248
        ]
    }, ....
```
## Restrictions of this version of the script
1. This version of the script works only with files on your local computer (not with links to JSON files on the Web).
2. It reads files using your defualt system encoding (utf-8 for Debian Linux, cp1251 for Windows, mac_cyrillic for Mac). If a JSON file encoding does not match your system encoding, Cyrillic letters may not be displayed correctly.

## Project Goals
The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
