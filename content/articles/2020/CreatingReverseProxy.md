Title: Using Nginx Reverse proxy to host multiple services on a single public IP address and port
Date: 2020-11-25 10:09
Modified: 2020-11-25 10:09
Category: Software Developement
Tags: nginx, reverse proxy, virtual servers


I have recently run into a problem where i wanted to test updates to my static [website](www.yang2lalang.com). The website data is stored on [github](https://github.com/yang2lalang/blog) and it's domain name provided by [google](https://domains.google.com/). The changes to the website is done on a google compute engine instance using a jupyter notebook running on a public ip address. The whole idea is below:

1. Modify or Create website content in a markdown script in jupyter notebook.

2. Use pelican for site generation to compile the markdown script and other website content to HTML

```bash
pelican /path/to/your/content/
```

3. View website on [localhost](http://localhost:8080) or  [127.0.0.1](http://127.0.0.1:8080/) to see what it looks like before deployment

```bash
cd /path/to/your/content/
```

```bash
python -m SimpleHTTPServer 8080
```

First problem with the third step is that we were using a remote host on google cloud and to view the website changes we have to go on the public ip of the remote host on port 8080. 

Second problem which leads to the point of this article is that the port 8080 on the remote host is already in use by another service (Cloud 9 IDE). A bit of [search](https://serverfault.com/questions/624387/run-multiple-servers-on-the-same-port) revealed that we cannot host two services on the same public ip address and the same port except with reverse proxy. I also did not want to open a new port on the host, as i did not want several entry points to the host.

This article is to explain the steps i used to introduce reverse proxy using Nginx to use a single public ip address and port. It may also help me in the future to remebmber exactly what i did as i always forget :) 

We will assume that we have setup up two services: [A flask service that recieves signal from Trading view](http://localhost:8080) and [A Cloud 9 IDE service for software development](http://localhost:8080)


# **Setup the alert first!**


##Insert indicator on chart
Lets say we went to be alert on a MA cross between the 5-period moving average and the 55-period exponential moving average on the 1hr EUR-USD chart. First we set-up our chart in trading view by including all the required indicators as shown below:

![Insert indicator on chart]({filename}/images/eurusdIndicators.png){.img-center}

## Create the alerts based on the indicator
Choose the alert condition, in the image below we have chosen to be alerted when ever there is cross between the MA-5 and the EMA-55 on the 1hr EUR-USD chart. We set our alert to go off once per minute since we want to continually test this condition every minute  You can also choose Once-Per-Bar Close  but this causes the alert to be triggered only after the bar closes. Set the Alert actions to Email-to-sms, this is the most important part. Email-to-sms is a free service on [Trading view](https://www.tradingview.com/) that let's send your alerts to an email which you have chosen in your profile. The email message can be customized by editing the message field and is sent in plain text removing all the clutter and images in a simple E-mail alert. We propose that you set-up a [gmail](https://www.gmail.com/) account for reciving these Email-to-sms alerts as our tutorial is based on gmail features.

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

Now the label just tags all emails we recieve from Tradingview and forwards them to our phone by MMS. A list of message gateways for some mobile phone carriers can be found [here](https://kb.sandisk.com/app/answers/detail/a_id/17056/~/list-of-mobile-carrier-gateway-addresses) at the time of this writing. Please note that the forward address has to be verified to become activated by typing the code recieved from gmail to your mobile phone via MMS. In the next article, we show a special case where we can read and forward our emails by SMS using google scripts.

