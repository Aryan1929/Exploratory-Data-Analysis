#!/usr/bin/env python
# coding: utf-8

# # Introduction
# 

# First importing the file containing the dataframe about the electoral bond transaction between the political parties and the purchasers ie either individuals or companies:
# 
# We'll download this file using the `urlretrieve` function from the `urllib.request` module.

# In[1]:


from urllib.request import urlretrieve


# In[2]:


party_bonds_url = 'https://raw.githubusercontent.com/Aryan1929/Exploratory-Data-Analysis/main/party_bonds_relation.csv'

urlretrieve(party_bonds_url, 'party_bonds.csv')


# To read the file, we can use the `read_csv` method from Pandas. Let's being by importing the `Pandas library`.

# In[3]:


import pandas as pd


# In[4]:


party_bonds_raw_df = pd.read_csv('party_bonds.csv')


# In[5]:


party_bonds_raw_df


# ### About the dataframe:

# This dataset into the intricate relationship between political party and companies. Leveraging data released by the Election Commission, we meticulously paired each bond purchaser's name with their corresponding political party, shedding light on the intricate web of connections between finance and politics. Our findings offer unprecedented insights into the alignment of financial interests with political ideologies, providing a nuanced understanding of how political affiliations influence investment behaviors. Explore the intersection of finance and politics like never before, as we unravel the complexities behind matched bonds and their implications for the political landscape.
# 
# This dataset provides a comprehensive analysis of Electrol Bonds purchases and donations, offering insights into the financial activities surrounding political funding. The dataset consists of component:
# 
# **Sr No.**: This stands for Serial Number, which is a unique identifier assigned to each entry in the dataset, typically starting from 1 and incrementing by 1 for each subsequent entry.
# 
# **Reference No (URN)**: URN stands for Unique Reference Number. It's a distinct identifier assigned to each record in the dataset for easy reference and tracking purposes.
# 
# **Journal Date**: This is the date on which the transaction was recorded or logged in the journal.
# 
# **Date of Purchase**: This refers to the date when the bond was bought or acquired.
# 
# **Date of Expiry**: This is the date on which the bond expires or reaches the end of its term.
# 
# **Name of the Purchaser**: This is the full name of the individual or entity who purchased the bond.
# 
# **Prefix**: This could be a prefix associated with the purchaser's name or title, such as Mr., Mrs., Dr., etc.
# 
# **Bond Number**: This is the unique identifier assigned to the bond itself.
# 
# **Denominations**: Denominations refer to the face value or monetary units of the bonds purchased.
# 
# **Issue Branch Code**: This code indicates the specific branch or location where the bonds were issued.
# 
# **Issue Teller**: This is the name or identifier of the bank teller or official who facilitated the issuance of the bonds.
# 
# **Status**: This indicates the current status of the bond, whether it's active, expired, redeemed, etc.
# 
# **Name of the Political Party**: If applicable, this refers to the political party associated with the purchaser or issuer of the bonds.
# 
# **Crore**: This column likely indicates the monetary value of the bonds in crores, a unit of measurement commonly used to denote large sums of money in the Indian subcontinent. 
# 
# **Political Parties in India**: The dataset encompasses donations made to various political parties in India, including but not limited to:
# 
# * Bharatiya Janata Party (BJP)
# * All India Trinamool Congress (TMC)
# * Indian National Congress (INC)
# * Bharat Rashtra Samithi
# * Biju Janata Dal (BJD)
# * Dravida Munnetra Kazhagam (DMK)
# * YSR Congress Party (Yuvajana Sramika Rythu Congress Party)
# * Shiv Sena (Political Party)
# * Telugu Desam Party (TDP)
# * Aam Aadmi Party (AAP)
# * Rashtriya Janata Dal (RJD)
# * Nationalist Congress Party (NCP)
# * Janata Dal (Secular) (JD(S))
# * Sikkim Krantikari Morcha (SKM)
# * Adyaksha Samajvadi Party
# * Jharkhand Mukti Morcha (JMM)
# * Janasena Party
# * All India Anna Dravida Munnetra Kazhagam (AIADMK)
# * Shiromani Akali Dal (SAD)
# * Maharashtra Navnirman Sena (MNS)
# * Goa Forward Party
# * Bihar Pradesh Janta Dal(United) (JDU)
# * Sikkim Democratic Front (SDF)
# * Jammu and Kashmir National Conference (JKNC)
# * Nationalist Congress Party Maharashtra Pradesh
# 
# **Purpose:**
# The dataset aims to provide insights into the funding patterns of political parties in India, facilitating a better understanding of political finance dynamics and regulatory compliance.
# 
# **Source:**
# The dataset was compiled from publicly available sources, possibly including government reports, electoral commission records, or other official disclosures related to political financing and electoral contributions.
# 
# **Format:**
# The dataset is provided in a tabular format with structured columns in a form of CSV file.

# #### Let's view the list of columns in the dataframe:

# In[6]:


party_bonds_raw_df.columns


# From above we get the list of names of all the colums present in the dataframe `party_bonds_raw_df` representing the Matching of Election Commission Data to Bond Purchasers with Political Affiliations

# # Data Preparation and Cleaning

# While this dataframe contains a wealth of data we will limit the data only to those parts which will be used by us for data analysis and visulaization, this is important to separate out unwanted datas from the sea of data we have in the dataframe:
# 

# Based on the dataset columns provided, here are the potential topics we will be considering for analysis:
# 
# 1. **Electoral Bond Transactions Analysis:**
#    - Explore the distribution of bond denominations.
#    - Analyze the frequency and timing of bond purchases (Date of Purchase).
#    - Investigate the status of bonds (e.g., whether they have been active, expired or redeemed).
#    -  Analyze any trends or patterns in bond status over time.
#     
# 2. **Purchaser Analysis:**
#    - Identify the top purchasers (individuals or entities) of electoral bonds.
#    - Analyze the distribution of purchases among different purchasers.
#    - Investigate any patterns or trends in purchasing behavior.
# 
# 3. **Political Party Funding Analysis:**
#    - Examine the distribution of funding among different political parties.
#    - Analyze the timing and frequency of bonds purchased to to be funded to political parties.
#    - Analyzing the amount (in Crores) of Electoral Bond Purchases for associated Political Parties in a particular year on monthly basis
# 
# 5. **Financial Analysis:**
#    - Calculate the total amount of money involved in electoral bond transactions.
#    - Examine the distribution of bond amounts in crore.
# 
# By focusing on these topics, you can gain valuable insights into the electoral bond transactions and their implications for political financing.

# ## (1) Selecting a subset of columns with relevant data for analysis

# #### Selecting out only those columns that are required for the alanalysis of the above mentioned potential topics:

# In[7]:


selected_columns = ['Sr No.', 
                    'Reference No  (URN)', 
                    'Journal Date', 
                    'Date of\rPurchase',
                    'Date of Expiry', 
                    'Name of the Purchaser', 
                    'BondNumber',
                    'Denominations',   
                    'Status',
                    'Name of the Political Party', 
                    'Crore']


# Length of the columns in the updated data frame:

# In[8]:


len(selected_columns)


# #### Extracting a copy of columns from this data to a new datafeame `party_bonds_df`, which can be continiously modified without affecting the original dataframe.
# 
# Below the `party_bonds_df` represent the new dataframe without the unnecessary columns:

# In[9]:


party_bonds_df = party_bonds_raw_df[selected_columns]


# In[10]:


party_bonds_df


# ## (2) Reanaming the Column Names

# Renaming the column names for better usability during various opeartions performed during the analysis of data from the dataframe:

# In[11]:


