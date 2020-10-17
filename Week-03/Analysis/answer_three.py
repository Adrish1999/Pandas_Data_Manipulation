#Question 3
#What is the average GDP over the last 10 years for each country? (exclude missing values from this calculation.)

#This function should return a Series named avgGDP with 15 countries and their average GDP sorted in descending order.


def answer_one():
    energy = pd.read_excel('Energy Indicators.xls',skiprows=1,skipfooter=1)
    energy = energy.drop(['Unnamed: 0','Unnamed: 1'],axis=1)
    for i in range(len(energy.index)):
        if((i >= 0 and i <= 15) or (i >= 243 and i <= 279)):
            energy = energy.drop(i)
    energy = energy.reset_index()
    energy = energy.drop(['index'] , axis=1)
    energy = energy.rename(columns = {'Environmental Indicators: Energy':'Country', 'Unnamed: 3':'Energy Supply', 
                              'Unnamed: 4':'Energy Supply per Capita','Unnamed: 5':'% Renewable'}) 
    energy['Country'] = energy['Country'].str.replace('\d+', '')
    energy['Country'] = energy['Country'].str.replace(r" \(.*\)","")
    energy['Country'] = energy['Country'].replace({"Republic of Korea": "South Korea","United States of America": "United States","United Kingdom of Great Britain and Northern Ireland": "United Kingdom","China, Hong Kong Special Administrative Region": "Hong Kong"})
    energy['Energy Supply'] *= 1000000 
    energy = energy.replace('\.+', np.nan, regex=True)
    GDP = pd.read_csv('world_bank.csv', skiprows=4)
    GDP = GDP.rename(columns={'Country Name': 'Country'})
    GDP['Country'] = GDP['Country'].replace({"Korea, Rep.": "South Korea", "Iran, Islamic Rep.": "Iran","Hong Kong SAR, China": "Hong Kong"})
    ScimEn = pd.read_excel('scimagojr-3.xlsx')

    df = pd.merge(pd.merge(energy, GDP, on='Country'), ScimEn, on='Country')
    df = df.set_index('Country')
    df = df[['Rank', 'Documents', 'Citable documents', 'Citations', 'Self-citations', 'Citations per document', 'H index', 'Energy Supply', 'Energy Supply per Capita', '% Renewable', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015']]
    df = (df.loc[df['Rank'].isin([i for i in range(1, 16)])])
    df = df.sort('Rank')
    return df
    
 
def answer_three():
    Top15 = answer_one()
    rows = ['2006', '2007', '2008',
           '2009', '2010', '2011', '2012', '2013', '2014', '2015']
    Top15["avgGDP"] = Top15[rows].mean(axis=1)
    return Top15.sort_values("avgGDP",ascending=False)["avgGDP"]
answer_three()
