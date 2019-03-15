import pandas as pd
import numpy as np
import Data_preprocessing_toolbox as dp


ap_df = pd.read_csv('AppleStore.csv')
gg_df = pd.read_csv('googleplaystore.csv')
it_df = pd.read_csv('itunes_scraper.csv')
it_df.drop(['web-scraper-order','name','web-scraper-start-url','app-href','tagline','cateogry-href'], axis=1, inplace=True)
it_df.dropna(inplace=True)



# # App Name Processing
# The cell below renames some apps.
ap_df.rename(columns={'track_name':'App'},inplace=True)
it_df.rename(columns={'app':'App'},inplace=True)
gg_df.drop_duplicates(subset=['App'], keep='first', inplace=True)


# # Category Processing
# The cell below merges some categories and renames the categories.
ap_df.rename(columns={'prime_genre':'Category'},inplace=True)
it_df.rename(columns={'cateogry':'Category'},inplace=True)
gg_df['Category'] = gg_df['Category'].apply(dp.Category_map)
ap_df['Category'] = ap_df['Category'].apply(dp.Category_map)
#it_df.dropna(subset=['Category'])
boo = (gg_df['Category'] == 'AUTO_AND_VEHICLES') | (gg_df['Category'] == 'LIBRARIES_AND_DEMO') |    (gg_df['Category'] == 'FAMILY') | (gg_df['Category'] == 'PARENTING') | (gg_df['Category'] == '1.9')
gg_df = gg_df.drop(gg_df[boo].index)


# # Size Processing
# The cell below unifies units of size.
ap_df.rename(columns={'size_bytes':'Size_M'},inplace=True)
gg_df.rename(columns={'Size':'Size_M'},inplace=True)
it_df.rename(columns={'size':'Size_M'},inplace=True)
gg_df['Size_M'] = gg_df['Size_M'].apply(dp.Size_map)
ap_df['Size_M'] = ap_df['Size_M'].apply(dp.Size_map)
it_df['Size_M'] = it_df['Size_M'].apply(dp.Size_map)


# # Rating Processing
# The cell below renames the column of rating.
ap_df.rename(columns={'user_rating':'Rating'},inplace=True)
it_df.rename(columns={'rating':'Rating'},inplace=True)
it_df['Rating_num'] = it_df['Rating'].apply(dp.Rating_num)
it_df['Rating'] = it_df['Rating'].apply(dp.Rating_map)
it_df = it_df[it_df['Rating_num']>1000]
gg_df.dropna(inplace=True)
# Below are used for choosing popular apps in Google Play
gg_df['Reviews'] = gg_df['Reviews'].apply(int)
gg_df = gg_df[gg_df['Reviews']>3000]
ap_df = ap_df[ap_df['rating_count_tot']>700]


# # Price Processing
# The cell below unifies price notation.
ap_df.rename(columns={'price':'Price'},inplace=True)
it_df.rename(columns={'pricing':'Price'},inplace=True)
gg_df['Price'] = gg_df['Price'].apply(dp.Price_map)
ap_df['Price'] = ap_df['Price'].apply(dp.Price_map)
it_df['Price'] = it_df['Price'].apply(dp.Price_map)


# Create clean csv
gg_clean = gg_df[['App','Category','Size_M','Price','Rating']]
ap_clean = ap_df[['App','Category','Size_M','Price','Rating']]
it_clean = it_df[['App','Category','Size_M','Price','Rating']]
gg_df.to_csv(r'myGooglePlay.csv')
ap_df.to_csv(r'myAppleStore.csv')
it_df.to_csv(r'myAppleStore_new.csv')
gg_clean.to_csv(r'myGooglePlay_clean.csv')
ap_clean.to_csv(r'myAppleStore_clean.csv')
it_clean.to_csv(r'myAppleStore_new_clean.csv')

