 [![Code of Conduct](https://img.shields.io/badge/%E2%9D%A4-code%20of%20conduct-blue.svg?style=flat)](https://github.com/edgi-govdata-archiving/overview/blob/main/CONDUCT.md)

# CD-Report-Spanish
Based on the EDGI Repo Guidelines at https://github.com/edgi-govdata-archiving/overview/blob/main/repo_guidelines.md

This repository is contains a Spanish-language version of the congressional report card project, found in the CD-report repository.

# How to start contributing to this repo
* Some files to not check into this repository
  - The .png files in the CD_Dirs folder that are generated when the .Rmd markdown are run.
  - The .html or .pdf files in the New folder that are generated.
* Developer setup
  - The developer will need R Studio and a bash command-line shell.
  - The process for generating reports is the same as in the EEW-Report-Making repository's README.md.
  
# How to Use This Repository

#### Generate R markdown .Rmd files for each CD

The CSVs listed in the cd_todos directory files are used to generate batches of the R markdown .Rmd files that create the report cards.

From the reportcards directory, the make_sedfiles.py script creates a file of replacement editing commands to be run against the template .Rmd file to make the .Rmd for the CD.  This script also creates the make_reports.sh bash shell script the calls upon the sedfiles to do the editing for each CD.

A state_names.csv file in the cd_todos directory is also used to map the state/CD from the cds_todo_X.csv files to the full possessive state name, e.g. AL,1 --> Alabama's 1st.

  ../cd_todos/cd_todos_1.csv
  ../cd_todos/state_names_es.csv   ---> make_sedfiles.py   ---> reportcards/SEDs/sedfile_AL1.txt, etc.
  
  VA4_2020_es.Rmd
  SEDs/sedfile_XXX.txt   ---> make_reports.sh   ---> reportcards/New/AL1_2020.Rmd, etc.
  
#### Create the HTML and PDF report cards from .Rmd files

The R Markdown files in the reportcards/New directory are inputs for the runreports.R script.  For every .Rmd file
it finds in the reportcards/New directory it creates an HTML and PDF report card.
  
#### Directory structure for making report cards
```
CD-Report-Spanish
  |- runreports.R
  |
  |- cds_todo
       |
       |- cds_todo_1.csv
          ...
  |
  |- reportcards
       |
       |- make_reports_es.sh
       |- make_sedfiles_es.py
       |- VA4_template_es.Rmd
          ...
          |- New  (Empty until make_reports.sh runs.)
              |- FL12_2020_es.Rmd
                 ...
          |- SEDs  (Empty until make_sedfiles.py runs.)
              |- FL12_es.txt
                 ...
          |- Outputs  (Empty until runreports.R runs. )
              |- FL12_2020_es.html
              |- FL12_2020_es.pdf
                 ...
  |
  |- CD_Dirs
       |
       |- AL1
            |
            |- active-facilities_All_pg3_AL-1-102320.csv
               ...
       |-  ...
  |
  |- CD_maps
       |
       |- AL1_map.png
          ...
  |
  |- CD_images
       |
       |- AL1_rep.jpeg
          ...
  ```        
  
* This project is part of the EPA Enforcement Watch (EEW), at slack channel eew_coordination.

**Suggestions for additional components of Readmes:**
* A "How to use" section if the repo's project is a tool or website
* A link to the [good-first-issue](https://github.com/issues?q=is%3Aopen+is%3Aissue+label%3Agood-first-issue+user%3Aedgi-govdata-archiving) label (this link across EDGI, or a specific link for the repo)
* Highlight "ready" label on issues to mean "this is an issue that is ready to work on and needs an owner"
* Additional badges at the top, such as code quality indicators
* "[All contributors](https://github.com/kentcdodds/all-contributors#emoji-key)" listing, following these additional guidelines (example: [web-monitoring-db contributors list](https://github.com/edgi-govdata-archiving/web-monitoring-db#contributors)):
  - Compact representation without avatars (less visual noise; easier to focus on contributions)
  - Icons are links with title attributes (accessibility)
  - Alphabetical order by surname/name/username (to eliminate implied ranking)
  - Presence in the list (and the name used) is optional and up to the contributor (not everyone wants to be listed — we offer, but do not add unless someone explicitly says yes)

**When using this template, please look through all of the files to ensure they apply to the new repo.**

---

## License & Copyright

Copyright (C) <year> Environmental Data and Governance Initiative (EDGI)
This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, version 3.0.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

See the [`LICENSE`](/LICENSE) file for details.
