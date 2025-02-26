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
	* If you have not entered your virtual environment you can quickly do this with `make update`.
	* Then you call to create the csv, which depends upon the html call,  `make ygainers.csv`. You can see an example of this csv in my [sample_data](https://github.com/AlannaHazlett/SP25_DS5111_uwa6xv/tree/main/sample_data) directory. 
* The current structure of the repository is:
```
├── LICENSE
├── README.md
├── google-chrome-stable_current_amd64.deb
├── requirements.txt
├── sample_data
│   └── ygainers.csv
├── scripts
│   ├── google-chrome-stable_current_amd64.deb
│   ├── init.sh
│   ├── install_chrome_headless.sh
│   ├── makefile
│   └── setup_github_global_creds.sh
└── ygainers.html
```
### Badges
[![Feature Validation](https://github.com/AlannaHazlett/SP25_DS5111_uwa6xv/actions/workflows/validations.yml/badge.svg?branch=LAB-03_csv_normalizer&event=push)](https://github.com/AlannaHazlett/SP25_DS5111_uwa6xv/actions/workflows/validations.yml)
