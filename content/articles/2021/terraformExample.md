Title: How to get Trading view Alerts on your mobile phone for free
Date: 2021-10-28 13:42
Modified: 2021-10-28 13:42
Category: Infrastructure
Tags: AWS, terraform, deployment, IAAC


This post shows how to create an live running Apache webserver on [AWS](https://aws.amazon.com) using [terraform](https://terraform.io). The advantage of this method is to be able to use a repeatable method to spin up infrastructure for software deployment as the business grows. It also creates a clear, detailed  and easily transferrable information about the deployment architecture and the infrastructure in use at each point in time for any interested developer in the organization.

# **Setup the alert first!**


##Insert indicator on chart
Lets say we went to be alert on a MA cross between the 5-period moving average and the 55-period exponential moving average on the 1hr EUR-USD chart. First we set-up our chart in trading view by including all the required indicators as shown below:

![Insert indicator on chart]({filename}/images/eurusdIndicators.png){.img-center}

## Create the alerts based on the indicator
Choose the alert condition, in the image below we have chosen to be alerted when ever there is cross between the MA-5 and the EMA-55 on the 1hr EUR-USD chart. We set 

# Conclusion

Now the label just tags all emails we recieve from Tradingview and forwards them to our phone by MMS. A list of message gateways for some mobile phone carriers can be found [here](https://kb.sandisk.com/app/answers/detail/a_id/17056/~/list-of-mobile-carrier-gateway-addresses) at the time of this writing. Please note that the forward address has to be verified to become activated by typing the code recieved from gmail to your mobile phone via MMS. In the next article, we show a special case where we can read and forward our emails by SMS using google scripts.