party_bonds_df = party_bonds_df.rename(columns = {'Sr No.': 'Sr-No.', 
                                                  'Reference No  (URN)': 'Reference_No_(URN)', 
                                                  'Journal Date': 'Journal_Date', 
                                                  'Date of\rPurchase': 'Date_of_Purchase',
                                                  'Date of Expiry': 'Date_of_Expiry', 
                                                  'Name of the Purchaser': 'Name_of_the_Purchaser', 
                                                  'Name of the Political Party': 'Name_of_the_Political_Party'})


# In[12]:


party_bonds_df


# ## (3) Changing the Index
# 
# Selecting the `Sr_no.` column as the index for the given data fram `party_bonds_df`

# In[13]:


party_bonds_df.set_index('Sr-No.', inplace=True)


# In[14]:


party_bonds_df


# ## (4) Viewing some basic information about the dataFrame

# In[15]:


party_bonds_df.shape


# From above we can see that the dataframe consists of 18871 rows and 10 columns

# In[16]:


party_bonds_df.info()


# * From the above data we can see that all values of all the columns are Non-null values.
# * Also the `Dates` values are in object Dtype which should be converted to DatetimeIndex for usability in data analysis
# * The `Refrence_No_(URN)` and `BondNumbers` are unique numbers on which no opeartions are to be performed, so these can be converted into strings rather than being in float.

# In[17]:


party_bonds_df.describe()


# ## (5) Converting required fields to DatetimeIndex
# 
# Converting the `Journal_Date`,	`Date_of_Purchase` and `Date_of_Expiry` values from string values to DatetimeIndex values:

# In[18]:


party_bonds_df['Journal_Date'] = pd.to_datetime(party_bonds_df.Journal_Date)
party_bonds_df['Date_of_Purchase'] = pd.to_datetime(party_bonds_df.Date_of_Purchase)
party_bonds_df['Date_of_Expiry'] = pd.to_datetime(party_bonds_df.Date_of_Expiry)


# Observing the changes in Dtype now:

# In[19]:


party_bonds_df.info()


# ## (6) Converting required Fields to Strings
# 
# The `Reference_No_(URN)` and `BondNumbers` are unique numbers on which no opeartions are to be performed, so these can be converted into strings rather than being in float.

# In[20]:


party_bonds_df['Reference_No_(URN)'] = party_bonds_df['Reference_No_(URN)'].astype(str)
party_bonds_df['BondNumber'] = party_bonds_df['BondNumber'].astype(str)


# In[21]:


party_bonds_df.info()


# We can see that the `Reference_no_(URN)` and `BondNumber` columns are successfully converted to object Dtype.

# ## (7) Adding required Columns
# 
# Adding the `Year_of_Purchase` and `Month_of_Purchase` columns to the party_bonds_df dataframe
# 

# In[22]:


party_bonds_df['Year_of_Purchase'] = pd.DatetimeIndex(party_bonds_df.Date_of_Purchase).year
party_bonds_df['Month_of_Purchase'] = pd.DatetimeIndex(party_bonds_df.Date_of_Purchase).month


# In[23]:


party_bonds_df


# # Exploratory Data Analysis
# 
# First importing all libraries that would be required for data analysis and vizualization:

# In[24]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[25]:


sns.set_style("darkgrid")


# ## (1) Electoral Bond Transactions Analysis:
# 
# - Exploring the distribution of bond denominations.
# - Analyzing the frequency and timing of bond purchases (Date of Purchase).
# - Investigating the status of bonds (e.g., whether they have been active, expired or redeemed) and trends/patterns in bond status over time.

# ### (1.1) Exploring the distribution of bond denominations.

# #### (a) Different types of denominations in DataFrame

# In[26]:


party_bonds_df.Denominations.unique()


# In[27]:


len(party_bonds_df.Denominations.unique())


# From above we can see that `party_bonds_df` dataframe contains 5 different types of denominations ie:
# * 10,00,000
# * 1,00,000
# * 1,00,00,000
# * 1,000
# * 10,000

# #### (b) Total amount (in Crores) worth of Electoral bonds distribution among different denominations
# 

# In[28]:


party_bonds_Denominations_df = party_bonds_df.groupby('Denominations')[['Crore']].sum()


# In[29]:


party_bonds_Denominations_df


# The above dataframe gives us an idea about the amount (in Crores) worth of Electoral bonds present in form of different denominations.
# 
# * 11671 Crores is present in the form of 1,00,00,000 denomination.
# * 22.28 Crores is present in the form of 1,00,000 denomination.
# * 0.0132 Crores is present in the form of 1,000 denomination.
# * 462 Crores is present in the form of 10,00,000 denomination.
# * 0.22 Crores id present in the form of 10,000 denomination

# Visual representaion of it is given as following:

# In[124]:


party_bonds_Denominations_df.plot(kind='bar', 
                                  figsize=(10,6), 
                                  xlabel = 'Denomination', 
                                  ylabel = 'Amount (in Crores)', 
                                  title = 'Distribution of amount(in Crores) in Different Denominations');


# This chart depicts the total amount (in crores) held in different bond denominations. Here's a brief analysis:
# 
# * The denomination of 1,00,00,000 crores dominates significantly, holding the majority of the total amount.
# * Other denominations (1,00,000, 1,000, 10,000) have much smaller amounts in comparison.
# * This indicates that most of the value in the dataset is concentrated in the highest denomination.
# 
# The data suggests that total value of bonds are heavily skewed towards the higher denominations. The vast majority of the total bond value is tied up in the highest denomination of 1,00,00,000 crores in the dataset. This reflects a potential preference or greater issuance of larger denomination bonds within this particular dataset.

# #### (c) Purchase Year and Month of different Denominations of Electoral Bonds

# In[197]:


plt.figure(figsize=(10, 6))

sns.scatterplot(x=party_bonds_df['Date_of_Purchase'], 
                y=party_bonds_df['Denominations'], 
                hue = party_bonds_df.Month_of_Purchase)

plt.xlabel('Date of Purchase')
plt.ylabel('Denominations')
plt.title('Purchase Year and Month of different Denominations of Electoral Bonds')
plt.legend(title='Month', bbox_to_anchor=(1.05, 1), loc='upper left');


# #### (d) Frequency of each Denomination in the DataFrame

# In[31]:


party_bonds_Denominations_count_df = party_bonds_df.groupby('Denominations')[['Crore']].size()


# In[32]:


party_bonds_Denominations_count_df


# The visual representation of above data is given as following:

# In[123]:


plt.figure(figsize=(10,6))

sns.countplot(y=party_bonds_df['Denominations']);

plt.xlabel('Number of Denominations')
plt.ylabel('Denominations')
plt.title('Frequency of each Denomination in the DataFrame');


# This bar chart shows the frequency of each bond denomination within the dataset. The key points are:
# 
# * The denomination of 1,00,00,000 is the most frequent, appearing the highest number of times.
# * The 10,00,000 and 1,00,000 denominations also have significant frequencies but are less common than the highest denomination.
# * Denominations of 1,000 and 10,000 have minimal frequencies, indicating fewer instances of these smaller denominations.
# 
# The skewed distribution towards higher denomination bonds can be attributed to several possible reasons:
# 
# 1) **Preference for Larger Transactions:** Institutional investors and large corporations often deal with large sums of money, preferring fewer but larger transactions for efficiency.
# 
# 2) **Significant Contributions:** Political parties often receive large contributions from wealthy individuals, corporations, and special interest groups. These contributors are more likely to use higher denomination bonds for their donations.
# 
# 3) **Funding Large Campaigns:** Electoral campaigns, especially for major elections, require substantial funds. Higher denomination bonds facilitate the transfer of large sums of money efficiently.
# 
# 4) **Compliance:** Donors might prefer larger denominations to ensure that their contributions are fully compliant with legal and regulatory frameworks, avoiding the complexity of managing multiple smaller transactions.
# 
# 5) **Transparency:** Higher denomination bonds might be preferred to maintain transparency and ease of audit for both donors and political parties.
# 

