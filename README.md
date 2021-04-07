[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]



<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/lethaiviet/ToolConverterExcelToJson">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">Converter | JSON to EXCEL & EXCEL to JSON</h3>

  <p align="center">
    The tool uses pyexcel_xlsx libs and pandas libs
    <br />
    <a href="https://github.com/lethaiviet/ToolConverterExcelToJson">View Demo</a>
    ·
    <a href="https://github.com/lethaiviet/ToolConverterExcelToJson">Report Bug</a>
    ·
    <a href="https://github.com/lethaiviet/ToolConverterExcelToJson">Request Feature</a>
  </p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

Input:
[![File excel][file-excel]]

Output:
```json
[
    {
        "firstName": "firstName_1",
        "key": "key_1",
        "lastName": "LastName_1",
        "members": [
            "members_1",
            "members_2"
        ],
        "middleName": "middleName_1",
        "name": "name_1",
        "password": "password_1",
        "roles": [
            "roles_1",
            "roles_2"
        ],
        "userName": "userName_1"
    },
    {
        "firstName": "firstName_2",
        "key": "key_2",
        "lastName": "",
        "members": [
            ""
        ],
        "middleName": "",
        "name": "name_2",
        "password": "password_2",
        "roles": [
            "roles_1",
            "roles_2"
        ],
        "userName": "userName_2"
    },
    {
        "firstName": "firstName_3",
        "key": "key_3",
        "lastName": "",
        "members": [
            ""
        ],
        "middleName": "",
        "name": "name_3",
        "password": "password_3",
        "roles": [
            "roles_1",
            "roles_3"
        ],
        "userName": "userName_3"
    }
]
```
Or vice versa
### Built With

* [pandas](https://www.marsja.se/how-to-convert-json-to-excel-python-pandas/) - The lib help to convert JSON data to an Excel file
* [pyexcel_xlsx](https://pypi.org/project/pyexcel-xlsx/) - A tiny wrapper library to read, manipulate and write data in xlsx



<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

* [Python3](https://www.python.org/downloads/)
* [Python Virtual Environments](https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/26/python-virtual-env/)
  

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/lethaiviet/ToolConverterExcelToJson.git
   ```
2. Create virtual environment
   ```sh
    cd ToolConverterExcelToJson
    00_install_env.bat
   ```
3. Active virtual environment
   ```sh
    01_active_env.bat
   ```
4. Install dependency libraries on the virtual environment
   ```sh
    02_install_libs.bat
   ```

NOTE: if you want to create Executable from Python Script
   ```sh
    03_create_app.bat
   ```
  After running successfully, the exe output in the path `ToolConverterExcelToJson\dist\ConverterExcelAndJson.exe`
<!-- USAGE EXAMPLES -->
## Usage
If you have `ConverterExcelAndJson.exe`, you just need to drag the file (.json or .excel) into `ConverterExcelAndJson.exe` to can get the desired file (.excel or .json).

Or run `ToolConverterExcelToJson\ConverterExcelAndJson.py` directly.
    ```bat
      01_active_env.bat
      python ConverterExcelAndJson.py dataTest\Book1.xlsx
    ```
<!-- CONTACT -->
## Contact
Project Link: [https://github.com/lethaiviet/ToolConverterExcelToJson](https://github.com/lethaiviet/ToolConverterExcelToJson)



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/lethaiviet/ToolConverterExcelToJson.svg?style=for-the-badge
[contributors-url]: https://github.com/lethaiviet/ToolConverterExcelToJson/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/lethaiviet/ToolConverterExcelToJson.svg?style=for-the-badge
[forks-url]: https://github.com/lethaiviet/ToolConverterExcelToJson/graphs/network/members
[stars-shield]: https://img.shields.io/github/stars/lethaiviet/ToolConverterExcelToJson.svg?style=for-the-badge
[stars-url]: https://github.com/lethaiviet/ToolConverterExcelToJson/graphs/stargazers
[issues-shield]: https://img.shields.io/github/issues/lethaiviet/ToolConverterExcelToJson.svg?style=for-the-badge
[issues-url]: https://github.com/lethaiviet/ToolConverterExcelToJson/graphs/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]:https://github.com/lethaiviet/ToolConverterExcelToJson/graphs/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[file-excel]: images/image01.PNG
