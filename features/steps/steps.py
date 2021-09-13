from behave import *
from Blackjack import *

################################
#	 		GIVEN
################################


# Dealer features INI
@given('a dealer')
def step_impl(context):
    context.dealer = Dealer()

@given('a hand {total:d}')
def step_impl(context, total):
	context.dealer = Dealer()
	context.total = total

@given('a {hand}')
def step_impl(context, hand):
	context.dealer = Dealer()
	context.dealer.hand = hand.split(',')
# Dealer features FIM


################################
#	 		WHEN
################################


# Dealer features INI
@when('the round starts')
def step_impl(context):
	context.dealer.newRound()
	
@when('the dealer sums the cards')
def step_impl(context):
	context.dealer_total = context.dealer.getHandTotal()

@when('the dealer determines a play')
def step_impl(context):
	context.dealer_play = context.dealer.determinePlay(context.total)
# Dealer features FIM

################################
#	 		THEN
################################


# Dealer features INI
@then('the dealer gives itself two cards')
def step_impl(context):
	assert (len(context.dealer.hand) == 2)

@then('the dealer chooses a play')
def step_impl(context):
	assert (context.dealer.makePlay() in ['stand', 'hit'])

@then('the {total:d} is correct')
def step_impl(context, total):
	assert (context.dealer_total == total)

@then('the {play} is correct')
def step_impl(context, play):
	assert (context.dealer_play == play)
# Dealer features FIM
