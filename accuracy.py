from rouge import Rouge
ROUGE = Rouge()
reference='''In a short stock markets provides a place where market participants can make transactions of shares and other eligible investement firms, tools and products without any fear of fraud and deception with zero to low operational risk
Operating under the defined rules as stated by the stock markets act as primary and secondary markets As primary market stock market enables companies to publish and sell their shares to investors and public through the process of an initial public offering
This activity helps companies acquire needed funds from investors and public It essentially means that a company breaks itself into a number of shares for example thousand shares and publishes a part of those shares  say hundred shares to interested candidates at a valuation per share To help proced this process a company wants a marketplace where these shares can be sold
If everything goes perfectly then the company will sell its shares at a price per share and collect funds Investors will get the company shares  which they can expect to hold for their preferred duration in anticipation of rise in share price and any potential income in the form of dividend payments'''
candidate='''In a nutshell  stock markets provide a secure and regulated environment where market participants can transact in shares and other eligible financial instruments with confidence  with zero to low operational risk
Operating under the defined rules as stated by the regulator  the stock markets act as primary markets and secondary markets   As a primary market  the stock market allows companies to issue and sell their shares to the common public for the first time through the process of an initial public offering  IPO
This activity helps companies raise necessary capital from investors
It essentially means that a company divides itself into a number of shares  for example     million shares  and sells a part of those shares  say    million shares  to the public at a price  for instance      per share    To facilitate this process  a company needs a marketplace where these shares can be sold
This marketplace is provided by the stock market
If everything goes according to plan  then the company will successfully sell the   million shares at a price of     per share and collect     million worth of funds
Investors will get the company shares  which they can expect to hold for their preferred duration  in anticipation of rising in share price and any potential income in the form of dividend payments'''
print(ROUGE.get_scores(candidate, reference))
