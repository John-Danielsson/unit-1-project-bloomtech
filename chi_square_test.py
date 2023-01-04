# Execute import and install statements.
import pandas as pd
from scipy.stats import chi2_contingency
import matplotlib as plt
# This following commented-out section is for notebook use.
# from google.colab import files
# !pip install kaggle

# # Upload kaggle.json (API token).
# token = files.upload()
# # Note: your present working directory
# # might be different from mine.
# # Put `kaggle.json` in a directory
# # called `.kaggle` in the `/root` directory.
# # Like this:
# # /root/.kaggle/kaggle.json
# %mkdir ../root/.kaggle
# %mv kaggle.json ../root/.kaggle

# # Make sure no one else can use the token.
# !chmod 600 /root/.kaggle/kaggle.json
# # Download dataset from Spotify.
# !kaggle datasets download -d paradisejoy/top-hits-spotify-from-20002019

# Make the .zip file a DataFrame.
# pd.read_csv() automatically unzips zipped .csv files for you.
df = pd.read_csv('top-hits-spotify-from-20002019.zip')
print(df.shape)
print(df.describe())

# Add new columns.
# These are based on the question we're asking:
# Are (explicit = 1 AND danceability >= 0.75) associated with popularity >= 70?
print(df.shape)
df['exp_dance'] = ((df['explicit'] == 1) & (df['danceability'] >= 0.75))
df['pop_70_or_greater'] = df['popularity'] >= 70
df['pop_80_or_greater'] = df['popularity'] >= 80

# Check out the columns.
print(df.columns)

# Check null values.
print(df.isnull().sum().sum())

# Perform a Chi Square Test of Independences
crosstab = pd.crosstab(
    index=df['exp_dance'],
    columns=df['pop_70_or_greater'],
    rownames=['exp_dance'],
    colnames=['pop_70_or_greater']
)
print(crosstab)
chi2 = chi2_contingency(crosstab)
t_val = chi2[0]
p_val = chi2[1]
dof = chi2[2]
expected = chi2[3]
print('   t_val=', t_val)
print('   p_val=', p_val)
print('     dof=', dof)
print('expected=', expected)
crosstab.plot(kind='bar')
print(df.loc[df['popularity'] >= 70].shape)
