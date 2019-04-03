def weight_on_planets():
   e_weight = int(input('What do you weigh on earth? '))
   m_weight = e_weight * 0.38
   j_weight = e_weight * 2.34
   print(('\n' + 'On Mars you would weigh {} pounds.\n' + 'On Jupiter you would weigh {} pounds.').format(m_weight,j_weight))
   
   
   
if __name__ == '__main__':
   weight_on_planets()