# #### (e) List of all purchasers who have purchased  electoral bonds of a particular denomination (Ex: 1,00,00,000):

# In[34]:


party_bonds_Denomination_1Cr_df = party_bonds_df[party_bonds_df.Denominations == '1,00,00,000']


# In[35]:


party_bonds_Denomination_1Cr_df['Name_of_the_Purchaser'].unique()


# The above data gives us the list of all purchasers who have purchased electoral bonds of 1,00,00,000 denomination. Similarly the list of purchasers of other denomination Electoral Bonds Can be also found.

# #### (f) List of all Political Parties who are associated with the issue of the Electoral Bonds of a particular denomination                   (Ex: 1,00,00,000):

# In[36]:


party_bonds_Denomination_1Cr_df['Name_of_the_Political_Party'].unique()


# The above data gives us a list of all Political Parties who are associated with the issue of Electoral bonds of 1,00,00,000 denominations. Similarly the list of Political Parties associated to other denomination Electoral Bonds Can be also found.

# #### (g) Frequency of Purchase of Electoral Bonds of each Denomination Annualy 

# In[37]:


party_bonds_Denomination_yearly_df = party_bonds_df.groupby(party_bonds_df['Date_of_Purchase'].dt.to_period('Y'))['Denominations'].value_counts().unstack()


# In[38]:


party_bonds_Denomination_yearly_df


# In[39]:


party_bonds_Denomination_yearly_df.plot(kind='bar', 
                                            figsize=(10, 6),
                                            xlabel = 'Year of Purchase', 
                                            ylabel = 'Number of Denominations Purchased',
                                            title = 'Frequency of Purchase of Electoral Bonds of each Denomination Annualy ');


# ### Observations:
# 
# For all the years we observe one general trend that is:
# 
# * High frequency of purchases for the denominations 1,00,00,000 (blue) and 10,00,000 (red).
# * Moderate purchases for denominations 1,00,000 (orange) and 10,000 (purple).
# * Lower purchases for the denomination 1,000 (green).
# 
# ### Potential Reasons for Variations:
# 
# The high purchase of electoral bonds in the years 2023, 2022, and 2019 can be attributed to several factors, primarily related to the political and electoral landscape in India. Here are some possible reasons:
# 
# #### 1. **Election Years:**
#    - **2019 General Elections:** India held its general elections in 2019. This is a major event where political parties require substantial funding for campaign activities, leading to a spike in the purchase of electoral bonds.
#    - **2022 State Elections:** Several significant state elections took place in 2022, including Uttar Pradesh, Punjab, Uttarakhand, Manipur, and Goa. These elections are crucial for political parties and necessitate large funds for campaigning.
#    - **2023 State Elections and Pre-General Election Preparation:** In 2023, there were several important state elections, and political parties also began preparing for the 2024 general elections. This preparation often starts a year in advance, driving up the demand for funds.
# 
# #### 2. **Political Funding Strategies:**
#    - **Increased Fundraising Efforts:** During these peak election periods, political parties intensify their fundraising efforts to ensure they have adequate resources for extensive campaign activities.
#    - **Large Denomination Bonds:** The dominance of high-value denominations like 1,00,00,000 indicates significant donations, likely from large corporate donors and wealthy individuals who prefer making substantial contributions during crucial election years.
# 
# #### 3. **Regulatory Environment:**
#    - **Regulatory Changes:** Any favorable changes in regulations governing electoral bonds might have made it easier or more attractive for donors to purchase bonds during these years.
#    - **Tax Incentives and Transparency Issues:** The tax benefits associated with donations via electoral bonds and the anonymity they offer could have spurred higher purchases during key election periods.
# 
# 
# #### 4. **Strategic Political Investments:**
#    - **Pre-Election Investments:** Political parties often build a war chest before major elections to fund advertising, rallies, and other campaign activities. The higher purchases in 2022 and 2023 could reflect pre-election funding drives.
#    - **Influence and Access:** Donors may increase their contributions in high-stakes election years to gain favor and access with the winning parties.
# 

# #### (h) Frequency of Purchase of Electoral Bonds of each Denomination Monthly

# In[40]:


party_bonds_Denomination_monthly_df = party_bonds_df.groupby(party_bonds_df['Date_of_Purchase'].dt.to_period('M'))['Denominations'].value_counts().unstack()


# In[41]:


party_bonds_Denomination_monthly_df


# In[42]:


party_bonds_Denomination_monthly_df.plot(kind='bar', 
                                            figsize=(10, 6),
                                            xlabel = 'Year-Month of Purchase', 
                                            ylabel = 'Number of Denominations Purchased',
                                            title = 'Frequency of Purchase of Electoral Bonds of each Denomination Monthly ');


# #### (i) Number of Electoral Bonds of each Denomination associated with the political parties

# In[43]:


party_bonds_Denomination_parties_df = party_bonds_df.groupby(party_bonds_df['Name_of_the_Political_Party'])['Denominations'].value_counts().unstack()


# In[44]:


party_bonds_Denomination_parties_df


# The above table shows the number of Electoral Bonds of each denomination associated with all the political parties for the year 2019-2024.

# In[45]:


party_bonds_Denomination_parties_df.plot(kind='bar', 
                                         figsize=(10, 6),
                                         xlabel = 'Political Party', 
                                         ylabel = 'Number of Denominations',
                                         title = 'Number of Electoral Bonds of each Denomination associated with the political parties');


# ### Observations:
# 
# 1. **Bharatiya Janata Party (BJP):**
#    - Highest total purchases with significant quantities in ₹1,00,00,000, ₹1,00,000, and ₹10,00,000 denominations.
# 
# 2. **Indian National Congress (INC):**
#    - Substantial purchases, though lower than BJP, with notable quantities in the highest denominations.
# 
# 3. **All India Trinamool Congress (AITC) and Bharat Rashtra Samithi (BRS):**
#    - Strong purchases, particularly in ₹1,00,00,000 denomination, indicating robust regional support.
# 
# 4. **Regional Parties:**
#    - Parties like Biju Janata Dal (BJD) and Dravida Munnetra Kazhagam (DMK) show considerable bond purchases, reflecting significant regional backing.
# 
# 5. **Smaller and Emerging Parties:**
#    - Lower purchases by parties like Goa Forward Party and Janasena Party, suggesting limited fundraising capacities.
# 
# ### Possible Reasons:
# 
# 1. **Political Influence and Strength:**
#    - Major parties like BJP and INC have broader national influence, attracting more donations.
# 
# 2. **Election Cycles:**
#    - Increased need for campaign funds during election years leads to higher bond purchases.
# 
# 3. **Corporate and Business Contributions:**
#    - Larger parties receive significant donations from corporate entities, favoring high-denomination bonds.
# 
# 4. **Regional Dynamics:**
#    - Strong regional parties show high purchases due to substantial local support and state election requirements.
# 
# 5. **Fundraising Strategies:**
#    - Effective donor outreach and fundraising strategies impact the number and denomination of bonds purchased.

# ### (1.2) Analyzing the frequency and timing of bond purchases (Date of Purchase)

# #### (a) Annual frequency of bond purchases

# In[200]:


bonds_purchase_frequency_yearly = party_bonds_df.groupby('Year_of_Purchase').size()


# In[201]:


