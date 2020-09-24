'''
Natural Language Processing (NLP)
ECOM6355

ASSIGNEMENT # 1

AZIZA AWAD HASSAN
220182085

'''


import re
txt = "The emergence of COVID-19 we have seen instances of public stigmatization among specific populations, and the rise of harmful stereotypes. Stigmatization could potentially contribute to more severe health problems, ongoing transmission, and difficulties controlling infectious diseases during an epidemic. Please see the Subject in Focus section for more information on how to counter stigmatizing attitudes. New cases for today in Alexandria are 256 cases and 122 cases were registered as recovered. MOH thinking about major lockdown for 3 weeks. In Cairo there were registered 400 new cases and the recovered 350 but no lockdown is seen ahead."
x = re.search("[Nn]ew cases|[Rr]ecovered cases",txt)
y = re.findall("[Nn]ew cases.*[0-9]{3}",txt)
z = re.findall("\d{3}",txt)
print("X = ",x)
print("Y = ",y)
print("Z = ",z)
print("In Alexandria: New Cases = ",z[0],", recoved cases = ",z[1],"\nIn Cairo: New Cases = ",z[2],", recoved cases = ",z[3])

print("X = ",x.group())

