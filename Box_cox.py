from scipy import stats
from scipy.special import boxcox1p
from scipy.stats import boxcox_normmax


from clean_data import * 


def transform(DF):
    df_T = pd.DataFrame()
    #df_T['Target'] = train['Target']
    for feature in DF.columns:
        X_T = DF.loc[:, feature]
        lam = boxcox_normmax(X_T + 1)
        print(f'lambda of {feature} = {lam}')
        tt = pd.DataFrame()
        #tt['Target'] = train['Target']
        #tt['Target'] = Y
        tt.loc[:, feature] = boxcox1p(X_T, lam)
        df_T = pd.concat([df_T, tt.loc[:, feature]], axis = 1)
        #print(tt.plot.scatter(x = feature, y= 'Target'))
        #print(train.plot.scatter(x = feature, y= 'Target'))
    return df_T
   

X_t = X1[['LotArea', 'patioSF','Bsmt_ratio']]
tt = transform(X_t)


train[tt.columns] = tt

Y = train['SalePrice']/train['TotalSF']
X1 = train[['LotFrontage', 'LotArea', 'OverallQual', 'OverallCond', 'YearRemodAdd', 
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