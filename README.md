# Syntatic Tree generation from POS-Tagging
## The experience

### Goal
* * *
This program was developed in order to generate a Syntatic Tree given a phrase in english, german, french or italian language.


### The work
* * *
The POS-Tagging was created using **spacy** library.<br>
Example of **spacy** use.

```python
# This code will print 'DET NOUN VERB', which are the POS-Taggin of the phrase 'The cat runs' 
import spacy
spacy_language = spacy.load('en_core_web_sm')
sentence = spacy_language('The cat runs.')
for t in sentence:
    print(t.pos_)
```
Was used two different predefined grammars, ones for english and german and another one for french and italian.
After POS-Tagging generation, we had to add each new POS-Tag to the predefined grammar.
At this point the new generated grammar could be used to generate the Syntatic tree, passing the
new grammar to **TreePrettyPrinter** object of *nltk*.

### Download
Before to run the code is necessary to run the following commands, which allow to download the
spacy grammar objects.

```bash
python -m spacy download en_core_web_sm
python -m spacy download it_core_news_sm
python -m spacy download fr_core_news_sm
python -m spacy download de_core_news_sm
```
