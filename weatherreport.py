from email import message
import json
import urllib.request
import smtplib, ssl

API="rHW4KYrE9Hpig5gnoDui6JnJyvlGMPmg"
CountryCode="IN"
City="Bengaluru"
Key ="204108"

def getForcast(location_key):
    daily_Forecast_Url = "http://dataservice.accuweather.com/forecasts/v1/daily/1day/"+location_key+"?apikey="+API+"&details=true&metric=true"
    with urllib.request.urlopen(daily_Forecast_Url) as daily_Forecast_Url:
        data = json.loads(daily_Forecast_Url.read().decode())
    for key1 in data['DailyForecasts']:
        date = key1['Date']
        min_Temperature=str(key1['Temperature']['Minimum']['Value'])
        max_Temperature = str(key1['Temperature']['Maximum']['Value'])
        air_Quality=str(key1['AirAndPollen'][0]['Category'])
        uv_Index = str(key1['AirAndPollen'][5]['Category'])
        day_Forecast = str(key1['Day']['LongPhrase'])
        wind_Speed = str(key1['Day']['Wind']['Speed']['Value'])
        wind_Gustspeed = str(key1['Day']['WindGust']['Speed']['Value'])  
    return date,min_Temperature,max_Temperature,air_Quality,uv_Index,day_Forecast,wind_Speed,wind_Gustspeed

date,min_Temperature,max_Temperature,air_Quality,uv_Index,day_Forecast,wind_Speed,wind_Gustspeed=getForcast(Key)

Forecast = "1-Day Weather forecast for Banglore on "+date
Forecast+= "\n Minimum Temperature(C) : "+min_Temperature
Forecast+= "\n Maximum Temperature(C) : "+max_Temperature
Forecast+="\n Air Quality : "+air_Quality
Forecast+="\n Uv Index : "+ uv_Index
Forecast+="\n Day Forecast : "+day_Forecast
Forecast+="\n Wind Speed : "+wind_Speed +" KM/H"
Forecast+="\n wind Gust Speed : "+wind_Gustspeed +" KM/H"


print(Forecast)

gmail_user = 'lucyrayala95@gmail.com'
gmail_password = 'Dhoni@183' 

sent_from = gmail_user
to = ['lucy.fireblast@gmail.com']   #Sumanjit.Saha@dell.com
subject = 'Weather forecast for the day'
body = Forecast

email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sent_from, ", ".join(to), subject, body)

try:
    smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    smtp_server.ehlo()
    smtp_server.login(gmail_user, gmail_password)
    smtp_server.sendmail(sent_from, to, email_text)
    smtp_server.close()
    print ("Email sent successfully!")
except Exception as ex:
    print ("Something went wrong….",ex)