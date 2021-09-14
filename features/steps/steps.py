from behave import *
from Blackjack import *


################################
#	 		GIVEN
################################

# DEALER INI

@given('a dealer')
def step_impl(context):
    context.dealer = Dealer()

@given('a hand {total:d} for the dealer')
def step_impl(context, total):
	context.dealer = Dealer()
	context.dealer.total = total

@given('a {hand} for the dealer')
def step_impl(context, hand):
	context.dealer = Dealer()
	context.dealer.hand = hand.split(',')

# DEALER FIM


# PLAYER INI

@given('a player')
def step_impl(context):
    context.player = Player()

@given('a hand {total:d} for the player')
def step_impl(context, total):
	context.player = Player()
	context.player.total = total

@given('a {hand} for the player')
def step_impl(context, hand):
	context.player = Player()
	context.player.hand = hand.split(',')

# PLAYER FIM



################################
#	 		WHEN
################################


# DEALER INI

@when('the round starts for the dealer')
def step_impl(context):
	context.dealer.newRound()
	
@when('the dealer sums the cards')
def step_impl(context):
	context.dealer_total = context.dealer.getHandTotal()

@when('the dealer determines a play')
def step_impl(context):
	context.dealer_play = context.dealer.determinePlay(context.dealer.total)

# DEALER FIM


# PLAYER INI

@when('the round starts for the player')
def step_impl(context):
	context.player.newRound()

@when('the player sums the cards')
def step_impl(context):
	context.player_total = context.player.getHandTotal()

@when('the player sums the cards and the sum is greater than 21')
def step_impl(context):
	context.player_lost = context.player.checkIfLost(context.player.total)

@when('the player sums the cards and the sum is equal to 21')
def step_impl(context):
	context.player_won = context.player.checkIfWon(context.player.total, 20)

@when('the player and the dealer sums the cards and the sum of both are equal to 21')
def step_impl(context):
	context.player_lost = not context.player.checkIfWon(context.player.total, context.dealer.total)

@when('the player and the dealer sums the card and the dealer sum is greater than 17 and the player sum is greater than the dealer sum')
def step_impl(context):
	context.player_won = context.player.checkIfWon(context.player.total, context.dealer.total)

# PLAYER FIM


################################
#	 		THEN
################################


# DEALER INI

@then('the dealer gives itself two cards')
def step_impl(context):
	assert (len(context.dealer.hand) == 2)

@then('the dealer chooses a play')
def step_impl(context):
	assert (context.dealer.makePlay() in ['stand', 'hit'])

@then('the {total:d} is correct for the dealer')
def step_impl(context, total):
	assert (context.dealer_total == total)

@then('the {play} is correct for the dealer')
def step_impl(context, play):
	assert (context.dealer_play == play)

# DEALER FIM


# PLAYER INI

@then('the player receives two cards')
def step_impl(context):
	assert (len(context.player.hand) == 2)

@then('the {total:d} is correct for the player')
def step_impl(context, total):
	assert (context.player_total == total)

@then('the {play} is correct for the player')
def step_impl(context, play):
	assert (context.player_play == play)

@then('the player loses')
def step_impl(context):
	assert(context.player_lost)

@then('the player wins')
def step_impl(context):
	assert(context.player_won)

# PLAYER FIM