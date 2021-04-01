import cbpro
import time

def myDataApi():
     public_client = cbpro.PublicClient()
     key = ''  # Your personal key
     b64 = ''  # Your personal b64 passkey
     passphrase = '' # Your personal passphrase
     auth_client = cbpro.AuthenticatedClient(key, b64, passphrase)
     x1 = auth_client.get_accounts()
     my_currencies = dict()
     cryptoValue = dict()
     portfolio = dict()
     portfolioValue = 0

     for x in x1:
          if float(x['balance']) != 0:  #finds all your currencies
               my_currencies[x['currency']] = float(x['balance'])
     t = time.localtime()
     current_time = time.strftime('%H:%M', t)  #add ":%S" after %M if you also want seconds
     for x in my_currencies.keys():

          cryptoValue[x]= float(public_client.get_product_24hr_stats(x + '-EUR')['last']) #Fetches the live value of all your currencies
          portfolio[x] = cryptoValue[x]*my_currencies[x] #Multiplies the value of the currency by the amount of given currency that you have
          portfolioValue += portfolio[x] #Calculates the total value of your portfolio by adding the previous amount we got, for all the currencies
          a = open('myCrypto.txt', 'a') #This is the document where all your current currencies will be compared
          a.write(current_time + ' ' + x + ' ' + str(cryptoValue[x] * my_currencies[x]) + '\n')

     f = open("values2.txt", "a")
     f.write(current_time + ' ' +  str(portfolioValue) + '\n')  #This is the document where your portfolio value will be written in



while True:
   myDataApi()
   time.sleep(60)    #choose how frequently you want your portfolio to update (in seconds)
