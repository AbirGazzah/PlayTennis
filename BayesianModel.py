from pgmpy.models import BayesianModel
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination


model = BayesianModel([('Outlook', 'PlayTennis'),('Temperature', 'PlayTennis'), ('Humidity', 'PlayTennis'), ('Wind', 'PlayTennis')])
cpd_outl = TabularCPD(variable='Outlook', variable_card=3, values =[[0.36], [0.28], [0.36]], state_names={'Outlook': ['sunny', 'overcast', 'rain']})
cpd_temp = TabularCPD(variable='Temperature', variable_card=3, values =[[0.29], [0.29], [0.42]], state_names={'Temperature': ['hot', 'cool', 'mild']})
cpd_hum = TabularCPD(variable='Humidity', variable_card=2, values =[[0.5], [0.5]], state_names={'Humidity': ['high', 'normal']})
cpd_wind = TabularCPD(variable='Wind', variable_card=2, values =[[0.57], [0.43]], state_names={'Wind': ['weak', 'strong']})

cpd_pt = TabularCPD(variable = 'PlayTennis', variable_card=2, values = [[0.2, 0.08, 0.67, 0.4, 0.43, 0.2, 0.86, 0.67, 0.34, 0.14, 0.8, 0.58,
                                                                        1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 0.36, 0.16, 0.82, 0.6,
                                                                        0.63, 0.36, 0.93, 0.82, 0.53, 0.28, 0.9, 0.75],
                                                                       [0.8, 0.92, 0.33, 0.6, 0.57, 0.8, 0.14, 0.33, 0.66, 0.86, 0.2, 0.42,
                                                                       0. ,0. ,0. ,0. ,0. ,0. ,0. ,0. ,0. ,0. ,0. ,0. ,0.64, 0.84, 0.18, 0.4,
                                                                       0.37, 0.64, 0.07, 0.18, 0.47, 0.72, 0.1, 0.25]],
                    evidence = ['Outlook', 'Temperature', 'Humidity', 'Wind'],
                    evidence_card = [3, 3, 2, 2],
                    state_names = {
                        'PlayTennis': ['yes', 'no'],
                        'Outlook': ['sunny', 'overcast', 'rain'],
                        'Temperature': ['hot', 'cool', 'mild'],
                        'Humidity': ['high', 'normal'],
                        'Wind': ['weak', 'strong']
                    })


model.add_cpds(cpd_outl, cpd_temp, cpd_hum, cpd_wind, cpd_pt)
#print(model.check_model())
#print(model.get_cpds())
#print(cpd_pt)
infer = VariableElimination(model)
print(infer.query(['PlayTennis'], evidence={'Outlook': 'sunny', 'Wind': 'weak', 'Temperature': 'hot', 'Humidity': 'normal'}))
print(infer.map_query(['PlayTennis'], evidence={'Outlook': 'sunny', 'Wind': 'weak', 'Temperature': 'hot', 'Humidity': 'normal'}))