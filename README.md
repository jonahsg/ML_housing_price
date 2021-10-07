# Machine Learning Housing Price Project
Ben Burkey, Jonah Gerstel, Michael McGuigan, Lena Chretien

## Dataset Used

-  https://www.kaggle.com/c/house-prices-advanced-regression-techniques
-  Various Census Data (ex. Median Income)
-  Various Location Data (ex. Distance to University)

## Business Approach

Goal: Aide realtors, buyers, and sellers in valuing houses and increasing house value based on a multitude of factors, using an output of Price/SF,  the most common valuation metric in real estate.

Factors include:

- Location (ex. Neighborhood, Proximity to a Main Road, Distance to University, etc)
- House Layout (ex. Number of Stories, Bedrooms, and Bathrooms, etc)
- House Quality (ex. Overall Quality, Finishing of Basement, etc)
- House Content (ex. A/C System,  Electric System, Presence of a Pool,  etc)

## Wrangling and Cleaning

- Merged location and census datasets to determine distance to various points of interest and income levels of various neighborhoods
- Filled NAs with median of neighborhood
- Ensured columns and column names were accurate and workable (ex. no white space, values were correct data type, etc
- Dummified/One-Hot-Encoded categorical variables (ex. Zoning, House Style, etc)
- Removed duplicates

## Feature Engineering
- Used Price/SF as target variable as opposed to Price (and including SF in dependent variables) in order to normalize the target variable and utilize a more applicable target variable to the real-estate industry
- Combined variables (ex. combined all porch-related variables into one 'Total Patio SF' variable)
- Created ratios of variables to provide more meaningful insight for the real-estate industry and reduce multi-collinearity (ex. Basement SF/Above Ground SF)
- Removed variables with high VIF or little importance with regard to Price/SF
- Normalized problematic independent variable

## Models Used (Tuned hyperparameters with GridSearchCV)
- Normal MLR
- Lasso
- Random Forest
- XGBoost
- SVM

## Results
- All models (besides normal MLR) had similar RMSE (7.5 - 8.6) and R-Squared (0.64 - 0.73) values
- Feature Importance was extracted from the tuned models, aggregated, and weighted in order to determine the effect and importance of each feature via ranking
- Based on the effect a feature had on Price/SF and the average cost of adding that feature, recommendations were made for homeowners on cost-effective ways to increase the Price/SF of their house and features that would negatively impact Price/SF. These recommendations could also be utilized by home builders
- Utilizing the ranked feature importance, specifically around location-related features, homebuilders can also pinpoint lots for sale that would result in the highest Price/SF
- The XGBoost model (most accurate in terms of R-squared and RMSE) can also be used to value one's own house or value houses for sale and pinpoint houses below market value

## Next Steps
- In order to aggregate all of the results above into a usable way for home owners, home buyers, and home builders, an app could be created to do all of the above:
  - Home owners and realtors can input housing features to get Price/SF predictions and recommendations on cost effective ways to increase Price/SF
  - Home builders can pinpoint the best location to build a new house via the app's aggregation of lots for sale, and location features like neaighborhood, proximity to POIs, and average income of an area
  - Potential home buyers can pinpoint houses below market value via the app's aggregation of homes for sale, and compare the listing price to the model's

## Link to Presentation
https://docs.google.com/presentation/d/1c-2vBQmojRKaxgXXrkb_bL1ff24TRzBpRPr3FY4Qk7A/edit?usp=sharing



