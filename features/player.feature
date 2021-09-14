Feature: The player for the game of 21

Scenario: Receive initial cards
  Given a player
  When the round starts for the player
  Then the player receives two cards

Scenario Outline: Get hand total
  Given a <hand> for the player
  When the player sums the cards
  Then the <total> is correct for the player

  Examples: Hands
  | hand          | total |
  | K,K,A         | 21    |
  | A,Q           | 21    |
  | 2,3           |  5    |
  | 7,5           | 12    |
  | A,A,A         | 13    |

Scenario Outline: Determine player loses if hand is greater than 21
  Given a hand <total> for the player
  When the player sums the cards and the sum is greater than 21
  Then the player loses

  Examples: Hands
  | total |
  | 23    |
  | 24    |
  | 25    |

Scenario Outline: Determine if the player wins if his hand equals 21
  Given a hand <total> for the player
  When the player sums the cards and the sum is equal to 21
  Then the player wins

  Examples: Hands
  | total |
  | 21    |


Scenario Outline: Determine if the player loses if his hand equals 21 and dealer hand equals 21 also
  Given a hand <totalPlayer> for the player
  Given a hand <totalDealer> for the dealer
  When the player and the dealer sums the cards and the sum of both are equal to 21
  Then the player loses

  Examples: Hands
  | totalPlayer | totalDealer  |
  | 21          |	 21          |

Scenario Outline: Determine if the player wins if no one reaches total of 21 in the hand and his hand is greater than the dealer
  Given a hand <totalPlayer> for the player
  Given a hand <totalDealer> for the dealer
  When the player and the dealer sums the card and the dealer sum is greater than 17 and the player sum is greater than the dealer sum
  Then the player wins

  Examples: Hands
  | totalPlayer | totalDealer  |
  | 20          |	 18          |