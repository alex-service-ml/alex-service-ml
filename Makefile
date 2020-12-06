DOMAIN_NAME=predictwith.us
SHELL=/bin/bash
CONDA_ACTIVATE=source $$(conda info --base)/etc/profile.d/conda.sh ; conda activate ; conda activate blog

build:
	$(CONDA_ACTIVATE) ; which python
	printf "$(DOMAIN_NAME)" > docs/CNAME
	# $(CONDA_ACTIVATE) ; python sitebuilder.py --build
