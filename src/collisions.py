import random

def how_many_before_collision(buckets, loops=1):
  """
  Roll random hashed indexes into buckets and print
  how many rolls before a collision

  Run loop times
  """
  for i in range(loops):
    tries = 0
    tried = set()
    tried_list = []

    while True:
      random_key = str(random.random())
      hash_index = hash(random_key) % buckets
      if hash_index not in tried:
        tried.add(hash_index)
        tries += 1

      # if hash_index not in tried_list:
      #   tried_list.append(hash_index)
      #   tries += 1
      # We can use a list instead of a set but the list might give a timeout error if buckets is very high. 
      # Sets are more efficient than a list

      else:
        # We have found a collision
        break
    
    print(f'{buckets} buckets, {tries} hashes before collision. ({tries/buckets *100:.1f}%) ')
    # :.1f means round it off to 1 decimal point 

how_many_before_collision(10000, 10)


