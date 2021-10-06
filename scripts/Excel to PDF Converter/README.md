## Excel to PDF Converter

<h4>Description:</h4> This Python script converts all `.csv`/Excel sheets into PDF files.

<br>

<h2>Python Script</h2>
<br>
Requirements:
<br>


```bash
pip install pywin32

```

<h2>Steps:</h2>

1. Create a COM Object Using Dispatch() method.<br>
2. It has to read the Excel file pass “Excel.Application” inside the Dispatch method.<br>
3. Pass Excel file path. <br>
4. Convert it into PDF using the ExportAsFixedFormat() method.<br>
<br>

ExportAsFixedFormat():- The ExportAsFixedFormat method is used to publish a workbook in either PDF or XPS format.

Syntax:

ExportAsFixedFormat (Type, FileName, Quality, IncludeDocProperties, IgnorePrintAreas, From, To, 

OpenAfterPublish, FixedFormatExtClassPtr)
<br>
Download the Excel file <a href="https://github.com/Rajspeaks/General-Purpose-Scripts/blob/main/scripts/Excel%20to%20PDF%20Converter/Excel.xlsx">HERE</a>
<br>

<h3>Input:</h3>
<br>
<img src="https://github.com/Rajspeaks/General-Purpose-Scripts/blob/main/scripts/Excel%20to%20PDF%20Converter/images/Screenshot1.png" height="300px" width="600px">

<br>


<h3>Output:</h3>
<br>
<img src="https://github.com/Rajspeaks/General-Purpose-Scripts/blob/main/scripts/Excel%20to%20PDF%20Converter/images/Screenshot2.png" height="300px" width="600px">

<br>



