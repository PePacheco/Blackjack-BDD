from behave import *
from Blackjack import *

################################
#	 		GIVEN
################################

# First scenario
@given('a dealer')
def step_impl(context):
    context.dealer = Dealer()

# Second scenario
@given('a hand {total:d}')
def step_impl(context, total):
	context.dealer = Dealer()
	context.total = total

# Third scenario
@given('a {hand}')
def step_impl(context, hand):
	context.dealer = Dealer()
	context.dealer.hand = hand.split(',')


################################
#	 		WHEN
################################

# First scenario
@when('the round starts')
def step_impl(context):
	context.dealer.newRound()

# Second scenario	
@when('the dealer sums the cards')
def step_impl(context):
	context.dealer_total = context.dealer.getHandTotal()

# Third scenario
@when('the dealer determines a play')
def step_impl(context):
	context.dealer_play = context.dealer.determinePlay(context.total)


################################
#	 		THEN
################################

# First scenario
@then('the dealer gives itself two cards')
def step_impl(context):
	assert (len(context.dealer.hand) == 2)

@then('the dealer chooses a play')
def step_impl(context):
	assert (context.dealer.makePlay() in ['stand', 'hit'])

# Second scenario	
@then('the {total:d} is correct')
def step_impl(context, total):
	assert (context.dealer_total == total)

# Third scenario
@then('the {play} is correct')
def step_impl(context, play):
	assert (context.dealer_play == play)