bonds_purchase_frequency_yearly


# The visual representation of the above data can be given as following:

# In[119]:


plt.figure(figsize=(10, 6))

sns.countplot(y=party_bonds_df['Year_of_Purchase']);

plt.xlabel('Number of Electoral Bonds')
plt.ylabel('Year of Purchase')
plt.title('Frequency of Purchase of Electoral Bonds Annualy');


# The bar chart depicts the frequency of the purchase of electoral bonds annually from 2019 to 2024. Here's an analysis of the data and the possible political reasons behind the variations in the number of purchases each year:
# 
# ### Observations:
# 
# 1. **2019:**
#    - Number of Bonds: Approximately 3000
#    - Observation: Moderate level of purchases.
# 
# 2. **2020:**
#    - Number of Bonds: Approximately 500
#    - Observation: Significant drop in purchases.
# 
# 3. **2021:**
#    - Number of Bonds: Approximately 3500
#    - Observation: Increase in the number of purchases compared to 2020.
# 
# 4. **2022:**
#    - Number of Bonds: Approximately 5000
#    - Observation: Noticeable surge in the purchase of electoral bonds.
# 
# 5. **2023:**
#    - Number of Bonds: Approximately 6000
#    - Observation: Further increase, marking the highest number of purchases in the observed years.
# 
# 6. **2024:**
#    - Number of Bonds: Approximately 1000 (partial year data likely)
#    - Observation: Relatively low compared to previous years, but data might not be complete for the year.
# 
# ### Political Reasons Behind High Purchases:
# 
# 1. **Election Years:**
#    - **2019 and 2024:** These are general election years in India, leading to higher political activity and fundraising. The relatively high purchase of electoral bonds in these years can be attributed to the need for campaign funds.
#    - **2022 and 2023:** These years likely saw significant state elections, which also require substantial funding for campaigns, resulting in high purchases of electoral bonds.
# 
# 2. **Pandemic Impact:**
#    - **2020:** The drop in bond purchases can be associated with the COVID-19 pandemic, which impacted economic activities and political fundraising efforts.
# 
# 3. **Policy and Regulations:**
#    - Changes in regulations or increased awareness and acceptance of electoral bonds as a method of political funding can also influence the frequency of purchases. For example, any amendments to make the process easier or more attractive for donors could lead to an increase in purchases.
# 
# 4. **Political Strategies:**
#    - Political parties may ramp up fundraising efforts in the years leading up to major elections to build a war chest for extensive campaign activities. The increased purchases in 2021, 2022, and 2023 can be seen as part of these preparatory activities.
# 

# #### (b) Monthly frequency of bond purchases

# In[49]:


bonds_purchase_frequency_monthly_df = party_bonds_df.groupby(party_bonds_df['Year_of_Purchase'])['Month_of_Purchase'].value_counts().unstack().sort_index()


# In[50]:


bonds_purchase_frequency_monthly_df


# The visual representation of the above data is given as following in both heatmap and bar plotting forms:

# In[210]:


plt.figure(figsize=(10, 6))

sns.heatmap(bonds_purchase_frequency_monthly_df);

plt.xlabel('Month of Purchase')
plt.ylabel('Year of Purchase')
plt.title('Number of Purchase of Electoral Bonds');


# In[51]:


bonds_purchase_frequency_monthly_df.plot(kind='bar', 
                                         figsize=(10, 6),
                                         xlabel = 'Year of Purchase', 
                                         ylabel = 'Number of Electoral Bonds',
                                         title = 'Frequency of Purchase of Electoral Bonds Monthly');


# The spikes in the purchase of electoral bonds correspond to periods surrounding significant political events and elections in India. Here's a detailed analysis for each specified period:
# 
# 1. **Early 2019**:
#    - **2019 General Elections**: The 17th Lok Sabha elections were held in April-May 2019. This major event likely prompted increased political funding in the months leading up to it.
#    
# 2. **Early 2021**:
#    - **State Elections**: Key state elections took place in West Bengal, Tamil Nadu, Kerala, Assam, and Puducherry around March-April 2021. These elections likely influenced the purchase of electoral bonds as political parties geared up for the polls.
#    
# 3. **Early 2022**:
#    - **State Elections**: In February-March 2022, state elections were held in Uttar Pradesh, Punjab, Uttarakhand, Manipur, and Goa. These elections are another probable cause for the spike in political funding observed in early 2022.
#    
# 4. **Late 2022**:
#    - **Gujarat and Himachal Pradesh Elections**: The Gujarat and Himachal Pradesh legislative assembly elections were held towards the end of 2022, driving another surge in the purchase of electoral bonds as parties mobilized resources.
#    
# 5. **Mid 2023**:
#    - **Karnataka Elections and Preparations for 2024 General Elections**: Karnataka held its state elections in May 2023, and political parties also began early preparations for the 2024 general elections, possibly leading to increased funding.
#    
# 6. **Mid 2024**:
#    - **Anticipation of the 2024 General Elections**: As the general elections are slated for April-May 2024, political activities and funding are likely ramping up during mid-2024.
# 
# These major elections and political campaigns correspond with the spikes in electoral bond purchases by various purchasers, as seen in the provided data. Political parties often require substantial funds for campaigns, which is reflected in the purchase patterns of electoral bonds around these critical periods.

# ### (1.3) Investigating the status of bonds and trends/patterns in bond status over time.

# #### (a) Identifying the different type of status of Electoral Bonds 

# In[52]:


party_bonds_df['Status'].unique()


# #### (b) Number of Electoral Bonds that have been Paid or Expired

# In[53]:


party_bonds_status_df = party_bonds_df.groupby('Status').size()


# In[54]:


party_bonds_status_df


# The visualization of above data is given as following:

# In[85]:


plt.title('Status of electoral Bonds (Paid or Expired)')
sns.countplot(y=party_bonds_df['Status']);


# From the above data and visualization we can clearly see that the status of almost all Electoral Bonds are paid and only very minimal of the Electoral Bonds are unpaid, ie out of 18871 Electoral bonds about 18741 are `Paid` and only 130 are `Unpaid`.

# #### (c) Annual Status of the Electoral Bonds Purchased

# In[56]:


party_bonds_annual_status_df = party_bonds_df.groupby(party_bonds_df['Date_of_Purchase'].dt.to_period('Y'))['Status'].value_counts().unstack()


# In[57]:


party_bonds_annual_status_df


# The visualization of teh above data is given as following:

# In[257]:


party_bonds_annual_status_df.plot(kind='bar', 
                                  figsize=(10, 6),
                                  stacked = True,
                                  xlabel = 'Year of Purchase', 
                                  ylabel = 'Number of Electoral Bonds',
                                  title = 'Status(Paid/Expired) of Electoral Bonds Purchased on Annual Basis');


# From the above data it is clearly seen that maximum of all the Electoral Bonds are paid in all the years,highest number of unpaid Electoral Bonds are present in the year 2019, 2023 and then 2024.

# #### (d) Monthly Status of the Electoral Bonds Purchased

# In[59]:


party_bonds_monthly_status_df = party_bonds_df.groupby(party_bonds_df['Date_of_Purchase'].dt.to_period('M'))['Status'].value_counts().unstack()


# In[60]:


party_bonds_monthly_status_df


# The graphical visualiztion of the above data is given as following:

# In[61]:


party_bonds_monthly_status_df.plot(kind='bar', 
                                  figsize=(10, 6),
                                  xlabel = 'Year of Purchase', 
                                  ylabel = 'Number of Electoral Bonds',
                                  title = 'Status(Paid/Expired) of Electoral Bonds Purchased on Monthly Basis');


