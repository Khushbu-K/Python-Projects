x = int(input())
movie_tickets = 100
popcorn_buckets = 50

def buy_movie_popcorn():
    if x >= 100:
        remaining_after_movie = x - movie_tickets
        popcorn_counts = 0
        print("You bought 1 movie ticket.")
        if remaining_after_movie < 50:
            print(f"You could only buy movie tickets. Your remaining amount is : {remaining_after_movie}")
        while remaining_after_movie >= 50:
            remaining_after_movie = remaining_after_movie - popcorn_buckets
            popcorn_counts += 1
            if remaining_after_movie < 50:
                print(f"After buying {popcorn_counts} popcorn buckets, remaining amount left is: {remaining_after_movie}")
    else:
        print("Insufficient balance")


buy_movie_popcorn()