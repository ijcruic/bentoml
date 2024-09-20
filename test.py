import bentoml

with bentoml.SyncHTTPClient("http://localhost:3000") as client:
    result = client.summarize(
        text=''' 
Donald Trump risks being doomed by what he wrought in North Carolina.

An already fiercely fought presidential contest in the critical swing state was thrown into greater turmoil Thursday by a stunning CNN investigation revealing a porn-site scandal surrounding Republican gubernatorial candidate Mark Robinson.

Lt. Gov. Robinson, whose politics and personality are extreme even by the standards of Trump’s MAGA movement, referred to himself as a “black NAZI!” on a pornography website’s message board more than a decade ago and expressed support for reinstating slavery, CNN’s KFile reported. Many of the remarks were lewd and gratuitously sexual in nature.

Robinson denied he made the comments, which predated his political career. But his proximity to Trump, who dubbed him “Martin Luther King on steroids” and had him on stage at a recent rally, jolted the White House race.

Vice President Kamala Harris’ campaign swiftly highlighted the scandal’s national implications and tried to equate Trump with Robinson as it argues that the ex-president is anti-woman, immoral, extreme and unfit to serve. The campaign for instance posted photos of the two men together on social media with an emoji of Trump’s signature thumbs-up.

The question of whether Robinson’s political disaster will seriously hurt Trump’s chances in one of the most tightly fought and important battleground states is a complex one. Trump voters are hugely loyal to their candidate — so it doesn’t necessarily follow that if they disdain Robinson, they won’t vote for the ex-president. And Democrats have several times thought North Carolina was ripe to pick off in recent elections — only for it to stubbornly stay red. Still, any fall-off of Republican turnout could be significant in a race that is currently neck-and-neck. And the implications are massive, since North Carolina could open up a fallback route to the White House for Harris in the event that she loses one of the Blue Wall states of Pennsylvania, Wisconsin or Michigan.

And it would be an ironic historical coda if Trump becomes collateral damage to a Republican who would have been anathema to the old GOP but who thrived in the smash mouth political era the ex-president nurtured.
'''
    )

print(result)