# ### Analysis of the Barplot
# 
# The barplot depicts the number of electoral bonds purchased on a monthly basis, categorized by their status as either "Paid" or "Expired". Here are some observations and potential reasons behind the patterns:
# 
# 1. **High Peaks of Purchases:**
#    - There are noticeable peaks in the number of purchased bonds during certain months, such as:
#      - April 2019
#      - July 2019
#      - January 2022
#      - March 2023
#    - **Reason:** These peaks likely correspond to periods leading up to significant political events such as elections. During such times, political parties might be more active in fundraising and thus purchase more electoral bonds.
# 
# 2. **Dominance of "Paid" Bonds:**
#    - The majority of the bonds are categorized as "Paid" rather than "Expired".
#    - **Reason:** Electoral bonds are typically meant to be used within a specific period. The dominance of "Paid" bonds indicates that most bonds are being utilized within their valid period, reflecting efficient use by political parties for their intended purpose (e.g., election campaigns).
# 
# 3. **Low Number of "Expired" Bonds:**
#    - The number of "Expired" bonds is minimal compared to "Paid" bonds.
#    - **Reason:** This suggests that the purchasers of the bonds (likely political parties or supporters) are aware of the bond's expiration terms and ensure that they are used before they expire. This also indicates effective financial management within these organizations.
# 
# 4. **Election Year Influence:**
#    - The spikes in bond purchases in specific months could align with state or national election timelines. For instance:
#      - The peak in April 2019 aligns with the general elections in India held during April-May 2019.
#      - The increase in January 2022 could be related to preparations for state elections in early 2022.
#      - March 2023 might be associated with upcoming elections or by-elections.
#    - **Reason:** Political parties ramp up their campaign efforts and financial inflows through donations during election years, resulting in increased purchases of electoral bonds.
# 

# ## (2) Purchaser Analysis:
# 
# - Identifying the top purchasers (individuals or entities) of electoral bonds.
# - Analyzing the distribution of purchases among different purchasers.
# - Investigate any patterns or trends in purchasing behavior.

# ### (2.1) Identifying the top purchasers (individuals or entities) of Electoral Bonds.

# #### (a) Identifying the top 100 Purchasers (individuals or entities) of Electoral Bonds:
# 
# Identifying the amount (in Crores) worth of Electoral Bonds purchased by each Purchaser:

# In[62]:


party_bonds_purchasers_df = party_bonds_df.groupby('Name_of_the_Purchaser')[['Crore']].sum()


# In[63]:


party_bonds_purchasers_df


# Arranging the purchasers in the order from highest amount purchases to lowest amount purchases worth of Electoral Bonds for various Political Parties:

# In[64]:


party_bonds_purchasers_df.sort_values(by='Crore', ascending = False)


# Identifying the top 100 Purchasers of Electoral Bonds:

# In[65]:


top_100_bond_purchasers_df = party_bonds_purchasers_df.sort_values(by='Crore', ascending = False).head(100)


# In[66]:


from IPython.display import display
with pd.option_context('display.max_rows', 100):
    display(top_100_bond_purchasers_df)


# #### (b) Visualization of top 10 Purchasers of Electoral Bonds in the form of a Bar Graph:

# In[67]:


top_10_bond_purchasers_df = party_bonds_purchasers_df.sort_values(by='Crore', ascending = False).head(10)


# In[68]:


top_10_bond_purchasers_df


# The visualization of the above data is given as following:

# In[259]:


plt.figure(figsize=(12, 6))
plt.ylabel('Amount (in Crores)')
plt.xlabel('Name of Purchaser')
plt.title('Top 10 Purchasers of Electoral Bonds')
plt.xticks(rotation=90)

plt.bar(top_10_bond_purchasers_df.index, top_10_bond_purchasers_df.Crore);


# ### (2.2) Analyzing the Distribution of Purchases among Different Purchasers
# 
# The distribution of Electoral Bond Purchase analysis is done for `VEDANTA LIMITED` company, sinmnilar analysis can be done for other companies as well.

# #### VEDANTA LIMITED

# In[70]:


VEDANTA_party_bonds_df = party_bonds_df[party_bonds_df.Name_of_the_Purchaser == 'VEDANTA LIMITED' ]


# In[71]:


VEDANTA_party_bonds_df


# #### (a) Amount (in Crore) worth of Electoral Bonds purchased annualy by `VEDANTA LIMITED`

# In[72]:


VEDANTA_purchase_amount_annualy_df = VEDANTA_party_bonds_df.groupby(VEDANTA_party_bonds_df['Date_of_Purchase'].dt.to_period('Y'))['Crore'].sum()


# In[73]:


VEDANTA_purchase_amount_annualy_df


# The visual representation of the above data is given as following:

# In[74]:


VEDANTA_purchase_amount_annualy_df.plot(kind='bar', 
                               figsize=(10, 6),
                               color = 'blue',
                               xlabel = 'Year of Purchase', 
                               ylabel = 'Amount (in Crore)',
                               title = 'Amount (in Crore) worth of Electoral Bonds purchased annualy by VEDANTA LIMITED');


# ### Analysis of the Barplot
# 
# The barplot shows the amount (in crores) of electoral bonds purchased annually by Vedanta Limited from 2019 to 2023. Here are the observations and potential reasons behind the trends:
# 
# 1. **2019:**
#    - Vedanta Limited purchased around 50 crores worth of electoral bonds.
#    - **Reason:** This was a general election year in India (Lok Sabha elections held in April-May 2019). Companies often increase political contributions during election years to gain favor or support from political parties.
# 
# 2. **2020:**
#    - There is no recorded purchase of electoral bonds by Vedanta Limited.
#    - **Reason:** This could be due to the absence of significant elections or political events in 2020. Additionally, the COVID-19 pandemic might have caused a shift in financial priorities, leading to a temporary halt in such expenditures.
# 
# 3. **2021:**
#    - Vedanta Limited's purchase of electoral bonds resumed but at a lower level, around 20 crores.
#    - **Reason:** This was a year of recovery from the pandemic. The lower amount could indicate cautious spending, focusing on stabilizing operations while still maintaining some level of political contribution.
# 
# 4. **2022:**
#    - A significant spike in purchases, with over 250 crores worth of electoral bonds bought by Vedanta Limited.
#    - **Reason:** Several state elections were held in 2022, including key states like Uttar Pradesh, Punjab, Goa, Uttarakhand, and Manipur. Companies typically increase political donations during state elections to support parties and candidates who can influence regional policies and business environments. The substantial increase indicates Vedanta's strategic investment in gaining political goodwill during these elections.
# 
# 5. **2023:**
#    - Purchases decreased to around 50 crores.
#    - **Reason:** While there might not have been as many significant elections as in 2022, the amount is still notable. It suggests ongoing, albeit reduced, political engagement. Companies often maintain a baseline level of contributions to stay connected with political entities, even in non-election years.
# 

# #### (b) Amount (in Crore) worth of Electoral Bonds purchased monthly by `VEDANTA LIMITED`

# In[75]:


VEDANTA_purchase_amount_monthly_df = VEDANTA_party_bonds_df.groupby(VEDANTA_party_bonds_df['Date_of_Purchase'].dt.to_period('M'))['Crore'].sum()


# In[76]:


VEDANTA_purchase_amount_monthly_df


# The visual representation of the above data is given as following:

# In[132]:


VEDANTA_purchase_amount_monthly_df.plot(kind='bar',  
                               figsize=(10, 6),
                               color = 'seagreen',
                               xlabel = 'Year of Purchase', 
                               ylabel = 'Amount (in Crore)',
                               title = 'Amount (in Crore) worth of Electoral Bonds purchased monthly by VEDANTA LIMITED');


