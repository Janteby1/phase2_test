Phase 2 Assessment - Code Against Humanity!

Congratulations on making it to this point! You're just one final challenge away from moving onto Phase 3, your final project, and the rest of your technology career.

If you have any questions regarding the assignment, please ask! If you have any questions regarding Python, Django, Javascript, now is not the time.

We're going to code a VERY simple web version of Cards Against Humanity. This is a fun one - work quickly and make it happen.

In case you've never played the game, the rules are simple. A group of three or more people can play. One player selects a "Black Card", which contains a question or a fill-in-the-blank. Here are some example Black Cards:

    What gives me uncontrollable gas?
    The class field trip was completely ruined by __________.
The other players select "White Cards" to fill in the answer. Whoever picks the funniest answer wins the round. Some example White Cards:

    Sniffing Glue
    A defective condom.
    Dick Cheney
Get the idea? You can look at the website if you still don't get it.

Your Challenge

Using Django, we're going to seed a database full of Black Cards and White Cards.

Here is a textfile containing blackcards

Here is textfile containing whitecards

We're going to have three routes on our Django Project.

"GET /" will be our main page.
"GET /blackcards" will return a JSON of a random Black Card in the database.
"GET /whitecards" will return a user a JSON response of 5 random white cards in the database.
Your main page should have a button that makes an AJAX GET request to /blackcards that displays the returned Black Card on the page. There should only ever be 1 Black Card on the page, and it should always be in the same place.

Your main page should also have a button that makes an AJAX GET request to /whitecards that displays the returned White Cards on the page. There should only ever be 5 White Cards on the page, and they should always be in the same place.

You should probably use Mustache for the card templates.

Once you have that working, style your White and Black cards. They should look as close as possible to what they actual cards look like - see them here

That font is Helvetica Bold 15pt. That's not a free font - try a lookalike like Droid Sans or Open Sans. Follow the directions on that page to link the font in your site.

Don't worry about the logo on the bottom of the cards - but DO worry about the black / white borders, card size / shape, and anything else you think makes your web implementation look like them.

Finally, if you have time left, make the white cards clickable. When you click the card, it should vaguely highlight it. The full Black Card + White Card sentence should display somewhere on the page for maximum funny.

Bonus: When you complete that, write atleast 3 tests for each of your Django routes.