# pandas-data-analyser
Code in python to generate some basic stats in a csv/excel file using pandas and numpy libs

## How it works?

-> **Uses the skill points add buttons image from the character screen**<br>
-> **If you are running a different game version, change the buttons.png image.**<br>
-> **It will click in a specific mouse X and Y position to add the points automatically**<br>


      ===== DATA SAMPLE (first five rows) =====
         ESTCIVIL  INSTRUCAO  FILHOES  SALÁRIO  ANO   MÊS  REGIAO
      0       1.0          1      NaN     4.00   26   3.0       1
      1       2.0          1      1.0     4.56   32  10.0       2
      2       2.0          1      2.0     5.25   36   5.0       2
      3       1.0          2      NaN     5.73   20  10.0       3
      4       1.0          1      NaN     6.26   40   7.0       3

      ===== COUNT BY COLUMN (VALID CELLS) =====
             ESTCIVIL  INSTRUCAO  FILHOES  SALÁRIO    ANO    MÊS  REGIAO
      count     29.00      32.00    17.00    32.00  32.00  30.00   32.00
      mean       1.41       1.84     1.53     9.77  34.22   5.33    2.03
      std        0.73       0.72     1.01     5.82   6.70   3.52    0.82
      min       -1.00       1.00     0.00    -1.00  20.00  -1.00    1.00
      25%        1.00       1.00     1.00     6.56  30.00   2.25    1.00
      50%        2.00       2.00     2.00     8.84  34.00   5.00    2.00
      75%        2.00       2.00     2.00    12.90  39.25   7.75    3.00
      max        2.00       3.00     3.00    23.30  48.00  11.00    3.00

      ===== MISSING DATA =====   
                 Percentage (%)  
      ESTCIVIL             9.38  
      INSTRUCAO            0.00  
      FILHOES             46.88  
      SALÁRIO              0.00  
      ANO                  0.00  
      MÊS                  6.25  
      REGIAO               0.00  

      ===== STATS BY COLUMN =====

      QTD  RANK  GRADE: ESTCIVIL 
      2.0    15    150
      1.0    12    120
      nan    3    3
      -1.0    1    10
      0.0    1    10

      QTD  RANK  GRADE: INSTRUCAO
      2    15    150
      1    11    110
      3    6    60


**NOTE**: created only as example. The data is not real.

## What this code wont do!

-> Its not for auto hunting!<br>
-> Not tested with a lot of MuOnline game versions (the screen GUI must match to work)<br>

## Install instructions

    1. Install python(> 3.8.x)
    2. pip install virtualenv
    3. Execute: virtualenv venv (or any other env name you wish)
    4. Activate the virtual env: cd venv/scripts & activate
    5. Execute: "pip install -r requirements.txt" to install the package (only one so far)

## Config instructions

    * Open the config.ini file
    * useExcelFile(boolean)  - can be true or false, its used to define if the data will be read from a csv or xlsx.
    * excelSheetName(string) - if the config above is true, you need to tell in what tab from the xlsx the data will be found.
    * invalidValueMarker(string) - it tell the code what cell value will be considered INVALID. For instance, if the cell holds a 'NA' it will be considered invalid
                                   Other values like empty string and null are also invalid for the matter.
    * rankValido/rankInvalido(int) - this is used to rate the good and bad data respectively. If the cell data is valid, it will multiply by 10. Exemple below:
    QTD  RANK  GRADE
     2    15    150

## Be happy! I`ve made this to force me use the pandas lib. :)
    EXECUTE: exec.bat ou python run.py

[Blog - rodrigoreisf.com.br](http://rodrigoreisf.com.br)