# ### Key Observations
# 
# #### 1) High Peaks:
# 
# * **Early 2022**: There's a significant peak in the purchase amount, nearly 100 crores.
# * **Late 2022:** Another peak, also over 100 crores, indicating heavy purchasing activity during these periods.
# 
# #### 2) Moderate Peaks:
# 
# * **Early 2019:** The amount is around 40 crores.
# * **Mid 2023**: There's another noticeable peak, albeit lower than those in 2022, indicating a consistent pattern of higher purchasing activity during certain times.
# 
# #### 3) Low Points:
# 
# * **Late 2019:** The purchase amounts drop significantly, indicating minimal purchasing activity.
# * **2021:** There's a gradual increase, but the amounts remain relatively low compared to 2022.
# 
# The graph shows significant peaks and troughs in Vedanta Limited's electoral bond purchases. High purchase amounts in 2022 suggest strategic donations aligned with political such as the ongoing state elections at that time or financial strategies.

# #### (c) Distribution of funds from `VEDANTA LIMITED` to different political parties

# Identifying the distribution of funds (ie Electoral Bonds) from `VEDANTA LIMITED` to different Political Parties and amount (in Crore) worth of Electoral Bonds received by each Political Party

# In[78]:


VEDANTA_bonds_party_distribution = VEDANTA_party_bonds_df.groupby('Name_of_the_Political_Party')['Crore'].sum()


# In[231]:


VEDANTA_bonds_party_distribution_df = VEDANTA_bonds_party_distribution.reset_index()


# In[232]:


VEDANTA_bonds_party_distribution


# The visual representation of the above data is given as folowing in the form of `bar-plot` and  `pie-chart`:

# In[261]:


VEDANTA_bonds_party_distribution.plot(kind='bar', 
                               figsize=(12, 6),
                               xlabel = 'Name of Political Party', 
                               ylabel = 'Amount (in Crore)',
                               title = ' Distribution of funds from VEDANTA LIMITED to different Political Parties');


# In[219]:


VEDANTA_bonds_party_distribution.plot(kind='pie', 
                               figsize=(8, 8),
                               title = ' Distribution of funds from VEDANTA LIMITED to different Political Parties');


# The bar chart illustrates the distribution of funds from Vedanta Limited to various political parties in India, measured in crores of rupees. Here are some key observations and potential reasons behind the distribution:
# 
# ### Observations:
# 1. **Bharatiya Janata Party (BJP)** received the highest amount of funding, significantly more than any other party, with over 200 crores.
# 2. **All India Trinamool Congress (AITC)** is the second highest recipient, receiving around 100 crores.
# 3. **Bharat Rashtra Samithi (BRS)** and **Indian National Congress (INC)** also received substantial amounts, around 50 crores and 45 crores respectively.
# 4. Other parties such as **Biju Janata Dal (BJD)**, **Dravida Munnetra Kazhagam (DMK)**, **Shiv Sena**, **Maharashtra Pradesh Congress Committee**, and **Telugu Desam Party (TDP)** received minimal to no funding compared to the top recipients.
# 
# ### Reasons Behind the Distribution:
# 1. **Political Influence and Reach**:
#    - The BJP, being the ruling party at the national level and having a vast political reach across India, is likely to attract more corporate donations. Companies might expect favorable policies or a stable business environment in return for their contributions.
#    - The AITC, which has strong influence in West Bengal, is a significant regional player, hence it might receive substantial funding due to its dominance in the state.
# 
# 2. **Strategic Contributions**:
#    - Companies like Vedanta may distribute funds strategically to parties they perceive as influential or having potential to govern, thus securing their business interests.
#    - By funding multiple parties, especially the prominent ones, companies may be hedging their bets to ensure good relations regardless of which party comes to power.
# 
# 3. **Electoral Performance and Prospects**:
#    - Funding often correlates with a party's past electoral performance and future prospects. Parties with a higher likelihood of winning elections receive more funding as businesses seek to align with the future government.
# 
# 4. **Regional Dynamics**:
#    - The significant funding to the AITC and BRS indicates Vedanta’s interest in key regional players, especially in states where these parties have considerable influence.
#    - Lesser funding to parties like DMK, TDP, and others may reflect their regional constraints or lower likelihood of influencing national-level policies.
# 
# 5. **Policy and Ideological Alignment**:
#    - Businesses often support parties whose policies are more business-friendly or whose ideological stance aligns with their interests. The BJP’s policies, for example, may be perceived as more favorable to big businesses.
# 
# In summary, the distribution of funds from Vedanta Limited to various political parties likely reflects a combination of these parties' political influence, strategic importance, electoral prospects, and alignment with the company's business interests.

# #### (d) The denominations of the bonds purchased by `VEDANTA LIMITED`

# (i) Identifying the types of denominations of Electoral Bonds purchased by `VEDANTA LIMITED`

# In[81]:


VEDANTA_party_bonds_df['Denominations'].unique()


# The above result shows that `VEDANTA LIMITED` has bought only 1,00,00,000, 10,00,000 and 1,00,000 denominationS Electoral Bonds

# (ii) Now identifying the number of 1,00,00,000 denomination Electoral Bonds bought by `FUTURE GAMING AND HOTEL SERVICES PR`

# In[82]:


VEDANTA_bonds_denomination_distribution = VEDANTA_party_bonds_df['Denominations'].value_counts()


# In[83]:


VEDANTA_bonds_denomination_distribution


# The visual representation is given as following:

# In[86]:


plt.title('Denominations of the bonds purchased by VEDANTA LIMITED')

sns.countplot(y=VEDANTA_party_bonds_df['Denominations']);


# From the above graph we can clearly see that, The electoral bonds purchased by `VEDANTA LIMITED` are in the denominations of only 1,00,00,000; 10,00,000 and 1,00,000. The maximum number of denominations are in the form of 1,00,00,000 denomination ie 398 of them, 26 of 10,00,000 denomination and lastly 5 of 1,00,000 denomination.

# ### (2.3) Investigating any patterns or trends in purchasing behavior.

# The frequency of purchase of Electoral Bonds by `VEDANTA LIMITED` is obtained in order to investgate any patterns or trends in purchasing behaviour:

# In[87]:


VEDANTA_purchase_frequency_df = VEDANTA_party_bonds_df.groupby(VEDANTA_party_bonds_df['Year_of_Purchase'])['Month_of_Purchase'].value_counts().unstack()


# In[88]:


VEDANTA_purchase_frequency_df


# The visual representation of the above data is given as following:

# In[89]:


VEDANTA_purchase_frequency_df.plot(kind='bar', 
                                           figsize=(10, 6),
                                           stacked = True,
                                           xlabel = 'Year of Purchase', 
                                           ylabel = 'Number of Electoral Bonds',
                                           title = 'Frequency of purchase of Electoral Bonds by VEDANTA LIMITED');


