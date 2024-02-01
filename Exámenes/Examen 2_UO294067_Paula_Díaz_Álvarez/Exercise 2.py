def moving_average(word,amount):
    """Calculates the moving average of the scores of each word with 2 digits
    -word: A non empty list of n words
    -amount: It's a number between (1 and n-1)
    -Returns a list with all the moving averages"""
    mov_averages=[]
    if amount<1 or amount>=len(word)-1:
        print(f"The amount must be in [1,{len(word)-1}]")
        return None
    for i in range (0,len(word),1):
        if amount>=i+1: #if the word is at a position less than or equal to the amount, I start counting at the word 0
            lower_limit=0
        else: #else I count the word and the 3 words before
            lower_limit=i+1-amount
        
        #Calculate the sum of all the words from lower_limit to the current word
        sum_scores=0
        number_word=0 #I count the words because it depends on the position
        for j in range(lower_limit,i+1,1):
            sum_scores+=calculate_score(word[j])
            number_word+=1
        
        # if i+1<amount:
        #     average=round(sum_scores/(i+1),2)
        # else:
        #     average=round(sum_scores/amount,2)

        average=round(sum_scores/number_word,2) #Calculate the average
        mov_averages.append(average) #Adding the average to the list
    return mov_averages


def calculate_score(word):
    """Calculates the score of a word (sum of all the ordinals of the chars of the word
    -word: It's the given word
    -Returns the score of that word"""
    score=0
    for i in range(0,len(word),1):
        score+=ord(word[i])
    return score


######################################
words=["amalgamas","desde","ahora","idiosincrasia","eufemismo","estudiante","profesor","pero","y","oviedo"]
amount=4
print(moving_average(words,amount))
