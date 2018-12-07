from textblob.classifiers import NaiveBayesClassifier
trainData=[]
f=open('/home/ai31/Desktop/train.txt','r')
data=f.readline().strip()
while data:
#	print(data)
        splitData=data.split('.')
        category=splitData[0]
        content=splitData[1]
        tuple=content,category
        trainData.append(tuple)
        data=f.readline().strip()
print('added data to train data')
print('training the model')
classifier=NaiveBayesClassifier(trainData)
testData=[('C01','Bacterial Infections Mycoses'),('C02','Virus Diseases')
print(classifierModel.classify("Measles antibody: reevaluation of protective titers.
 A school blood drive before a measles outbreak permitted correlation of preexposure measles antibody titers with clinical protection using the plaque reduction neutralization (PRN) test and an EIA.
 Of 9 donors with detectable preexposure PRN titer less than or equal to 120, 8 met the clinical criteria for measles (7 seroconfirmed) compared with none of 71 with preexposure PRN titers greater than 120 (P less than .0001).
 Seven of 11 donors with preexposure PRN titers of 216-874 had a greater than or equal to 4-fold rise in antibody titer (mean, 43-fold) compared with none of 7 with a preexposure PRN titer greater than or equal to 1052 (P less than .02).
 Of 37 noncases with preexposure PRN titer less than 1052, 26 (70%) reported one or more symptoms compared with 11 (31%) of 35 donors with preexposure PRN titers greater than or equal to 1052 (P less than .002).
 By EIA, no case had detectable preexposure antibody; the preexposure geometric mean titer of asymptomatic donors (220) was not significantly higher than that of symptomatic donors who did not meet the clinical criteria for measles (153) (P = .10).
 The study suggests that PRN titers less than or equal to 120 were not protective against measles disease and illness without rash due to measles may occur in persons with PRN titers above this level."))    

