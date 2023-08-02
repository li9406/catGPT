# catGPT

Everyone is now talking about chatGPT. As amazing as it is, it is simply a well trained next
word prediction model, similar to how the auto-complete on your phone but on a larger scale on
the vast knowledge of the internet. In other words, chatGPT helps you finish your sandwiches
sentences. You recall learning Tries from FIT2004 which can also be used for auto-complete.
Thus, you set out to implement something similar using Tries.

Unfortunately, you do not have the computing power needed to process human language. Your
friend, Kim Katdashian who is a cat expert suggest doing a variant for cats because it is simpler.
She call this catGPT. The concept is simple – the model would be able to complete what does
a cat say automatically:
1. Let say Tabby the cat goes “meow meoow meow meowth...”.
2. Then catGPT will be able to complete Tabby’s sentence with “... meow meuw nyan”.
Kim states that there are a total of 26 words in a cat’s vocabulary. You realized that it is
possible to map this to the 26 letters in the English language. For example:
* meow = a
* meoow = b
* meuw = c
* meuuw = d
* meuow = e
* ...
* nyan = y
* meowth = z
In the example above, Tabby’s initial sentence could be viewed as abaz and then it is auto-completed to be acy. It is auto-completed this way because many many cats would finish their
sentence in such a way. Luckily, Kim has collected a large set of cat sentences to help your
Trie decide how a cat sentence would be completed. These sentences are stored in a long list
of sentences, formatted as follows:
* abc
* abazacy
* dbcef
* gdbc
* abazacy
* xyz
* ...
* abazacy
* dbcef

## The Trie Data Structure
You must write a class CatsTrie that encapsulates all of the cat sentences. The __init__
method of CatsTrie would take as input a list of timelines, sentences, represented as a list
of strings with:
* N sentences, where N is a positive integer.
* The longest sentence would have M characters, as mapped from the cat vocabulary. M
is a positive integer.
* A cat word can occur more than once in a single sentence. For example, the string baacbb
represents a valid sentence.
* It is possible for more than a single sentence to have the same words. Have a look at the
example in Section 2.4.
* You can assume that there is only a maximum of 26 unique cat words in total, represented
as lower case characters from a to z.

For the example stated earlier, the CatsTrie object will contain all the following sentences abc,
abazacy, dbcef, gdbc, abazacy, xyz, ..., abazacy, dbcef.

Consider implementing a Node class to help encapsulate additional information that you might
want to store in your CatsTrie class to help solve this problem.

## Auto-Completing Sentences
You would now proceed to implement autoComplete(self, prompt) as a function within the
CatsTrie class. The function accepts 1 argument:
* prompt is a string with characters in the set of [a...z]. This string represents the
incomplete sentence that is to be completed by the trie.

The function would then return a string that represents the completed sentence from the
prompt. Do note the following:
* If such a sentence exist, return the completed sentence with the highest frequency in the
cat sentences list.
* If there are multiple possible auto-complete sentences with the same highest frequency,
then you would return the lexicographically smaller string.
* If such a sentence does not exist, return None

## Complexity
The complexity for this task is separated into 2 main components.
The __init__(sentences) constructor of CatsTrie class would run in O(NM) time and space
where:
* N is the number of sentence in sentences.
* M is the number of characters in the longest sentence.
The autoComplete(self, prompt) of the CatsTrie class would run in O(X + Y ) time where:
* X is the length of the prompt.
* Y is the length of the most frequent sentence in sentences that begins with the prompt,
unless such sentence do not exist (in which case autoComplete(self, prompt) should
have complexity O(X)). Thus, this is an output-sensitive complexity.
