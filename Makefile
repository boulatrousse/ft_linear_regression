GREEN					= \033[1;32m
UNDERLINE				= \e[4m
END_UNDERLINE			= \e[24m
PURPLE					= \033[1;35m
BLUE			        = \033[0;36m
END						= \033[0m

DATA					= data.csv
all:
	@echo "$(GREEN)$(UNDERLINE)Usage$(END_UNDERLINE): make setup    (install virtual env)"
	@echo "       make req      (install matplotlib)"
	@echo "       make predict  (predict price of a car)"
	@echo "       make train    (train the model)"
	@echo "       make json     (reset json file)$(END)"

setup:
	@python3 -m venv env

req:
	@pip install -r utils/requirements.txt

predict:
	@python predict_price.py

train:
	@python ft_linear_regression.py $(DATA)

json:
	@echo "{\"theta0\": 0, \"theta1\": 0}" > params.json

clean:
	@rm -rf __pycache__
	@rm -rf utils/__pycache__