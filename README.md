# Word Locator / Line Locator
Locates the line number of the said word from the said file. (One or all instances of the word)

Usage:
```powershell
python locate_line.py [-h] --word WORD --file FILE [--all]
```

Options:
```powershell
options:
  -h, --help   show this help message and exit
  --word WORD  Word to be searched in the wordlist
  --file FILE  Wordlist
  --all        Find all the instances of the word in the file
```

Examples
```powershell
$ python locate_line.py --word secret123 --file password.txt --all

"secret123" found in password.txt at lines 41049, 197885, 397133.

...
$ python locate_line.py --word secret123 --file password.txt

"secret123" found at 41049 in password.txt

...
$ python locate_line.py --word cr4ckb0x --file password.txt

"cr4ckb0x" does not exist in password.txt

...
$ python locate_line.py --word cr4ckb0x --file password.txt --all

"cr4ckb0x" does not exist in password.txt
```
