def clear():
    print("\n"*100)
bids = {}
def get_bid():
    name = input("what is your name: ")
    bid = int(input("what is your bid: "))
    bids[name] = bid
    clear()
is_continue = True
while is_continue:
    get_bid()
    x = input("are there more bidders : yes or no").lower()
    if x == "no":
        is_continue = False
higest_bid = 0
winner = ""
for bidder in bids:
    if bids[bidder] > higest_bid:
        higest_bid = bids[bidder]
        winner = bidder
print(f"The winner is {winner} with {higest_bid} bid ")

