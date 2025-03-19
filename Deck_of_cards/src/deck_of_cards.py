import random

class Card:
    def __init__(self,suit,value):
        self.suit = suit
        self.value = value
    
    def __repr__(self):
        return f"{self.value} of {self.suit}"

class Deck:
    def __init__(self,):
        suits = ["Hearts","Diamonds","Clubs","Spades"]
        values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

        self.cards = [Card(suit,value) for suit in suits for value in values]


    def count(self):
        return len(self.cards)
        
    def __repr__(self):
        return f"Deck of {len(self.cards)} cards"

    

    def _deal(self,n):
        if not self.cards:
            raise ValueError("All cards have been dealt")
        
        cards_to_deal = min(n,len(self.cards))

        dealt_cards = self.cards[-cards_to_deal:]
        del  self.cards[-cards_to_deal:]

        return dealt_cards
    
    def shuffle(self):
        if self.count() != 52:
            raise ValueError("Only full decks can be shuffled")
       
        random.shuffle(self.cards)

    def deal_card(self):
        dealt_cards = self._deal(1)
        return dealt_cards[0]
        # return self._deal(1)[0]

    def deal_hand(self,number):
        dealt_cards = self._deal(number)
        return dealt_cards
        

if __name__ == "__main__":
    deck = Deck()
    print(deck)

    deck.shuffle()
    print("Shuffled deck: ",deck)

    while deck.count() > 0:
        print("\n---Yeni Tur---")
        print(f"kalan kartlar: {deck.count()}")


        number = int(input("kaç kart çekmek istiyorsunuz? "))
        card = deck.deal_hand(number)
        print(f"çekilen kart: {card}")

        go_on = input("Devam etmek istiyor musunuz? e/h: ")
        if go_on != 'E'.lower():
            print("Oyun sonlandırıldı")
            break
    
    if deck.count() == 0:
        print("\n destedeki tüm kartlar dağıtıldı! Oyun bitti")
