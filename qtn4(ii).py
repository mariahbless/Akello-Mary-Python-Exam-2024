#question 4ii

def counting_occcurance(sentence):
  words = sentence.split()
  word_counting = {}

  for word in words:
    if word in word_counting:
      word_counting[word] +=1
    else:
      word_counting[word] = 1
      return word_counting
    sentence = "python exam"
    print(counting_occcurance(sentence))