# The bar chart displays the frequency of electoral bond purchases by Vedanta Limited from 2019 to 2023, segmented by the month of purchase. Here is a detailed analysis and summary:
# 
# ### Observation:
# 1. **2019**: Vedanta Limited purchased around 50 electoral bonds, with purchases distributed across April, May, and October.
# 2. **2020**: There were no recorded purchases of electoral bonds by Vedanta Limited.
# 3. **2021**: A modest number of bonds were purchased, with activity only in April.
# 4. **2022**: This year saw a significant spike in purchases, with over 250 bonds bought. The purchases were spread across January, April, October, and November, with a substantial amount in November.
# 5. **2023**: There was a noticeable decrease compared to 2022, but still a relatively high number of purchases compared to previous years except for 2022. Purchases were made in April, July, October, and November.
# 
# ### Reasons Behind the Distribution:
# 1. **Election Cycle Influence**:
#    - The spike in 2022 could be correlated with important elections or anticipated political events. Major elections, such as state assembly elections, might have prompted Vedanta Limited to increase its contributions to political parties via electoral bonds.
#    - In India, many state elections were held in 2022, including Uttar Pradesh, Punjab, Uttarakhand, Manipur, and Goa. These states are significant in terms of political influence, likely prompting increased funding activities.
# 
# 
# The data indicates that Vedanta Limited's purchases of electoral bonds are significantly influenced by the political and electoral calendar, with notable increases during election years. The pattern of purchases also suggests strategic planning aligned with financial cycles and possibly regulatory considerations. The absence of purchases in 2020 and the significant spike in 2022 reflect a tactical approach to political contributions, likely driven by key electoral events and strategic objectives.

# ## (3) Political Party Funding Analysis:
# 
#    - Examining the distribution of funding among different political parties and Analyze the financial impact of electoral bonds on political parties.
#    - Analyzing the timing and frequency of bond purchases by political parties.
#    - Analyzing the amount (in Crores) of Electoral Bond Purchases for associated Political Parties in a particular year on monthly basis

# ### (3.1) Examining the distribution and comparison of funding among different political parties.

# Listing down all the political parties associated with funding from Electoral Bonds:

# In[90]:


party_bonds_df['Name_of_the_Political_Party'].unique()


# Total amount (in Crores) worth of Electoral Bonds received by each Political Party is shown as following:

# In[91]:


partywise_fund_distribution_df = party_bonds_df.groupby('Name_of_the_Political_Party')['Crore'].sum()


# In[92]:


partywise_fund_distribution_df


# The visual representation of the above data is given as following:

# In[263]:


partywise_fund_distribution_df.plot(kind='bar',
                                    figsize=(12, 6),
                                    xlabel = 'Political Party', 
                                    ylabel = 'Amount (in Crores)',
                                    title = 'Distribution of Funding among Different Political Parties');


# ### Observations:
# 1. **Highest Funds**:
#    - **Bharatiya Janata Party (BJP)** has the highest declared funds with ₹3939.9440 crores.
#    - **President, All India Congress Committee** follows with ₹2104.3190 crores.
# 
# 2. **Significant Funds**:
#    - **All India Trinamool Congress** and **Bharat Rashtra Samithi** have significant funds with ₹2342.1428 crores and ₹1574.5861 crores respectively.
# 
# 3. **Moderate Funds**:
#    - Parties like **Biju Janata Dal**, **Dravida Munnetra Kazhagam (DMK)**, and **YSR Congress Party** have funds ranging from ₹500 to ₹600 crores.
# 
# 4. **Low Funds**:
#    - Several parties have relatively low funds, such as **ADYAKSHA SAMAJVADI PARTY**, **ALL INDIA ANNA DRAVIDA MUNNETRA KAZHAGAM**, and **JANASENA PARTY**, with funds less than ₹10 crores.
# 
# 5. **Unknown/Not Encashed**:
#    - There is an entry "Not encashed" with ₹0.1528 crores and "unknown" with ₹11.0271 crores.
# 
# ### Reasons Behind Observations:
# 1. **Party Popularity and Influence**:
#    - Major national parties like BJP and Congress have higher funds due to their larger support bases, more extensive fundraising networks, and greater influence both nationally and internationally.
# 
# 2. **State-Level Dominance**:
#    - Parties like All India Trinamool Congress and Bharat Rashtra Samithi have significant funds reflecting their dominance in states like West Bengal and Telangana, respectively.
# 
# 3. **Funding Sources**:
#    - The funds declared by political parties come from various sources, including donations from individuals, corporations, membership fees, and electoral bonds. Major parties tend to attract more substantial donations due to their potential influence on policy and governance.
# 
# This analysis provides insight into the financial strength and support base of different political parties in India.

# ### (3.2) Analyzing the timing of bonds purchased to be funded to Political Parties (along with current status)
# 
# Here the analysis for timing of bonds purchased to be funded to Political Parties is done also showing the status of the bond purchased ie either it is `Paid` or `Expired`

# In[177]:


plt.figure(figsize = (10, 10))

sns.scatterplot(x ='Date_of_Purchase', 
                y ='Name_of_the_Political_Party', 
                hue = 'Status', 
                data = party_bonds_df,
                s = 80);

plt.xlabel('Date of Purchase')
plt.ylabel('Name of Political Parties')
plt.title('Timing of Electoral Bond Purchases for associated Political Parties');


# ### Observations from the Electoral Bond Purchase Timing Chart:
# 
# 1. **High Frequency of Purchases**:
#    - **Bharatiya Janata Party (BJP)**, **All India Trinamool Congress**, and **President, All India Congress Committee** have a high frequency of bond purchases spread consistently over the years from 2019 to 2024.
# 
# 2. **Clustering of Purchases**:
#    - Certain parties like **BJP**, **Trinamool Congress**, and **President, All India Congress Committee** have clustering of bond purchases around specific periods, possibly correlating with election cycles.
# 
# 3. **Expired Bonds**:
#    - The orange dots represent expired bonds. Notably, **BJP**, **All India Trinamool Congress**, and **President, All India Congress Committee** show several expired bonds, indicating either unutilized bonds or delays in encashment.
#    - **Biju Janata Dal** and **Dravida Munnetra Kazhagam (DMK)** also have instances of expired bonds, though less frequently.
# 
# 4. **Sporadic Purchases**:
#    - Smaller or regional parties such as **Goa Forward Party**, **Janasena Party**, and **Jharkhand Mukti Morcha** have sporadic purchases indicating lower or more irregular funding through electoral bonds.
# 
# 5. **Inconsistent Reporting**:
#    - The "unknown" and "Not encashed" entries indicate some discrepancies or issues with reporting and encashment of electoral bonds.
# 
# ### Reasons Behind Observations:
# 
# 1. **Election Cycles**:
#    - The clustering of bond purchases around specific periods likely corresponds to major election cycles (general elections, state elections) where parties need increased funding for campaigning.
# 
# 2. **Party Influence and Reach**:
#    - Major parties like BJP and Congress, along with influential regional parties like Trinamool Congress, have a broader donor base and thus higher frequency and volume of bond purchases.
# 

# ### (3.3) Analyzing the amount(in Crore) and frequency of Electoral Bond Purchases for Political Parties

# #### (a) Analyzing the Amount (in Crore) of Electoral Bond Purchases for associated Political Parties (2023)

# In[148]:


party_bonds_2023_df = party_bonds_df[party_bonds_df.Year_of_Purchase == 2023]


# In[149]:


purchase_timing_2023_df = party_bonds_2023_df.groupby(['Month_of_Purchase', 'Name_of_the_Political_Party'])['Crore'].sum().unstack().fillna(0)


# In[150]:


purchase_timing_2023_df


# In[264]:


purchase_timing_2023_df.plot(kind='bar', figsize=(14, 8), stacked = True);

