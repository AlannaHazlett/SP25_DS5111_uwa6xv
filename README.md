# SP25_DS5111_uwa6xv
## DS5111 Software and Automation Skills Course Work
### Set Up AWS Virtual Machine
* Start by making sure the machine is up to date and run `sudo apt update` in the command line.
* Create GitHub SSH key 
	* In the command line generate the SSH key  `ssh-keygen -t ed25519 -C "your_email@example.com"`, making sure to utilize the email affiliated with your GitHub account.
	* Save the file in the appropriate directory `home/ubuntu/.ssh/id_ed25519`, this should be what is automatically populated, so you can just hit enter.
	* Optionally you can enter a passphrase that will be required for pushing and pulling. If you do not wish to have one simply press enter.
	* Change directories to `home/ubuntu/.ssh`.
	* Display the SSH key `cat id_ed25519.pub` and copy the output, including the email address. 
	* In GitHub Settings -> SSH and GPG Keys click on new SSH key button.
	* Name your SSH Key, so you remember what system it is used to connect to and paste the output from `cat id_ed25519.pub` into the Key section. 
	* Check GitHub connection with `ssh -T git@github.com` in the command line. If all went well you will see your GitHub username.  
* Set up your GitHub global configurations utilizing `setup_git_global_configs.sh` in the `scripts/` directory, making sure to enter in your GitHub email and username in the script. 
### Set Up Project
* Clone my [repo](https://github.com/AlannaHazlett/SP25_DS5111_uwa6xv) so from this point forward the instructions should be runnable directly from my scripts.
* Use the script to install chrome headless browser.  Use example.com for a quick test.
* You can quickly install package dependencies utilizing the  `requirements.txt` file. 
	* In the command line `pip install -r requirements.txt` 
* To create and update the virtual environment use `make update` from the makefile. 
* Utilize makefile to activate google headless browser to create a csv.
	* If you have not entered your virtual environment you can quickly do this with `make update` or with `source env/bin/acitvate`.
	* Then you call to create the unnormalized csv, which depends upon the html call,  `make ygainers.csv` or `make wsjgainers.csv`. You can see an example csv in my [sample_data](https://github.com/AlannaHazlett/SP25_DS5111_uwa6xv/tree/main/sample_data) directory. 
    * To create the normalized csv with the timestamp saved in the file name call `make gainers which=yahoo` or `make gainers which=wsj`. This will save the files in the collected_data directory.
* Lint all files in bin/ and tests/ with `make lint`.
* Test all files in tests/ with `make test`. This will also call `make lint` as a requirement. 
* Remove HTML or unnormalized CSV files with either `make clean ygainers` or `make clean wsjgainers`. 
* The current structure of the repository is:

```
/home/ubuntu/SP25_DS5111_uwa6xv
├── ERDiagram.md
├── LICENSE
├── PracticeMermaid.md
├── README.md
├── __pycache__
│   └── main_process.cpython-312.pyc
├── bin
│   ├── __pycache__
│   │   └── normalize_csv.cpython-312.pyc
│   ├── gainers
│   │   ├── __pycache__
│   │   │   ├── download.cpython-312.pyc
│   │   │   ├── factory.cpython-312.pyc
│   │   │   ├── process.cpython-312.pyc
│   │   │   ├── wsj.cpython-312.pyc
│   │   │   └── yahoo.cpython-312.pyc
│   │   ├── download.py
│   │   ├── factory.py
│   │   ├── process.py
│   │   ├── wsj.py
│   │   └── yahoo.py
│   └── normalize_csv.py
├── collected_data
│   ├── norm_wsjgainers2025-03-10_13:31:09.csv
│   ├── norm_wsjgainers2025-03-10_16:29:09.csv
│   ├── norm_wsjgainers2025-03-10_20:01:17.csv
│   ├── norm_wsjgainers2025-03-11_13:51:12.csv
│   ├── norm_wsjgainers2025-03-11_16:30:18.csv
│   ├── norm_wsjgainers2025-03-11_20:01:18.csv
│   ├── norm_wsjgainers2025-03-12_13:31:19.csv
│   ├── norm_wsjgainers2025-03-12_16:30:20.csv
│   ├── norm_wsjgainers2025-03-12_20:01:18.csv
│   ├── norm_wsjgainers2025-03-13_13:31:17.csv
│   ├── norm_wsjgainers2025-03-13_16:30:18.csv
│   ├── norm_wsjgainers2025-03-13_20:01:35.csv
│   ├── norm_wsjgainers2025-03-14_13:31:18.csv
│   ├── norm_wsjgainers2025-03-14_16:30:18.csv
│   ├── norm_wsjgainers2025-03-14_20:01:18.csv
│   ├── norm_ygainers2025-03-10_13:33:12.csv
│   ├── norm_ygainers2025-03-10_16:28:12.csv
│   ├── norm_ygainers2025-03-10_20:01:10.csv
│   ├── norm_ygainers2025-03-11_13:31:34.csv
│   ├── norm_ygainers2025-03-11_16:30:09.csv
│   ├── norm_ygainers2025-03-11_20:01:10.csv
│   ├── norm_ygainers2025-03-12_13:31:11.csv
│   ├── norm_ygainers2025-03-12_16:30:11.csv
│   ├── norm_ygainers2025-03-12_20:01:10.csv
│   ├── norm_ygainers2025-03-13_13:31:09.csv
│   ├── norm_ygainers2025-03-13_16:30:09.csv
│   ├── norm_ygainers2025-03-13_20:01:10.csv
│   ├── norm_ygainers2025-03-14_13:31:10.csv
│   ├── norm_ygainers2025-03-14_16:30:09.csv
│   ├── norm_ygainers2025-03-14_20:01:09.csv
│   ├── wsjgainers2025-03-10_13:31:09.csv
│   ├── wsjgainers2025-03-10_16:29:09.csv
│   ├── wsjgainers2025-03-10_20:01:17.csv
│   ├── wsjgainers2025-03-11_13:51:12.csv
│   ├── wsjgainers2025-03-11_16:30:18.csv
│   ├── wsjgainers2025-03-11_20:01:18.csv
│   ├── wsjgainers2025-03-12_13:31:19.csv
│   ├── wsjgainers2025-03-12_16:30:20.csv
│   ├── wsjgainers2025-03-12_20:01:18.csv
│   ├── wsjgainers2025-03-13_13:31:17.csv
│   ├── wsjgainers2025-03-13_16:30:18.csv
│   ├── wsjgainers2025-03-13_20:01:35.csv
│   ├── wsjgainers2025-03-14_13:31:18.csv
│   ├── wsjgainers2025-03-14_16:30:18.csv
│   ├── wsjgainers2025-03-14_20:01:18.csv
│   ├── ygainers2025-03-10_13:33:12.csv
│   ├── ygainers2025-03-10_16:28:12.csv
│   ├── ygainers2025-03-10_20:01:10.csv
│   ├── ygainers2025-03-11_13:31:34.csv
│   ├── ygainers2025-03-11_16:30:09.csv
│   ├── ygainers2025-03-11_20:01:10.csv
│   ├── ygainers2025-03-12_13:31:11.csv
│   ├── ygainers2025-03-12_16:30:11.csv
│   ├── ygainers2025-03-12_20:01:10.csv
│   ├── ygainers2025-03-13_13:31:09.csv
│   ├── ygainers2025-03-13_16:30:09.csv
│   ├── ygainers2025-03-13_20:01:10.csv
│   ├── ygainers2025-03-14_13:31:10.csv
│   ├── ygainers2025-03-14_16:30:09.csv
│   └── ygainers2025-03-14_20:01:09.csv
├── crontab.sh
├── debug.txt
├── get_gainer.py
├── google-chrome-stable_current_amd64.deb
├── main.py
├── makefile
├── projects
│   ├── gainers
│   │   ├── README.md
│   │   ├── analyses
│   │   ├── dbt_project.yml
│   │   ├── logs
│   │   │   └── dbt.log
│   │   ├── macros
│   │   ├── models
│   │   │   └── example
│   │   │       ├── ende.sql
│   │   │       ├── enfr.sql
│   │   │       ├── french.sql
│   │   │       ├── my_first_dbt_model.sql
│   │   │       ├── my_second_dbt_model.sql
│   │   │       └── schema.yml
│   │   ├── seeds
│   │   │   └── numbers.csv
│   │   ├── snapshots
│   │   ├── target
│   │   │   ├── compiled
│   │   │   │   └── gainers
│   │   │   │       └── models
│   │   │   │           └── example
│   │   │   │               ├── ende.sql
│   │   │   │               ├── enfr.sql
│   │   │   │               ├── french.sql
│   │   │   │               ├── my_first_dbt_model.sql
│   │   │   │               ├── my_second_dbt_model.sql
│   │   │   │               └── schema.yml
│   │   │   │                   ├── accepted_values_french_FR__un__deux__troi.sql
│   │   │   │                   ├── not_null_french_FR.sql
│   │   │   │                   ├── not_null_my_first_dbt_model_id.sql
│   │   │   │                   ├── not_null_my_second_dbt_model_id.sql
│   │   │   │                   ├── relationships_enfr_EN__EN__ref_ende_.sql
│   │   │   │                   ├── unique_french_FR.sql
│   │   │   │                   ├── unique_my_first_dbt_model_id.sql
│   │   │   │                   └── unique_my_second_dbt_model_id.sql
│   │   │   ├── graph.gpickle
│   │   │   ├── graph_summary.json
│   │   │   ├── manifest.json
│   │   │   ├── partial_parse.msgpack
│   │   │   ├── run
│   │   │   │   └── gainers
│   │   │   │       ├── models
│   │   │   │       │   └── example
│   │   │   │       │       ├── ende.sql
│   │   │   │       │       ├── enfr.sql
│   │   │   │       │       ├── french.sql
│   │   │   │       │       ├── my_first_dbt_model.sql
│   │   │   │       │       ├── my_second_dbt_model.sql
│   │   │   │       │       └── schema.yml
│   │   │   │       │           ├── accepted_values_french_FR__un__deux__troi.sql
│   │   │   │       │           ├── not_null_french_FR.sql
│   │   │   │       │           ├── not_null_my_first_dbt_model_id.sql
│   │   │   │       │           ├── not_null_my_second_dbt_model_id.sql
│   │   │   │       │           ├── relationships_enfr_EN__EN__ref_ende_.sql
│   │   │   │       │           ├── unique_french_FR.sql
│   │   │   │       │           ├── unique_my_first_dbt_model_id.sql
│   │   │   │       │           └── unique_my_second_dbt_model_id.sql
│   │   │   │       └── seeds
│   │   │   │           └── numbers.csv
│   │   │   ├── run_results.json
│   │   │   └── semantic_manifest.json
│   │   └── tests
│   └── logs
│       └── dbt.log
├── pylintrc
├── requirements.txt
├── sample_data
│   ├── wsjgainers.csv
│   └── ygainers.csv
├── scripts
│   ├── google-chrome-stable_current_amd64.deb
│   ├── init.sh
│   ├── install_chrome_headless.sh
│   └── setup_github_global_creds.sh
├── tests
│   ├── __pycache__
│   │   ├── test_controls.cpython-312-pytest-8.3.4.pyc
│   │   ├── test_wsj.cpython-312-pytest-8.3.4.pyc
│   │   ├── test_wsjgainers_normalize_csv.cpython-312-pytest-8.3.4.pyc
│   │   ├── test_yahoo.cpython-312-pytest-8.3.4.pyc
│   │   └── test_ygainers_normalize_csv.cpython-312-pytest-8.3.4.pyc
│   ├── test_controls.py
│   ├── test_wsj.py
│   ├── test_wsjgainers_normalize_csv.py
│   ├── test_yahoo.py
│   └── test_ygainers_normalize_csv.py
├── wsjgainers.html
├── wsjgainers_crontab_csv.py
├── wsjgainers_norm.csv
├── ygainers.html
├── ygainers_crontab_csv.py
└── ygainers_norm.csv
```

### Badges[![Feature Validation](https://github.com/AlannaHazlett/SP25_DS5111_uwa6xv/actions/workflows/validations.yml/badge.svg?branch=LAB-03_csv_normalizer&event=push)](https://github.com/AlannaHazlett/SP25_DS5111_uwa6xv/actions/workflows/validations.yml)
