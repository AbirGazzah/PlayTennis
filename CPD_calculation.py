import pandas as pd


def search_corresp(X, x1, y):
    feature_count_y = 0
    feature_count_n = 0
    yes_count = 0
    no_count = 0
    for i in range(len(y)):
        if y[i] == 'Yes':
            yes_count += 1
            if X[i] == x1:
                feature_count_y += 1
        else:
            no_count += 1
            if X[i] == x1:
                feature_count_n += 1
    p_x1_yes = feature_count_y / yes_count
    p_x1_no = feature_count_n / no_count
    return p_x1_yes, p_x1_no


def possible_CPD(X0, X1, X2, X3):
    all_CPD = set((i, j, k, l) for i in X0
                  for j in X1
                  for k in X2
                  for l in X3
                  )
    return list(all_CPD)


def CPD(X0, X1, X2, X3, y, py, pn):
    all_CPD = possible_CPD(X0, X1, X2, X3)
    CPD = {}
    for CPD_ in all_CPD:
        eq_y = py * search_corresp(X0, CPD_[0], y)[0] * search_corresp(X1, CPD_[1], y)[0] * \
               search_corresp(X2, CPD_[2], y)[0] * search_corresp(X3, CPD_[3], y)[0]
        eq_n = pn * search_corresp(X0, CPD_[0], y)[1] * search_corresp(X1, CPD_[1], y)[1] * \
               search_corresp(X2, CPD_[2], y)[1] * search_corresp(X3, CPD_[3], y)[1]
        CPD['P(' + str(CPD_)] = ['{:.2f}'.format(eq_y / (eq_y + eq_n)), '{:.2f}'.format(
            eq_n / (eq_y + eq_n))]  # [ when PlayTennis = yes, when PlayTennis = no]

    df = pd.DataFrame([CPD[key] for key in CPD], [key for key in CPD])
    df.columns = ['P(PlayTennis = yes)', 'P(PlayTennis = no)']
    return df


def main():
    with open('./tennis_data.txt', 'r') as f:
        data = f.readlines()

    py = 0.64
    pn = 0.36
    Temperature = []
    outlook = []
    Humidity = []
    Wind = []
    PlayTennis = []

    for row in data:
        vector = row.split(',')
        outlook.append(vector[1])
        Temperature.append(vector[2])
        Humidity.append(vector[3])
        Wind.append(vector[4])
        PlayTennis.append(vector[5][:-1])

    print(CPD(outlook, Temperature, Humidity, Wind, PlayTennis, py, pn))


if __name__ == '__main__':
    main()