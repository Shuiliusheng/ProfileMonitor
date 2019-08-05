1. `analyze.py` read `MonitedSitesAndconfig.txt` to decide how to monitor given website.
2. Each line in `MonitedSitesAndconfig.txt` is a website you want to monitor, the format is `website type paramiters`
   1. type1: `IDS`, monitor the tag areas, their id is given in paramiters
   2. type2:`CLASSES`, similar to IDS, but given tag's class
   3. type3:`KEYS`, this type is not elaborated, simply monitor the 2 upper level area of the area contains keywords given in paramiters.
3. `crawlers.py` defines how to get data of target website's area.
4. `parser.py` parse remove html tags, and remain plain text only.
5. `differ.py` return the differences compare with last time. 
6. `send_email.py` send the differences to peoples who care about the results. If none monited websites changes, send **No changes**.