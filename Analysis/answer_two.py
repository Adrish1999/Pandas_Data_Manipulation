#Question 2
#The previous question joined three datasets then reduced this to just the top 15 entries. When you joined the datasets, but before you reduced this to the top 15 items, how many entries did you lose?

#This function should return a single number.


def answer_two():
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
    df_1 = pd.merge(pd.merge(energy, GDP, on='Country'), ScimEn, on='Country')
    df_2 = pd.merge(pd.merge(energy, GDP, how = 'outer', on='Country'), ScimEn, how = 'outer', on='Country')
    return (len(df_2)-len(df_1))
answer_two()