plt.title('Amount of Bond Purchases for Political Parties')
plt.xlabel('Month of Purchase (2023)')
plt.ylabel('Amount Contributed (in Crores)')
plt.xticks(rotation=0)
plt.legend(title='Political Party', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()


# ### Observations:
# 
# 1. **Peak Contributions**: 
#    - Significant peaks in bond purchases are observed in April, July, and November 2023, suggesting these months are key periods for political funding, likely due to upcoming elections or major political events.
# 
# 2. **Major Recipients**:
#    - The **Bharatiya Janata Party (BJP)** and **President, All India Congress Committee** are prominent recipients, indicated by their larger contributions, especially during the peak months.
# 
# 3. **Diverse Contributions**:
#    - Several other parties, including **All India Trinamool Congress**, **Bharat Rashtra Samithi**, and **Dravida Munnetra Kazhagam (DMK)**, also show significant contributions, reflecting a diverse political funding landscape.
# 
# 4. **Smaller Contributions**:
#    - Smaller parties such as **Goa Forward Party** and **Janasena Party** have comparatively smaller contributions, which are spread more thinly across the months.
# 
# 5. **Electoral Bond Activity**:
#    - The distribution of contributions across different months indicates active participation in the electoral bond scheme, with varying degrees of engagement from different political parties.
# 
# These trends highlight the strategic timing of electoral bond purchases aligned with political needs and activities throughout the year.

# #### (b) Analyzing the Frequency of Electoral Bond Purchases for associated Political Parties (2023)

# In[174]:


purchase_frequency_2023_df = party_bonds_2023_df.groupby(['Year_of_Purchase', 'Name_of_the_Political_Party'])['Crore'].value_counts().unstack()


# In[175]:


purchase_frequency_2023_df


# In[176]:


purchase_frequency_2023_df.plot(kind='bar', stacked = True);

plt.title('Frequency of Bond Purchases for Political Parties')
plt.xlabel('Month of Purchase (Year 2023)')
plt.ylabel('No. of Electoral Bonds')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()


# The above data gives the frequency of bond purchases that are associated with Political Parties in the year 2023, showing major bond purchases for the maor big parties and less amount of bond purchases for smaller parties.

# ## (4) Financial Analysis:
# 
#    - Calculate the total amount of money involved in electoral bond transactions.
#    - Examine the distribution of bond amounts in crore.
#  

# ### (4.1) Calculate the total amount of money involved in electoral bond transactions.

# To obtain the total amount of money involved in Electoral Bond transactions, we obtain the `sum` of the `Crore` column:

# In[101]:


Total_crores = party_bonds_df['Crore'].sum()


# In[102]:


Total_crores


# In[103]:


Total_amount_in_Rupees = Total_crores * 10000000


# In[104]:


Total_amount_in_Rupees


# In[105]:


print("Total amount of money involved in electoral bond transactions is: Rs. {}".format(Total_amount_in_Rupees))


# ### (4.2) Examine the distribution of Bond Amounts in Crore.

# Here we are examining the distribution of bond amount in crores among different political parties:

# In[106]:


bond_amount_distribution_crore_df = party_bonds_df.groupby('Name_of_the_Political_Party')['Crore'].value_counts().unstack()


# In[107]:


bond_amount_distribution_crore_df 


# The visual representation of the above data is given as following:

# In[108]:


bond_amount_distribution_crore_df.plot(kind='bar', 
                                       figsize=(10, 6),
                                       stacked = True,
                                       xlabel = 'Name of Political Party', 
                                       ylabel = 'Number of Electoral Bonds',
                                       title = 'Distribution of Bond Amounts in Crore');


# ### Observations:
# 
# 1. **Bharatiya Janata Party (BJP)** has the highest expenditure, especially in the highest bracket of 1 crore, with a total expenditure of 3765.0 crores. This indicates a significant financial capacity, likely due to extensive fundraising, donations, and possibly government support given their dominant political position.
# 
# 2. **Indian National Congress (INC)** also shows substantial expenditure, particularly in the highest bracket of 1 crore, amounting to 2039.0 crores. Despite losing ground to BJP in recent years, INC still remains a major political force with considerable financial resources.
# 
# 3. **All India Trinamool Congress (AITC)**, with 2252.0 crores in the highest bracket, reflects its strong regional influence in West Bengal and active campaigning strategies.
# 
# 4. **Regional Parties** such as Dravida Munnetra Kazhagam (DMK), Biju Janata Dal (BJD), and others show significant expenditures but on a smaller scale compared to BJP and INC. This reflects their focus on state-level politics where they hold substantial influence.
# 
# 5. **Smaller Parties** like Goa Forward Party, Jana Sena Party, and others exhibit much lower expenditures, reflecting their limited financial resources and smaller political reach.
# 
# 6. **Expenditure Concentration**: Most parties have their highest expenditures in the 1 crore bracket, indicating high-cost campaign strategies aimed at large-scale voter outreach, advertising, and rallies.
# 
# 7. **NaN Values**: Several parties have NaN values in lower brackets, suggesting either no reported expenditure or negligible amounts in these categories, indicating a focus on larger, more impactful spending.
# 
# ### Reasons Behind the Observations:
# 
# - **Fundraising Capability**: Larger parties like BJP and INC have better fundraising capabilities through corporate donations, member contributions, and public support, allowing for higher expenditure.
# - **Campaign Strategy**: High expenditure in the 1 crore bracket signifies a strategic focus on large-scale, high-impact campaigns which require substantial financial outlays.
# - **Political Influence and Reach**: Parties with national influence (BJP, INC) naturally have higher expenditures compared to regional parties, reflecting their broader political ambitions and activities across the country.
# - **Regulatory and Reporting Practices**: The absence of data (NaN) in some brackets may reflect variations in how parties report their finances or possibly gaps in data collection and transparency.
# 
# 

# # Conclusion

# ### Conclusion for EDA Project on Electoral Bonds
# 
# The exploratory data analysis (EDA) on electoral bonds provided valuable insights into various aspects of the bond transactions, purchasers, political party funding, and financial impact. Here are the key conclusions drawn from the analysis:
# 
# 1. **Electoral Bond Transactions Analysis**:
#    - The distribution of bond denominations revealed a preference for higher-value bonds, indicating a trend towards significant financial contributions.
#    - The analysis of purchase frequency and timing highlighted peaks during specific periods, likely corresponding to election cycles or political events.
#    - Investigating the status of bonds showed a high rate of redemption, suggesting active engagement by political entities with the funds received.
#    - Over time, trends in bond status exhibited increased activity during election years, with noticeable patterns in the issuance and redemption rates.
# 
# 2. **Purchaser Analysis**:
#    - Identified top purchasers included both individuals and corporate entities, with certain players consistently appearing as significant contributors.
#    - The distribution of purchases among different categories of purchasers indicated a concentration among a few high-value donors.
#    - Patterns in purchasing behavior showed strategic timing aligned with political events, hinting at coordinated funding efforts.
# 
# 3. **Political Party Funding Analysis**:
#    - The distribution of funding among political parties highlighted disparities, with major parties receiving the bulk of contributions.
#    - Timing and frequency analysis of bond purchases revealed synchronized funding efforts, particularly around election periods, demonstrating the strategic importance of electoral bonds.
#    - Monthly analysis of funding amounts underscored significant spikes in contributions during critical months, reflecting the intense fundraising efforts during election campaigns.
# 
# 4. **Financial Analysis**:
#    - The total amount of money involved in electoral bond transactions was substantial, emphasizing the importance of this funding mechanism in the political landscape.
#    - The distribution of bond amounts showed a skew towards higher denominations, pointing towards significant individual contributions rather than widespread small donations.
# 
# ### Overall Conclusion:
# 
# The EDA on electoral bonds underscores the critical role these instruments play in political funding in India. The findings reveal strategic behaviors by donors and recipients, with significant financial flows aligned with electoral cycles. This analysis provides a foundation for understanding the dynamics of political financing and highlights areas for further investigation, such as the impact of these funding patterns on electoral outcomes and policy decisions. The insights gained can inform policymakers, political analysts, and the public about the financial underpinnings of political campaigns and the influence of money in politics.

# In[ ]:




