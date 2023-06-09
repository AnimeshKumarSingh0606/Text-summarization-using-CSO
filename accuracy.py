from rouge import Rouge
ROUGE = Rouge()
reference='''WHILE Hurricane Andrew was wreaking havoc across large parts of southern
Florida and Louisiana this week, a grade two dollar crisis (on a one-to-four
scale, four being most severe) was blowing itself out at the end of a
tumultuous few days for US and world financial markets.
On Wall Street, most of the damage from the currency storm was inflicted a
week ago Friday and on the following Monday, when bond yields jumped sharply
and the Dow Jones industrial average plunged by more than 75 points.
The flimsy walls erected hastily by the Federal Reserve and other big
central banks to protect the vulnerable dollar from a tidal wave of selling
on foreign exchange markets failed to hold; and as the sellers poured
through the breached barricades, the currency dropped.This was
its lowest-ever point against the D-mark.
The conditions necessary for a dollar crisis had been building up in
currency markets for some time. Interest rate differentials between US and
Germany widened over the summer as the Fed eased, and the Bundesbank
tightened, their respective monetary policies.
The failure of the US economy to climb out of recession with any vigour was
also making overseas investors increasingly unhappy about holding the dollar.
So, too, was the political hole President Bush had dug for himself in a
re-election battle that only a year ago was supposed to be a shoo-in for the incumbent.
Moreover, the fact that almost every central bank worth its salt was in the
markets trying to prop up the dollar served only to convince foreign
exchange dealers that the currency was heading in one direction  - down.
While there were plenty of reasons for the dealers to sell the dollar, the
logic for such a strongly negative reaction from bond and stock markets was less obviously compelling.
The second is that it makes it hard for the Fed to engineer another cut in
interest rates to stimulate the flagging recovery, and raises the
possibility that rates may actually have to go up to protect the currency.
The first explanation is not particularly convincing - imports account for
not much more than 10 per cent of US gross domestic product, so higher
import prices do not greatly effect the overall price level, which is now
around 3 per cent and heading lower.
The second explanation carries more weight. Although there is not much
chance, given the present economic and political climate, that the Fed will
raise rates to help the dollar, there is little doubt that the currency's
weakness makes it extremely difficult for the Fed to ease monetary policy again.
The fear that the Fed may be done with interest rate cuts for the present
economic cycle was also behind the selling in equity markets. But investors
in stocks were equally, if not more, troubled by the rise in bond yields.
Just over a week ago, the yield on the benchmark 30-year bond, which has
remained stubbornly high all year despite the poor state of the economy,
looked as if it might drop below 7.3 per cent.
The dollar was not the only story in financial markets this week, and the
devastating effect of Hurricane Andrew produced a typically hard-eyed,
although nonetheless logical, reaction from Wall Street.
The stocks of those insurance companies with the greatest exposure in
southern Florida, the area hit worst by the hurricane, all took a tumble.
But the relatively modest losses in Geico, Travelers and Progressive
suggested that the market believed the insurers were reserved or reinsured
adequately enough to cover hurricane-related claims.
The flip side of the hurricane's coin was a strong showing from the stocks
of home construction companies expected to benefit from demand for
rebuilding damaged or destroyed homes. Since there are an estimated 250,000
people left homeless by the storm, there is a lot of work to be done.
The biggest gains among construction stocks this week were posted by Lennar,
Oakwood Homes, Engle Homes and Fleetwood, the largest maker of
pre-manufactured homes in the US.'''
candidate='''tumultuous few days for US and world financial markets.its lowest ever point against the D mark.currency markets for some time.tightened their respective monetary policies.also making overseas investors increasingly unhappy about holding the dollar.re election battle that only a year ago was supposed to be a shoo in for the incumbent.exchange dealers that the currency was heading in one direction down.logic for such a strongly negative reaction from bond and stock markets was less obviously compelling.possibility that rates may actually have to go up to protect the currency.around per cent and heading lower.The second explanation carries more weight.weakness makes it extremely difficult for the Fed to ease monetary policy again.economic cycle was also behind the selling in equity markets.southern Florida the area hit worst by the hurricane all took a tumble.rebuilding damaged or destroyed homes.pre manufactured homes in the US.
'''
print(ROUGE.get_scores(candidate, reference))
