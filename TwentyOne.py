import easygui
from TwentyOneSub import *

newGame = easygui.ynbox('Welcome!\nDo you want to play 21?', 'Twenty One')


while newGame:
    deck = DeckOfCards()
    deck.shuffleDeck()

    newRound = True
    while newRound:
        player = Player()
        dealer = Player()

        moreCardsPlayer = True
        moreCardsDealer = False

    # -----------------------------------------------------------------------------
    # Player's sequence

        print("Player:")
        while moreCardsPlayer:
            card = deck.requestNewCard()
            if deck.cardsLeft <= 0:
                easygui.msgbox("Sorry, but there are no more cards. Game over")
                exit()

            player.calcTotalScore(card.value)
            print(str(deck.cardsLeft) + "\t" +  card.to_str() + "\t" + str(card.value) + "\t" + str(player.totalScore))

            msg = card.to_str() + "\n" + "Your total score is " + str(player.totalScore) + "\n\n"

            if player.totalScore > 21:
                moreCardsPlayer = False
                msg += "Sorry but you're busted\n\nDo you want to play again?"
                newRound = easygui.ynbox(msg, "Twenty One")
                if not newRound: exit()

            if player.totalScore == 21:
                moreCardsPlayer = False
                msg += "Congratulations - you win!!\n\nDo you want to play again?"
                newRound = easygui.ynbox(msg, "Twenty One")

            if player.totalScore < 21:
                msg += "Do you want another card?"
                moreCardsPlayer = easygui.ynbox(msg, "Twenty One")
                if not moreCardsPlayer: moreCardsDealer = True

        # End of 'while moreCardsPlayer:'

    # -----------------------------------------------------------------------------
    # Dealer's sequence

        print("Dealer:")
        while moreCardsDealer:
            card = deck.requestNewCard()
            if deck.cardsLeft <= 0:
                easygui.msgbox("Sorry, but there are no more cards. Game over")
                exit()

            dealer.calcTotalScore(card.value)
            print(str(deck.cardsLeft) + "\t" +  card.to_str() + "\t" + str(card.value) + "\t" + str(dealer.totalScore))

            msg = card.to_str() + "\n" + "Dealer's total score is " + str(dealer.totalScore) + "\n"
            msg +=                       "Your total score is     " + str(player.totalScore) + "\n\n"

            if dealer.totalScore > 21:
                moreCardsDealer = False
                msg += "Dealer's busted - Congratulations!!\n\nDo you want to play again?"
                newRound = easygui.ynbox(msg, "Twenty One")

            if dealer.totalScore == 21:
                moreCardsDealer = False
                msg += "Dealer wins!\n\nDo you want to play again?"
                newRound = easygui.ynbox(msg, "Twenty One")

            if dealer.totalScore < 21:
                if dealer.totalScore >= DEALER_STOPS_AT:
                    moreCardsDealer = False
                    if dealer.totalScore > player.totalScore:
                        msg += "Sorry,dealer wins. \n\nDo you want to play again?"
                        newRound = easygui.ynbox(msg, "Twenty One")
                    else:
                        msg += "Congratulations - you win!!\n\nDo you want to play again?"
                        newRound = easygui.ynbox(msg, "Twenty One")
                else:
                    msg += "Dealer wants another card."
                    easygui.msgbox(msg, "TwentyOne")

        # End of 'while moreCardsDealer:'

    # -----------------------------------------------------------------------------

    # End of 'while newRound:'

    newGame = False

# End of 'while newGame:'


