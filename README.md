# PlayTennis
This repository contains Python code for a small dataset that includes recall data for 14 days. The dataset features include Outlook, Temperature, Humidity, and Wind, while the output variable is represented as `y = PlayTennis`, which can take on the values 'yes' or 'no'. In this problem, we use the Naive Bayes theorem to calculate the necessary conditional probabilities for the Naive Bayes network.

### CPD Calculation
In the CPD_calculation.py script, we calculate all the possible conditional probabilities, differentiating between cases where the output variable 'PlayTennis' is 'yes' and where it is 'no'. The script takes as input the recalled data stored in the text file : `data.txt` and returns a table containing all the calculated probabilities. For a detailed illustration of the Bayesian network in which we use these calculated probabilities, you can refer to the PDF file in the repository named 'BayesNet.pdf'.

### Bayesian Model
The BayesianModel.py script models the constructed Bayesian network using the pgmpy library. You can utilize this code to calculate further probabilities using the 'infer.query' or 'infer.map_query' functions.

### Runing the code
To execute the code, you will need the following Python packages:

```bash
pip install pandas
pip install pgmpy
pip install importlib-resources
```
To run the `CPD_calculation.py` script:
```bash
python CPD_calculation.py
```

To run the `BayesianModel.py` script:
```bash
python BayesianModel.py
```
