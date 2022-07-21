from discord_webhook import DiscordWebhook, DiscordEmbed
import time

print("Fortnite Account Puller")
print("Made by zt#7380")
print('')

epic = input('Epic: ')
linked = input('Linked Accs/Connections (ex. PlayStation: name, Xbox: name, Nitendo: name): ')
email = input('Email(s): ')
odis = input('OG Display Name(s): ')
ip = input('IP(s): ')
login = input('Recent Login(s): ')
place = input('Where was the account made (New Jersey, City): ')
pur = input('Recent/Old Purchaes (make sure you have invoice ID): ')
pm = input('Payment Methods used to purchase the items: ')

final = (f'Hi, Epic Games im requesting to get the email changed on my account. The Display Name is : {epic}, The linked Accounts are: {linked}, I have full OG info and can prove it. The old email(s) to the account is: {email}, Old Display Name(s) is: {odis}, Old/New IP(s): {ip}, Recent Logins: {login}, Where the account was made: {place}, Recent/Old Purchaes: {pur}, Payment methods used to purchase these items: {pm}')

def main():
 fort = ''
 webhook = DiscordWebhook(url=fort, content=f"@everyone Copy & Paste: ```py\n{final}```")
 response = webhook.execute()
 print('webhook sent with info!')
 print('')
 print(final)
 time.sleep(15)
main()
