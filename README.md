## Thinkorswim Statement Converter for Trade Monitoring
This Python CLI tool converts Thinkorswim account csv statements into a more manageable format for trade analysis.  It transforms complex, difficult-to-parse statements into clear, structured data, enabling you to focus on what matters most: understanding your trading performance.


Turn this:

![alt text](image_docs\image.png)

Into this:

![alt text](image_docs\image-1.png)


## Usage
### With UV
1. Run UV Sync
    ```
    uv sync
    ```

2. Run example file with python
    ```
    python statement-converter.py 2022-06-21-AccountStatement.csv
    ```

### Without UV installed
1. install the dependencies
    ```
    pip install -r requirements.txt
    ```

2. Run example file with python
    ```
    python statement-converter.py 2022-06-21-AccountStatement.csv
    ```

A new file with the converted data format will then be created in the [converted](converted) folder

## How to download statements from Thinkorswim
1. Head over to the "monitor" tab then  "Account Statements"

    ![alt text](image.png)

2. click on menu icon on the very left and choose "export to file"

    ![alt text](image-1.png)