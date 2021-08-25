import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
plt.style.use('ggplot')

test = pd.read_csv("data/test_set.csv")

print(test.Neighborhood.value_counts())
test.boxplot(column ='SalePrice', by = 'Neighborhood')

# Dummies for Neigghborhood

test.columns

dummy = pd.get_dummies(test['Neighborhood'], prefix='hood')
drop_col = test['Neighborhood'].mode()[0]
dummy.drop(['hood_'+drop_col], axis = 1, inplace= True) # race 1 is the dominant category
dummy.head()

test = pd.concat([test, dummy], axis= 1) 
test.shape

print(test.columns)

##Fill in Na with Median
# Lot Frontage

front = test.LotFrontage
med = front.median()

test['LotFrontage'].fillna(med,inplace= True)
#hs_na = test.isna().sum()
#hs_na.plot.bar()


# Income
front = test.income
med = front.median()

test['income'].fillna(med,inplace= True)


missingRows = pd.isnull(test.loc[:, test.columns != 'tract']).any(axis = 1)


#missingRows = pd.isnull(trai)
missingRows.sum()
test = test[~missingRows] 

hs_na = test.isna().sum()
hs_na.plot.bar()

# Finished Basement Sq-ft
test['FinBsmtSF'] = test['TotalBsmtSF'] - test['BsmtUnfSF']

# Total SF
test['TotalSF'] = test['TotalBsmtSF'] + test['1stFlrSF'] + test['2ndFlrSF']

test['bsmt_above_ratio'] = test['TotalBsmtSF']/(test['1stFlrSF'] + test['2ndFlrSF'])

# Zoning Dummy

dummies = pd.get_dummies(test, prefix=['MSZoning'], columns = ['MSZoning'], drop_first = True)
dummies = dummies[['PID','MSZoning_RH','MSZoning_RL','MSZoning_RM']]
test = test.merge(dummies, left_on = 'PID', right_on = 'PID')

def near_rr(df):
    rr = ['RRAe', 'RRAn', 'RRNn','RRNe']
    if df['Condition1'] in rr:
        return 1
    if df['Condition2'] in rr:
        return 1
    else:
        return 0

# Creating near RR column
test['NearRR'] = test.apply(near_rr, axis =1)

def near_pos(df):
    pos = ['PosA', 'PosN']
    if df['Condition1'] in pos:
        return 1
    if df['Condition2'] in pos:
        return 1
    else:
        return 0

# Creating near Positive Feature column
test['NearPos'] = test.apply(near_pos, axis = 1)

# Creating function to see if Condition1 or Condition2 shows house is adjacent to arterial road
def near_art(df):
    art = ['Artery']
    if df['Condition1'] in art:
        return 1
    if df['Condition2'] in art:
        return 1
    else:
        return 0

# Creating adjacent to arterial road column
test['Artery'] = test.apply(near_art, axis = 1)

# Function to converting ordinal KitchenQual to number
def qual_to_num_kit(df):
    if df['KitchenQual'] == 'Po':
        return 1
    if df['KitchenQual'] == 'Fa':
        return 2
    if df['KitchenQual'] == 'TA':
        return 3
    if df['KitchenQual'] == 'Gd':
        return 4
    if df['KitchenQual'] == 'Ex':
        return 5

# Replacing Kitchen Qual string values with numerical
test['KitchenQual'] = test.apply(qual_to_num_kit, axis = 1)


# Building Types

# separate dummy df
dum_bldgtype = pd.get_dummies(test.BldgType, prefix='BldgType')
dum_bldgtype.drop('BldgType_'+str(test['BldgType'].mode()[0]), axis=1, inplace=True)
test = pd.concat([test, dum_bldgtype], axis=1)


# House Style

test['HouseStyle'].replace('2.5Fin', '2Story', inplace=True)
test['HouseStyle'].replace('2.5Unf', '1Story', inplace=True)
test['HouseStyle'].replace('1.5Unf', '1.5Fin', inplace=True)

dum_housestyle = pd.get_dummies(test.HouseStyle, prefix='HouseStyle')
dum_housestyle.drop('HouseStyle_'+str(test['HouseStyle'].mode()[0]), axis=1, inplace=True)
# concatenating dum_housestyle with test
test = pd.concat([test, dum_housestyle], axis=1)



# Basement 
test['Bsmt_ratio'] = test['FinBsmtSF']/test['TotalBsmtSF']
missvals = test.Bsmt_ratio.isnull()
test.loc[missvals,'Bsmt_ratio'] = 0 


# Rms 
test['Bedr_ratio'] = test['BedroomAbvGr']/test['TotRmsAbvGrd']

coldrop = ['Unnamed: 0','Unnamed: 0.1','MSSubClass']
test = test.drop(coldrop, axis = 1)


test = test[test.dist<500]
test['dist'].max()

Y_test = test['SalePrice']/test['TotalSF']
X1_test = test[['LotFrontage', 'LotArea', 'OverallQual', 'OverallCond', 'YearRemodAdd', 
           'KitchenQual', 'Fireplaces', 'GarageArea', 
           'MiscVal', 'bathrm_cnt', 'patioSF', 'dist', 'income', 
           'hood_Blmngtn', 'hood_BrDale', 'hood_BrkSide', 'hood_ClearCr', 
            'hood_CollgCr', 'hood_Crawfor', 'hood_Edwards', 'hood_Gilbert', 
            'hood_Greens', 'hood_IDOTRR', 'hood_MeadowV', 'hood_Mitchel', 
            'hood_NPkVill', 'hood_NWAmes', 'hood_NoRidge', 'hood_NridgHt', 
            'hood_OldTown', 'hood_SWISU', 'hood_Sawyer', 'hood_SawyerW', 
           'hood_Somerst', 'hood_StoneBr', 'hood_Timber', 'hood_Veenker', 
           'MSZoning_RH', 'MSZoning_RL', 'MSZoning_RM', 'NearRR', 'NearPos', 
           'Artery', 'BldgType_2fmCon', 'BldgType_Duplex', 'BldgType_Twnhs', 
           'BldgType_TwnhsE', 'HouseStyle_1.5Fin', 'HouseStyle_2Story', 
           'HouseStyle_SFoyer', 'HouseStyle_SLvl','Bsmt_ratio','Bedr_ratio',
           'TotalBsmtSF','bsmt_above_ratio']]