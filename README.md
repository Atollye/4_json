# Prettify JSON

This script allows you to open a JSON file and print out its contents to the console in a human-readable form
(i.e. with newlines, left indents for each data level and extra spaces between words).

## Usage

Clone or download the project to your computer. Unzip the archive, if necessary. Run the file pprint_json.py in your console, specifying the path to the file with json as the first argument.

Example of script launch on Linux, Python 3.5:

```bash

$ python pprint_json.py <full path to JSON file>
{
    "properties": {
        "Attributes": {
            "AdmArea": "Юго-Восточный административный округ",
            "District": "район Кузьминки",
            "global_id": 171714335,
            "ClarificationOfWorkingHours": null,
            "TypeService": "реализация продовольственных товаров",
            "IsNetObject": "нет",
            "Address": "Волгоградский проспект, дом 106, корпус 1",
            "WorkingHours": [
                {
                    "Hours": "09:00-23:00",
                    "DayOfWeek": "понедельник"
                },
...
                {
                    "Hours": "09:00-23:00",
                    "DayOfWeek": "воскресенье"
                }
            ],
            "PublicPhone": [
                {
                    "PublicPhone": "нет телефона"
                }
            ],
            "OperatingCompany": null,
            "Name": "Крафтовое пиво"
        }, ...
```
## Possible problems
1. This version of the project works only with files on your local computer (not with links to JSON files in the Web).
2. It reads files using your defualt system encoding (utf-8 for Debian Linux, cp1251 for Windows,mac_cyrillic for Mac). 
If a JSON file encoding does not match your system encoding, Cyrillic letters may not be displayed correctly.

## Project Goals
The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
