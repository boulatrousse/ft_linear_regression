GREEN					= \033[1;32m
UNDERLINE				= \e[4m
END_UNDERLINE			= \e[24m
PURPLE					= \033[1;35m
BLUE			        = \033[0;36m
END						= \033[0m

DATA					= data.csv
all:
	@echo "$(GREEN)$(UNDERLINE)Usage$(END_UNDERLINE): make setup (install requirements)"
	@echo "       make price (predict price of a car)"
	@echo "       make train (train the model)"
	@echo "       make json  (set thetas parameters to 0)$(END)"

setup:
	@python -m venv env
	@pip install -r utils/requirements.txt

price:
	@python predict_price.py

train:
	@python ft_linear_regression.py $(DATA)

json:
	@echo "{\"theta0\": 0, \"theta1\": 0}" > params.json



