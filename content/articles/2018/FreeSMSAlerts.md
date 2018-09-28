Title: How to get Trading view Alerts by sms for free
Date: 2018-09-17 12:19
Modified: 2018-09-17 12:19
Category: Trading
Tags: Tradingview, sms, gmail

## **Introduction**


This will be the first post in our new blog! Today i am going to show how we can recieve alerts created on [Trading view](https://www.tradingview.com/) by sms directly on your mobile phone for free. At the time of this writing, trading view only sends email and email-to-sms alerts for free while the sms alerts are reserved for premium subscribers only. The rest of us minions have to fork out a hefty fine for the premium plan or make do with email alerts.

But why do we even need sms alerts when we can get the same information by email ?  Well, in trading, especially if you trade intra day, you might not always be in front of your computer to follow the charts so most traders set alerts to monitor movements in the market. If we get only email alerts or email-to-sms alerts, this leaves us checking our email every minute just to see if we have an alert!!! Hardly practical. Now i will not go into detail into what happens when you are on the road or without email access or having lunch at a fancy resturant, let's just say that you always want to be alerted as soon as the market moves. So we need our alerts to delivered as an sms messages to our mobile phone. This method in my view is easier to stay connected to the market than to always be opening an email box and checking for an alert.

# **Setup the alert first!**


##Insert indicator on chart
Lets say we went to be alert on a MA cross between the 5-period moving average and the 55-period exponential moving average on the 1hr EUR-USD chart. First we set-up our chart in trading view by including all the required indicators as shown below:

![Insert indicator on chart]({filename}/images/eurusdIndicators.png){.img-center}

## Create the alerts based on the indicator
Choose the alert condition, in the image below we have chosen to be alerted when ever there is cross between the MA-5 and the EMA-55 on the 1hr EUR-USD chart. We set our alert to go off once per minute since we want to continually test this condition every minute  You can also choose Once-Per-Bar Close  but this causes the alert to be triggered only after the bar closes. Set the Alert actions to Email-to-sms, this is the most important part. Email-to-sms is a free service on [Trading view](https://www.tradingview.com/) that let's send your alerts to an email which you have chosen in your profile. The email message can be customized by editing the message field and is sent in plain text removing all the clutter and images in a simple E-mail alert. We propose that you set-up a [gmail](https://www.gmail.com/) account for reciving these Email-to-sms alerts as our tutorial is based on reading our email using google scripts in real-time.

![Create Alerts based on indicator]({filename}/images/createalert.png){.img-center}

Now that we have our Alerts running and we see our alerts delivered as email messages but we need to have them delivered to our mobile phone. Several options exist:

# **Forward Email alerts to mobile phone**


##1. First Case: Deliver Alerts by MMS

Multi-media messaging services (MMS) are usually available on most network carriers. This method requires us to label the email alerts that we recieve from trading view and then forward the same message by mms to our mobile phone. We will assume that your network carrier is not blocking you from recieving MMS for free (I have seen this in 2018!!!). On gmail we click on **Settings** > **Forwarding and POP/IMAP** > **Add a forwarding address**. Here you have to input your Mobile Message Gateway usually in the format;  **number@mms.operatorgateway.com**.  This is an email to which gmail forwards email messages and you recieve this as an MMS message in your mobile phone. Your mobile carrier has to activate this feature for it to work and provide you with a mobile message gateway for you recieve these emails.

##2. Create a label in gmail and forward emails to the MMS gateway

In gmail click **Settings** > **Filters and Blocked Addresses** > **Create a new filter**
![Create a label in gmail]({filename}/images/createfilter.png){.img-center}

In the **From** field of the form that we are presented, we write the [email address used by Trading view](noreply@tradingview.com) to send us alerts. This email might change from time to time just look at the sender email and include it in this field to identify the sender and click  **Create filter with this search** at the bottom right of this form.

From the search results we will be presented with a form for actions to perform on a message matching the search. Select the check box **Apply Label** and click **Choose label**. A drop-down menu is presented and we create a label by choosing **New Label**. Set name the label as **tradingview** or to another name of your choice. Select the check box **Forward it** and here select the forwarding address previously created and click **Create filter** to finish the process.

![Create a label in gmail]({filename}/images/labeltradingview.png){.img-center}

# Conclusion

Now the label just tags all emails we recieve from Tradingview and forwards them to our phone by MMS. A list of message gateways for some mobile phone carriers can be found [here](https://kb.sandisk.com/app/answers/detail/a_id/17056/~/list-of-mobile-carrier-gateway-addresses) at the time of this writing. Please note that the forward address has to be verified to become activated by typing the code recieved from gmail to your mobile phone via MMS.

